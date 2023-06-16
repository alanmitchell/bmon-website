#!/usr/bin/env python
"""Script to make a Markdown file with a Table of Contents of
all the User Guide documents.
"""
import re
from pathlib import Path

from slugify import slugify

stop_words = ["a", "an", "the", "and", "but", "or", "on", 
              "in", "with", "to", "of", "for"]

md_files = [
    ('intro', 2),
    ('sensors', 2),
    ('setup-bmon', 2),
    ('use-data', 2)
    ]

fout = open('out/toc.md', 'w')

base_dir = Path('../guide')
for f, max_depth in md_files:

    fin = open(base_dir / f'{f}.md')
    while True:

        lin = fin.readline()

        if lin == '':
            break

        if lin.startswith('title:'):
            doc_title = lin.split(':')[1].strip()
            print(f'\n### {doc_title}', file=fout)

        match = re.match(r'^(#+)(.*)', lin)
        if match:
            depth = len(match.group(1))
            if depth <= max_depth:
                leader_space = ' ' * (depth - 2) * 4
                title = match.group(2).strip().replace('*', '')
                # read the next line to get the link target
                lin_target = fin.readline()
                search = re.search(r'{: #(.+)}', lin_target)
                target = search.group(1) if search else ''
                print(f'{leader_space} - [{title}]({f}#{target})', file=fout)

        if '***Video:' in lin:
            caption_search = re.search(':\*{3}(.+)', lin)
            caption = caption_search.group(1).strip().replace('*', '')
            # read the next line to retrieve the target
            lin_target = fin.readline()
            search = re.search(r'{: #(.+)}', lin_target)
            target = search.group(1) if search else ''
            print(f'{leader_space}    - **Video:** [{caption}]({f}#{target})', file=fout)

fout.close()

