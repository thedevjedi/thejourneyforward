#!/usr/bin/env python
import subprocess
from concurrent import futures
import os


def copy_file(file):
    print("copying file: {}".format(file))



def main():
    src = "/home/scottdavis/Documents"
    dest = "/data/prod_backup/"
    executor = futures.ProcessPoolExecutor()
    for root, dirs, files in os.walk(src):
        #for d in dirs:
        #    print(os.path.join(root,d))
        for f in files:
            print(os.path.join(root,f))
        
            
            #executor.submit(copy_file, f)
    print("waiting")
    executor.shutdown()
    return 0

    
main()
    
        