#!/usr/bin/env python
"""Script to make a Markdown file with a Table of Contents of
all the User Guide documents.
"""
import re
from pathlib import Path
import os

from slugify import slugify

script_path = os.path.abspath(__file__)  # Full path of the script
script_dir = os.path.dirname(script_path)

stop_words = ["a", "an", "the", "and", "but", "or", "on", 
              "in", "with", "to", "of", "for"]

md_files = [
    ('intro', 2),
    ('sensors', 2),
    ('setup-bmon', 2),
    ('use-data', 2)
    ]

fout = open(f'{script_dir}/out/toc.md', 'w')

base_dir = Path(f'{script_dir}/../guide')
for f, max_depth in md_files:

    print(f)
    leader_space = ''
    fin = open(base_dir / f'{f}.md')
    while True:

        lin = fin.readline()

        if lin == '':
            break
        lin = lin.strip()

        if lin.startswith('title:'):
            doc_title = lin.split(':')[1].strip()
            print(f'\n### {doc_title}', file=fout)

        match = re.match(r'^(#+)(.*)', lin)
        if match:
            depth = len(match.group(1))
            if depth <= max_depth:
                leader_space = ' ' * (depth - 2) * 2
                title = match.group(2).strip().replace('*', '')
                # read the next line to get the link target
                lin_target = fin.readline()
                search = re.search(r'{: #(.+)}', lin_target)
                target = search.group(1) if search else ''
                print(f'{leader_space}- [{title}]({f}#{target})', file=fout)

        if '***video:' in lin.lower():
            caption_search = re.search(':\*{3}(.+)', lin)
            caption = caption_search.group(1).strip().replace('*', '')
            # read the next line to retrieve the target
            lin_target = fin.readline()
            search = re.search(r'{: #(.+)}', lin_target)
            target = search.group(1) if search else ''
            print(f'{leader_space}  - **Video:** [{caption}]({f}#{target})', file=fout)

        if '<br>{: #image' in lin:
            if '*' in lin:
                # if this line doesn't have the full caption, read subsequent lines and add them
                while not lin.endswith('*'):
                    lin += ' ' + fin.readline().strip()
                caption_search = re.search('\*(.+)\*', lin)
                if caption_search:
                    caption = caption_search.group(1).strip()         
                    search = re.search(r'{: #(.+)}', lin)
                    target = search.group(1) if search else ''
                    print(f'{leader_space}  - **Figure:** [{caption}]({f}#{target})', file=fout)
                else:
                    print(lin.strip())

fout.close()

