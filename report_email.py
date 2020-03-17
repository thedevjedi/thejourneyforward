#!/usr/bin/env python3

import os.path
import emails
import reports
import datetime
import sys
import os

SRC = "~/supplier-data/descriptions/"
SRC = "/home/scottdavis/eclipse-workspace/images"
URLSTR = "http://0.0.0.0/fruits"

content_dict = {}

def read_myfile(filename):
    keystr = os.path.basename(filename)
    my_values_list = []
    with open(filename) as file:
        for line in file:
            my_values_list.append(line.replace("lbs","").strip())
            content_dict[keystr] = my_values_list
    return ""

def create_body_para(a):
    for filename in os.listdir(SRC):
        srcstr = SRC + "/" + filename
        if os.path.isfile(srcstr) and srcstr.endswith(".txt"):         
            read_myfile(srcstr)
    thebodycontent = []
    for key, value in content_dict.items():
        fruit_name = value[0]
        fruit_weight = value[1]
        
        thebodycontent.append("name: " + fruit_name)
        thebodycontent.append("<br />")
        thebodycontent.append("weight: " + str(fruit_weight) + " lbs")
        thebodycontent.append("<br />")
        thebodycontent.append("<br />")

        thetext = ''.join(thebodycontent)
        d = datetime.datetime.today()
        formatted_date = d.strftime("%B %d, %Y")
        reports.generate(SRC + "/processed.pdf", "Processed Update on " + formatted_date, thetext)   
    
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
       
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    
    message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send(message)
    
    return thebodycontent

if __name__ == "__main__":
    create_body_para(sys.argv)