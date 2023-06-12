#!/bin/bash
pandoc --extract-media=./converted/ \
  --lua-filter=remove-underlines.lua \
  --lua-filter=remove-blockquotes.lua \
  -s source-docs/section-2.docx -t gfm | \
  sed -e 's/\\</</g' -e 's/\\>/>/g' | \
  sed 's|./converted//||g' \
  > converted/section-2.md 


# Alternative method of removing block-quotes, instead of lua-filter.
#  sed 's/- > /- /' | \
#  sed 's/^\( *\)> /\1/' | \
