#!/usr/bin/env python3

import os
from PIL import Image

CNVRTD = "/home/scottdavis/Documents/WorkInProgress/module1images/converted"
SRC = "/home/scottdavis/Documents/WorkInProgress/module1images"

def resize_image(the_file):
    srcstr = SRC + "/" + the_file
    dststr = CNVRTD + "/" + the_file
    size = (128, 128)

    try:
        with Image.open(srcstr) as im:
            im.thumbnail(size)
            im.convert("L").rotate(270).save(dststr, "JPEG", quality=100, optimize=True)
    except Exception as e:
        print(e)

def main():
    for filename in os.listdir(SRC):
        srcstr = SRC + "/" + filename
        if os.path.isfile(srcstr):
            resize_image(filename)
            

main()


    
