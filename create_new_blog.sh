#!/bin/bash
read -p "Article Title: " r_title
read -p "Category: [Development/DevOps/Misc]" r_category
read -p "Tags: (separated by comma) " r_tags
title=${r_title:-NewBlog}
category=${r_category:-Development}
tags=${r_tags:-na}

cd content/
cat > $(echo $title | tr ' ' '_').md <<EOF
Title: ${title}
Date: $(date "+%Y-%m-%d %H:%M")
Category: ${category}
Tags: ${tags}
Authors: Ace Fei


[TOC]

EOF

echo "Now you can edit new article: content/$(echo $title | tr ' ' '_').md"
