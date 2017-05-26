#!/bin/bash
cd content/
title=${1:-NewBlog}
cat > $(echo $title | tr ' ' '_').md <<EOF
Title: ${title}
Date: $(date "+%Y-%m-%d %H:%M")
Category: Python
Authors: Ace Fei
Summary: Short version for index and feeds

### This is the content of my blog post.
EOF