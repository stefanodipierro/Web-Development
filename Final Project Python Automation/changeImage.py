#!/usr/bin/env python3

import os
import sys
from PIL import Image

# specify the path
folder = os.path.expanduser('~') + '/supplier-data/images/'

# open an image with PIL, resize, convert and save.
for img in os.listdir(folder):

    try:
        new_im = Image.open(folder + img).resize((600,400)).convert('RGB')
        filename = img.split('.')[0] + '.jpeg'
        new_im.save(folder + filename,'JPEG')
        new_im.close()
        print('OK')
    except:
        print('Error') # Not an image
print('Upload Completed')
