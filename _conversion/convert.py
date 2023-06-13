#!/usr/bin/env python
"""Command line tool to due some Markdown conversions.
"""

import sys
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

    else:
        # Line not needing action
        print(line)

