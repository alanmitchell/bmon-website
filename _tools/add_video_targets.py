#!/usr/bin/env python
"""Script to add anchor targets to every Video.
"""
from pathlib import Path
import re

from slugify import slugify

stop_words = ["a", "an", "the", "and", "but", "or", "on", 
              "in", "with", "to", "of", "for"]

md_files = [
    #'intro',
    #'sensors',
    #'setup-bmon',
    'use-data',
    ]

base_dir = Path('../guide')

for f in md_files:

    fout = open(f'out/{f}.md', 'w')

    for lin in open(base_dir / f'{f}.md'):
        lin = lin.strip()
        print(lin, file=fout)
        if '***Video:' in lin:
            caption_search = re.search(':\*{3}(.+)', lin)
            caption = caption_search.group(1).strip().replace('*', '')
            slug = slugify(
                caption, 
                stopwords=stop_words,
                )
            slug = 'video-' + '-'.join(slug.split('-')[:3])
            print('{: #' + slug +  '}', file=fout)

    fout.close()
