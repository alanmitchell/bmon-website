#!/usr/bin/env python
import os
import sys
import re
from PIL import Image
import yaml

# the base directory for the images
base_dir = sys.argv[1]

def resize_images(image_directory, new_width, new_height):
    for filename in os.listdir(image_directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img = Image.open(os.path.join(image_directory, filename))
            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save(os.path.join(image_directory, filename))

#resize_images('/path/to/your/images', 800, 600)

# open the YAML file containing resizing info for this set of images
img_info = yaml.safe_load(open(f'image-{base_dir}.yaml', 'r'))
print(img_info)
 
source_dir = f'converted/{base_dir}/media'
out_dir = f'../assets/guide/{base_dir}'
for filename in os.listdir(source_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        print(filename)
        # get image number
        match = re.search(r"image(\d+)", filename)
        img_num = int(match.group(1))

        img = Image.open(os.path.join(source_dir, filename))
        width, height = img.size
        aspect_ratio = height/width

        if img_num in img_info:
            new_width = int(790 * img_info[img_num])
            print(img_num, new_width)
        else:
            new_width = 790
        new_height = int(new_width * aspect_ratio)

        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        img.save(os.path.join(out_dir, filename))
