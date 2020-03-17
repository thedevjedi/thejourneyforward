#!/usr/bin/env python3

import emails
import os
import reports

table_data=[
  ['Name', 'Amount', 'Value'],
  ['elderberries', 10, 0.45],
  ['figs', 5, 3],
  ['apples', 4, 2.75],
  ['durians', 1, 25],
  ['bananas', 5, 1.99],
  ['cherries', 23, 5.80],
  ['grapes', 13, 2.48],
  ['kiwi', 4, 0.49]]
reports.generate("/tmp/cars.pdf", "A Complete Inventory of My Fruit", "This is all my fruit.", table_data)

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Sales summary for last month"
body = "The Mercedes-Benz E-Class (2009) generated the most revenue: $22749529.02\nThe Acura Integra (1995) had the most sales: 1192\nThe most popular year $

message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
emails.send(message)
