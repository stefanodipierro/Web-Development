#!/usr/bin/env python3
import requests
import os

# url is local
url = 'http://localhost/fruits/'
#folder path
path = os.path.expanduser('~') + '/supplier-data/descriptions/'
# this gets a list of the files in the folder
txtList = os.listdir(path)

# in this case the text is already divideed in list of 3 strings objects 
def upload_products(folder):
    txtList = os.listdir(folder)

    for txt in txtList:
        try:
                    productDict = {}
                    opened = open(path + txt, 'r')
                    linesList = opened.readlines()
                    productDict['name'] = linesList[0]
                    productDict['weight'] = int(linesList[1].split()[0])
                    productDict['description'] = linesList[2]
                    productDict['image_name'] = txt.split('.')[0] + '.jpeg'
                    opened.close()
                    r = requests.post(url, data = productDict)
                    print('Product Uploaded')
        except :
            print('Error')
    print('Upload completed')

upload_products(path)
