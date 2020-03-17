#!/usr/bin/env python3


import json
import locale
import sys

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

import os.path
import mimetypes
import smtplib
import getpass


import emails
import os
import reports
    
def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data

def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(car["car_make"], car["car_model"], car["car_year"])

def process_data(data):
    """Analyzes the data, looking for maximums.

         Returns a list of lines that summarize the information.
    """
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    max_revenue = {"revenue": 0}
    max_sales = {}
    most_popular_year = {}
    
    for item in data:
        # Calculate the revenue generated by this model (price * total_sales)
        # We need to convert the price from "$1234.56" to 1234.56
        thecar = format_car(item["car"])
        salescount = item["total_sales"]
                   
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = salescount * item_price
        
        max_revenue[thecar] = item_revenue
        
        # TODO: also handle max sales
        if len(max_sales) > 0:
            if max_sales.get(thecar):
                ts = item["total_sales"]
                if ts > salescount:
                    max_sales[thecar] = ts
            else:
                ts = item["total_sales"]
                [(k, v)] = max_sales.items()
                if ts > v:
                    max_sales.clear()
                    max_sales[thecar] = ts
        else:
            max_sales[thecar] = salescount
            
        # TODO: also handle most popular car_year
        tc = item["car"]
        if len(most_popular_year) > 0:
            if most_popular_year.get(tc["car_year"]):
                most_popular_year[tc["car_year"]] += item["total_sales"]
            else:
                most_popular_year[tc["car_year"]] = item["total_sales"]
        else:
            most_popular_year[tc["car_year"]] = item["total_sales"]
        
    #pop year    
    yr_maximum = max(most_popular_year, key=most_popular_year.get)
    yr_max_val = most_popular_year[yr_maximum]
    
    #most sales
    [(make_model_year, sale_count)] = max_sales.items()
    
    #max rev
    max_rev = max(max_revenue, key=max_revenue.get)
    rev_max_val = max_revenue[max_rev]
    
    
    summary = ["The {} generated the most revenue: ${}".format(max_rev, rev_max_val),]
    summary.append(["<br/>"])
    summary.append(["The {} had the most sales: {}".format(make_model_year,sale_count)])
    summary.append(["<br/>"])
    summary.append(["The most popular year was {} with {} sales.".format(yr_maximum,yr_max_val)])                  

    return summary



def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
    return table_data
   

def main(argv):
    """Process the JSON data and generate a full report out of it."""
    tf = '/home/scottdavis/eclipse-workspace/mytest/' + 'cars.json'
    data = load_data(tf)
    summary = process_data(data)
    

    # TODO: turn this into a PDF report
    reports.generate("/tmp/cars.pdf", "Sales summary for last month", summary, cars_dict_to_table(data))
    
    # TODO: send the PDF report as an email attachment
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Sales summary for last month"
    body = summary
    
    message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
    emails.send(message)
    
if __name__ == "__main__":
    main(sys.argv)
