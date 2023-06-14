#!/bin/bash
# First CLI parameter is base name of docx file to convert (without .docx), 
# second parameter is base name of (without .md) of output Markdown file.
echo -e "---\nlayout: single\ntitle: "BMON and Building Monitoring"\ntoc: true\n---\n" > converted/$2.md
pandoc --extract-media=./converted/$2/ \
  --lua-filter=remove-underlines.lua \
  --lua-filter=remove-blockquotes.lua \
  -s source-docs/$1.docx -t gfm | \
  sed 's/”/"/g' | \
  sed -e 's/\\</</g' -e 's/\\>/>/g' | \
  sed "s|./converted/$2//media|{{ site.baseurl }}/assets/guide/$2|g" | \
  sed -e 's|<summary>\*\*|<summary>|g' -e 's|\*\*</summary>|</summary>|g' | \
  python convert.py \
  >> converted/$2.md 

# Alternative method of removing block-quotes, instead of lua-filter.
#  sed 's/- > /- /' | \
#  sed 's/^\( *\)> /\1/' | \

