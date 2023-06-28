#!/usr/bin/env python
"""Script to replace italicized figure captions with <figcaption> HTML
tagged captions.
"""
import re
from pathlib import Path

md_files = [
#    'intro',
    'sensors',
#    'setup-bmon',
#    'use-data',
    ]

base_dir = Path('../guide')

for f in md_files:
    print(f)

    with open(f'out/{f}.md', 'w') as fout:

        fin = open(base_dir / f'{f}.md')
        while True:

            lin = fin.readline()

            if lin == '':
                break

            lin = lin.rstrip()

            if '<br>{: #image' in lin:
                if '*' in lin:
                    # if this line doesn't have the full caption, read subsequent lines and add them
                    while not lin.endswith('*'):
                        lin += ' ' + fin.readline().strip()
                    print(lin + "{: .small_text}", file=fout)
                    
                else:
                    print(lin, file=fout)

            else:
                print(lin, file=fout)
