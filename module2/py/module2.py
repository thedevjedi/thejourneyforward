#!/usr/bin/env python3

import os
import requests
import pathlib
from requests.api import request

#SRC = "/data/feedback"
SRC = "/home/scottdavis/eclipse-workspace/module1"
content_dict = {}

def read_myfile(filename):
    count = 1
    thefile = os.path.basename(filename)
    keystr = ""
    with open(filename) as file:
        for line in file:
            if count == 1:
                keystr = thefile + "_title"
                #print(keystr)
            elif count == 2:
                keystr = thefile + "_name"
                #print(keystr)
            elif count == 3:
                keystr = thefile + "_date"
                #print(keystr)
            elif count == 4:
                keystr = thefile + "_feedback"
                #print(keystr)
            else:
                print("other")
            count += 1          
            content_dict[keystr] = line
            
    return ""


def main():
    for filename in os.listdir(SRC):
        srcstr = SRC + "/" + filename
        if os.path.isfile(srcstr) and srcstr.endswith(".txt"):         
            read_myfile(srcstr)
            
    urlstr = "http://34.71.108.60/feedback"
    
    for key, value in content_dict.items():
        cleaned_key = key[key.index("_")+1:]
        myobj = {cleaned_key : value}
        x = requests.post(urlstr, data = myobj)
        print(x)
    
main()