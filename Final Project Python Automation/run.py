#!/usr/bin/env python3
import requests
import os

path = os.path.expanduser('~') + '/supplier-data/descriptions/'
txtList = os.listdir(path)
url = 'http://localhost/upload/'

def upload_products(folder):
    txtList = os.listdir(folder)

    for txt in txtList:
        try:
                    productDict = {}
                    opened = open(path + txt, 'r')
                    linesList = opened.readlines()
                    productDict['name'] = linesList[0]
                    productDict['weight'] = int(linesList[1].strip('lbs'))
                    productDict['description'] = linesList[2]
                    productDict['image_name'] = txt.strip('.txt') + 'jpeg'
                    opened.close()
                    r = requests.post(url, data = productDict)
                    print('Product Uploaded')
        except :
            print('Error')
    print('Upload completed')

if __name__ == '__main__':
    # files path
    path = os.path.expanduser('~') + '/supplier-data/descriptions/'

    # web service url
    url = 'http://localhost/fruits/'
    # run the script
    upload_products(path)
