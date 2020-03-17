#!/usr/bin/env python3

import os
import requests
import pathlib
import json


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
def main():
    for filename in os.listdir(SRC):
        srcstr = SRC + "/" + filename
        if os.path.isfile(srcstr) and srcstr.endswith(".txt"):         
            read_myfile(srcstr)
            
    for key, value in content_dict.items():
        fruit_name = value[0]
        fruit_weight = value[1]
        fruit_description = value[2]
        file_name = key.replace("txt","jpeg")
        thejsonobject = ("{" + "\"name\": " + "\"" + "{}".format(fruit_name) + "\"" 
                         + "," + "\"weight\": " + "{}".format(fruit_weight)
                         + "," + "\"description\": " + "\"" + "{}".format(fruit_description) + "\""
                         + "," + "\"image_name\": " + "\"" + "{}".format(file_name) + "\"" + "}")
        
        print(thejsonobject)
        #x = requests.post(URLSTR, data = thejsonobject)
        #print(x)  
    
main()