#!/usr/bin/env python3

import re
def check_zip_code(text):
  result = re.search(r".[0-9]{5}", text)
  return result != None
  

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print("this is an add test")