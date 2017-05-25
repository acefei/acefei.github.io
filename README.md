[使用Pelican + Github Pages搭建个人博客](http://www.wengweitao.com/shi-yong-pelican-github-pagesda-jian-ge-ren-bo-ke.html)


### Make a Github Pages blog with Pelican:
##### 1. install dependence
```
sudo yum install -y git
sudo pip install pelican markdown
```
##### 2. Set up the blog with Pelican
```
$ git clone https://github.com/acefei/acefei.github.io
$ cd acefei.github.io/
$ pelican-quickstart
Welcome to pelican-quickstart v3.7.1.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.


> Where do you want to create your new web site? [.]
> What will be the title of this web site? Acefei's Blog
> Who will be the author of this web site? acefei
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n)
> What is your URL prefix? (see above example; no trailing slash) https://acefei.github.io
> Do you want to enable article pagination? (Y/n) n
> What is your time zone? [Europe/Paris] Asia/Shanghai
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
> Do you want to upload your website using FTP? (y/N)
> Do you want to upload your website using SSH? (y/N)
> Do you want to upload your website using Dropbox? (y/N)
> Do you want to upload your website using S3? (y/N)
> Do you want to upload your website using Rackspace Cloud Files? (y/N)
> Do you want to upload your website using GitHub Pages? (y/N) Y
> Is this your personal page (username.github.io)? (y/N) Y

```

#####  3. [Write first post](http://docs.getpelican.com/en/3.6.3/content.html)
this script will create a template with md format
```
$ cat create_new_blog.sh
#!/bin/bash
cd content/
title=${1:-NewBlog}
cat > $(echo $title | tr ' ' '_').md <<EOF
Title: ${title}
Date: $(date "+%Y-%m-%d %H:%M")
Modified: $(date "+%Y-%m-%d %H:%M")
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Authors: Ace Fei
Summary: Short version for index and feeds

This is the content of my super blog post.
EOF
```
generate html format and pre-view on http://localhost:8000/
```
$ make html && make serve&
$ firefox http://localhost:8000/
# After pre-view 
$ fg
# Then, Ctrl+C to terminate the process
```
##### 4. Publish
If everything is OK, generate the website
```
$ make publish
$ cd output
$ git add .
$ git commit -m "post."
$ git push -u origin master
$ cd ..
$ echo '*.pyc' >> .gitignore #don't need pyc files
$ git add .
$ git commit -m "commit."
$ git push -u origin master
```


### Finally
Everything can be customized in Pelican. To start with, you can choose from [a set of themes](http://pelicanthemes.com/). There are also [a set of plug-ins](https://github.com/getpelican/pelican-plugins) that help you add various functions to your site. Of course, you can write your own, or customize existing plugins and themes.
