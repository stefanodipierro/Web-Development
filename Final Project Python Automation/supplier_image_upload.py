#!/usr/bin/env python3

import requests
import sys, os

url = 'http://localhost/upload/'
#get home path
folder = os.path.expanduser("~") + '/supplier-data/images/'
#pass folder name from command line
def upload_images(folder):
    for img in os.listdir(folder):
        if img.endswith('.jpeg'):
            try:
                with open(folder + img, 'rb') as opened:
                    r = requests.post(url, files = {'file': opened})
                    print('Uploaded')
            except:
                print('Error')


upload_images(folder)
