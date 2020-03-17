#!/usr/bin/env python3

import requests
import os

SRC = "~/supplier-data/images"

def upload_image(full_path_to_file,url_str):
    with open(full_path_to_file,'rb') as opened:
        r = requests.post(url_str, files={'file':opened})
    return r

def create_body_para():
    
    url_to_upload_to = "0.0.0.0/upload"
    
    for filename in os.listdir(SRC):
        srcstr = SRC + "/" + filename
        if os.path.isfile(srcstr):
            upload_image(filename,url_to_upload_to)
            

create_body_para()