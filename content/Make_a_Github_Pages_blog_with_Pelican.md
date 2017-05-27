Title: Make a Github Pages blog with Pelican
Date: 2017-05-25 10:05
Category: Python
Tags: pelican
Authors: Ace Fei

[TOC]

## Make a Github Pages blog with Pelican:
###  Install dependence
```
sudo yum install -y git
sudo pip install pelican markdown ghp-import BeautifulSoup4
```

###  Create user pages
There are two basic types of GitHub Pages: [User/Organization Pages and Project Pages](https://help.github.com/articles/user-organization-and-project-pages/). 

Generally, most people will select User Pages, and there are two caveat as below:

> You must use the *username.github.io* naming scheme.
> Content from the *master* branch will be used to build and publish your GitHub Pages site.

When User Pages are built, they are available at http(s)://username.github.io.


###  Set up the blog with Pelican
Create a new branch (pelican) for hosting pelican settings on github, please refer to [Publish](#publish) 
```
$ git clone https://github.com/acefei/acefei.github.io
$ cd acefei.github.io/
$ git checkout -b pelican
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

###  [Write first post](http://docs.getpelican.com/en/3.6.3/content.html)
To facilitate blog creation, I write a script for creating the template with md format.
```bash
#!/bin/bash
## save as create_new_blog.sh
cd content/
title=${1:-NewBlog}
cat > $(echo $title | tr ' ' '_').md <<EOF
Title: ${title}
Date: $(date "+%Y-%m-%d %H:%M")
Category: Python
Tags: pelican
Slug: my-super-post
Authors: Ace Fei
Summary: Short version for index and feeds

This is the content of my blog post.
EOF
```

Generate html format and pre-view via http://localhost:8000/
```
make html && make serve&
firefox http://localhost:8000/
# After pre-view 
fg
# Then, Ctrl+C to terminate the process
```
### Publish
If everything is OK, generate the website.         
Currently, all pelican settings that are used to render HTML are on pelican branch.       
As previously mentioned, the static website content should be pulish from master branch.       
So, I need to publish respectively:      
For static website: (on [master branch](https://github.com/acefei/acefei.github.io/tree/master))
```
make github
```     
For pelican settings: (on [pelican branch](https://github.com/acefei/acefei.github.io/tree/pelican))       
```
echo -e "*.pyc\noutput/" >> .gitignore
git add .
git commit -m "commit pelican setting"
git push -u origin pelican
```

### Extension
#### Theme
Download your fevorite [theme](http://pelicanthemes.com/), such as [elegant](http://oncrashreboot.com/elegant-best-pelican-theme-features)
and unpack it (the path named pelican-elegant-1.3) to the path where there is pelicanconf.py.                             
Then, append the following content into pelicanconf.py
```
THEME = "pelican-elegant-1.3"
```
         
> Caveat:            
> Under GFW, we need to find an alternative CDN site to replace googleapis           
> I use [a script](https://raw.githubusercontent.com/acefei/acefei.github.io/pelican/boost_cdn.sh) to do it.

#### Plugin
At first, clone the plugin repo.
```
git clone git://github.com/getpelican/pelican-plugins.git
```
Then, add following contents into pelicanconf.py
```
###### plugin configuration #######
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
SITEMAP = {
'format': 'xml',
'priorities': {
    'articles': 0.5,
    'indexes': 0.5,
    'pages': 0.5
    },
'changefreqs': {
    'articles': 'weekly',
    'indexes': 'daily',
    'pages': 'monthly'
    }
}
```
Ok, plugin install completely.


### Reference
> Blog [`onCrash=Reboot();`](http://oncrashreboot.com) uses Elegant theme. You
can see its configuration files at
[Github](https://github.com/talha131/onCrashReboot) for inspiration. 
