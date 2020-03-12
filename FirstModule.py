'''
Created on Mar 5, 2020

@author: scottdavis
'''
#!/usr/bin/env python3
import datetime
import os
import csv
import re


def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$",name)
    return "{} {}".format(result[2], result[1])


def read_myfile(filename):
    outputtext = ""
    linetext = ""
    with open(filename) as file:
        for line in file:
            linetext = line.upper()
            outputtext += linetext
    return outputtext

def write_myfile(filename):
    with open(filename,"a") as file:
        file.write("this is added to the end.\n")
    return "File appended."

def get_modified(filename):
    timestamp = os.path.getmtime(filename)
    return str(datetime.datetime.fromtimestamp(timestamp))

def read_mycsvfile(filename):
    outputtext = ""
    with open(filename) as file:
        csvf = csv.reader(file)
        for line in csvf:
            name, dob, sex = line
            outputtext += "Name: {}, DOB: {}, Sex: {}, ".format(name,dob,sex)
    return outputtext

def write_mycsvfile(filename):
    listtext = [["workstation.local","10.0.0.2"],["server.local","10.0.0.1"]]
    
    with open(filename, "w") as file:
        writer = csv.writer(file)
        writer.writerows(listtext)
        
    return "File write OK."

def read_mycsvDictfile(filename):
    outputtext = ""
    with open(filename) as file:
        reader = csv.DictReader(file)
        for line in reader:
            outputtext += "Name: {}, Users: {}  ".format(line["name"], line["users"])
    return outputtext

def write_mycsvDictfile(filename):
    users = [ {"name": "john doe", "username": "jdoe", "dept": "it"},{"name": "john downer", "username": "jdowner", "dept": "fin"}]
    keys = ["name","username","dept"]
    with open(filename, "w") as file:
        writer = csv.DictWriter(file,fieldnames=keys)
        writer.writeheader()
        writer.writerows(users)
    return "File write of dicts OK."
    
thereadfile = "readthis.txt"
thecsvreadfile = "csvfile.txt"

print(read_myfile(thereadfile))

print(write_myfile(thereadfile))

print(read_myfile(thereadfile))

print(get_modified(thereadfile))

print(read_mycsvfile(thecsvreadfile))

write_mycsvfile("hosts.csv")

print(read_myfile("hosts.csv"))

print(read_mycsvDictfile("mydictfile.txt"))

print(write_mycsvDictfile("mydictWritefile.txt"))

print(read_myfile("mydictWritefile.txt"))

print(rearrange_name("Davis, Scott"))