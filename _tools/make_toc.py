#!/usr/bin/env python
"""Script to make a Markdown file with a Table of Contents of
all the User Guide documents.
"""
import re
from pathlib import Path

md_files = [
    'intro',
    'sensors',
    'setup-bmon',
    'use-data'
    ]

fout = open('toc.md', 'w')

base_dir = Path('../guide')
for f in md_files:

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
            leader_space = ' ' * (len(match.group(1)) - 2) * 4
            title = match.group(2).strip().replace('*', '')
            # read the next line to get the link target
            lin_target = fin.readline()
            match = re.match(r'{: #(.+)}', '{: #creating-monitoring-plan}')
            target = match.group(1) if match else ''
            print(f'{leader_space} - [{title}]({f}#{target})', file=fout)
