#!/usr/bin/env python3

import requests
import sys, os


def upload_images(folder):
    for img in os.listdir(folder):
        if img.endswith('.jpeg'):
            try:
                with open(folder + img, 'rb') as opened:
                    r = requests.post(url, files = {'file': opened})
                    print('Uploaded')
            except:
                print('Error')

if __name__ ==' __main__':
    url = 'http://localhost/upload/'
    #get home path
    home = os.path.expanduser("~")
    #pass folder name from command line
    upload_images(home + '/supplier-data/images/')
