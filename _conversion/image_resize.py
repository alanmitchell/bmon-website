#!/usr/bin/env python
import os
import sys
import re
from PIL import Image
import yaml

# Set of images to resize: 'All' or 'Selected' (those that appear in the info file)
IMAGE_SET = 'Selected'

FULL_WIDTH = 1052      # Image width in pixels for full-width image.

# the base directory for the images
base_dir = sys.argv[1]

# open the YAML file containing resizing info for this set of images
img_info = yaml.safe_load(open(f'image-{base_dir}.yaml', 'r'))
if img_info is None:
    img_info = {}
print(img_info)
 
source_dir = f'converted/{base_dir}/media'
out_dir = f'../assets/guide/{base_dir}'
for filename in os.listdir(source_dir):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        # get image number
        match = re.search(r"image(\d+)", filename)
        img_num = int(match.group(1))

        if IMAGE_SET.lower() == 'selected' and (img_num not in img_info):
            continue

        print(filename)

        img = Image.open(os.path.join(source_dir, filename))
        width, height = img.size
        aspect_ratio = height/width

        if img_num in img_info:
            new_width = int(FULL_WIDTH * img_info[img_num])
            print(img_num, new_width)
        else:
            new_width = FULL_WIDTH
        new_height = int(new_width * aspect_ratio)

        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        img.save(os.path.join(out_dir, filename), quality=95)
        img.close()
