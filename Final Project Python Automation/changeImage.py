#!/usr/bin/env python3

import os, sys
from PIL import Image

def convert_images(folder):
        for img in os.listdir(folder):

            try:
                new_im = Image.open(folder + img).resize((600,400)).convert('RGB')
                filename = img.split('.')[0]
                new_im.save(folder + filename,'jpeg')
                im.close()
                print('OK')
            except:
                print('Error')


if __name__ ==' __main__':
    #get home path
    home = os.path.expanduser("~")
    #pass folder name from command line
    convert_images(home + '/supplier-data/images/')
