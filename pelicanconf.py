#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'acefei'
SITENAME = u"""<span style="color:black;">Acefei</span> <span style="color:darkblue;">'s</span> <span style="color:#AA1032;">One Piece</span>"""
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
        ('CSDN (legacy blog)', 'http://blog.csdn.net/ace_fei'),
        ('GitHub', 'https://github.com/acefei'),
        ('Wechat', 'acefei'),
        ('Email', 'mailto:acefei@163.com'),
          )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True

# SEO
SITE_DESCRIPTION = u'My name is acefei/ace_fei. This is my personal blog.'

#Disqus
DISQUS_SITENAME = "ace"

###### elegant theme configuration #######
THEME = "theme/pelican-elegant-1.3"
# About Me
LANDING_PAGE_ABOUT = {
        'title': 'WHEN YOU AUTOMATE, YOU ACCELERATE',
        'details': """
        <div><p>As a geek, I always like to bring fresh and challenging work.</p></div>
        """
        }

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''


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