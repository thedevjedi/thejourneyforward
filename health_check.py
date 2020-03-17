#!/usr/bin/env python3

import shutil
import emails
import psutil
import socket
from psutil import virtual_memory
import os

def check_health():
    errormessage = ""
    if psutil.cpu_percent(interval=1) > 80:
        errormessage = "CPU usage is over 80%"
    
    total, used, free = shutil.disk_usage("/")
    
    td = (total // (2**30))
    tf = (free // (2**30))
    
    perfree = ((tf / td) * 100)
    
    if perfree < 20:
        errormessage += "\nAvailable disk space is less than 20%"
        
    mem = virtual_memory()
    mem.total 
    
    THRESHOLD = 500 * 1024 * 1024
    
    if mem.available < THRESHOLD:
        errormessage += "\nAvailable memory is less than 500MB"

    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
    except: 
        errormessage += "{} cannot be resolved to {}".format(host_name, host_ip)
    
    print(errormessage)
    
    if len(errormessage) > 0:
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        subject = errormessage
       
        body = "Please check your system and resolve the issue as soon as possible."
    
        message = emails.generate(sender, receiver, subject, body, "")
        emails.send(message)

print("please wait...")
check_health()