#!/bin/bash
# Converts external links to open in new tab in a markdown file
# usage:  ext_links xyz.md
# First backs up target file.
cp $1 $1.bak
sed -i -E 's/(https:\/\/\S+\))/\1{:target="_blank"}/g' $1