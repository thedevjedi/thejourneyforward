#!/usr/bin/env python3
#Import libraries

import re
import csv
import subprocess


def write_mycsvDictfile(filename,thedict,error_info):
    
    sorted(thedict.values())
    with open(filename, "w") as file:
        writer = csv.writer(file)
        if error_info == "ERROR":
            writer.writerow(["Error","Count"])
            for key, value in sorted (thedict.items()):
                writer.writerow([key, value])
        else:
            writer.writerow(["Username","INFO","ERROR"])
            for key, value in sorted (thedict.items()):
                writer.writerow([key, value, "0"])

    
    return "File write of dicts OK."


def main(): 
    
    filename = "/home/scottdavis/eclipse-workspace/mytest/testlg.log"
    #filename = "/home/student-00-1982425570a3/syslog.log"
    userstats = {}
    errordict = {}
    usernamefound = r"\((\w+\))"
    
    with open(filename) as file:
        for line in file:
            result = re.search(usernamefound, line)
            usr_name_clean = result[0].replace('(', '')
            usr_name_clean = usr_name_clean.replace(')', '')
            
            foo = userstats.get(usr_name_clean, "nf")
            
            if foo == "nf":
                userstats[usr_name_clean] = 1
            else:
                userstats[usr_name_clean] += 1
                
            foundinfo = line.find("INFO:")
                      
            if foundinfo >= 0:
                foo = ""    
            else:
                error_msg = line[line.index("ERROR:")+7:line.index(result[0])]

                foo2 = errordict.get(error_msg.strip(), "nf")
            
                if foo2 == "nf":
                    errordict[error_msg.strip()] = 1
                else:
                    errordict[error_msg.strip()] += 1                                            
            usr_name_clean = ""
            result = ""
            
    filename_csv = "/home/scottdavis/eclipse-workspace/mytest/stats.csv"
    write_mycsvDictfile(filename_csv,userstats,"")
    filename_csv2 = "/home/scottdavis/eclipse-workspace/mytest/errors.csv"
    write_mycsvDictfile(filename_csv2,errordict,"ERROR")
    print(userstats)
    print(errordict)
            
    
        
        
main() 
#subprocess.Popen("/home/scottdavis/eclipse-workspace/mytest/anotherone.py somearg", shell=True)
        
