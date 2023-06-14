#!/usr/bin/env python
"""Command line tool to due some Markdown conversions.
"""

import sys
import re
from slugify import slugify

stop_words = ["a", "an", "the", "and", "but", "or", "on", 
              "in", "with", "to", "of", "for"]

out_lines = []
for line in sys.stdin:
    line = line.rstrip()
    if line.startswith('#'):
        # Add a link target to section headings
        print(line)
        # Section heading. Add a target.
        title = ' '.join(line.strip().split()[1:])
        slug = slugify(
            title, 
            stopwords=stop_words,
            )
        # limit the slug to 3 words
        slug = '-'.join(slug.split('-')[:3])
        print('{: #' + slug +  '}')

    elif '![](' in line:
        # Add a link target and Captions to images
        print(line)
        img_file = line.split('/')[-1]
        img_base = img_file.split('.')[0]
        print('<br>{: #' + img_base +  '}*Caption*')

    elif "https://vimeo.com/" in line:
        print(line)
        match = re.search(r"vimeo\.com/(\d+)", line)
        if match:
            print('*Caption*')
            print('{% include video id="' + match.group(1) + '" provider="vimeo" %}')

    else:
        # Line not needing action
        print(line)

