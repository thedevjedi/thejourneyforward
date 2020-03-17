#!/usr/bin/env python3

import os
from PIL import Image

DEST = "~/supplier-data/images"
SRC = "~/supplier-data/images"

DEST = "/home/scottdavis/Documents/WorkInProgress/module1images/converted"
SRC = "/home/scottdavis/Documents/WorkInProgress/module1images"


def resize_image(the_file):
    srcstr = SRC + "/" + the_file
    dststr = SRC + "/" + the_file + ".jpeg"
    size = (600, 400)

    try:
        with Image.open(srcstr) as im:
            im.convert("L").resize(size).save(dststr, "JPEG", quality=100, optimize=True)
    except Exception as e:
        print(e)

def main():
    for filename in os.listdir(SRC):
        srcstr = SRC + "/" + filename
        if os.path.isfile(srcstr):
            resize_image(filename)
            

main()
