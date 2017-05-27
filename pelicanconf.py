#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#################### For the details, please refer to http://docs.getpelican.com/en/stable/settings.html  #####################

AUTHOR = u'acefei'
SITENAME = u"""<span style="color:black;">Acefei</span> <span style="color:darkblue;">'s</span> <span style="color:#AA1032;">One Piece</span>"""
SITEURL = ''

PATH = 'content'
# set the page in navigation bar
PAGE_PATHS = ['pages']

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Friend link
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)



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
USE_SHORTCUT_ICONS = True
DEFAULT_PAGINATION = 10
RECENT_ARTICLES_COUNT = 10

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'Stay in Touch'

# Social widget
SOCIAL = (
        ('CSDN (legacy blog)', 'http://blog.csdn.net/ace_fei'),
        ('GitHub', 'https://github.com/acefei'),
        ('Wechat', 'acefei'),
        ('Email', 'mailto:acefei@163.com'),
          )


###### plugin configuration #######
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap',
           'extract_toc',
           'tipue_search',
           #'related_posts',
           #'code_include',
           #'summary',
          ]
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

# For extract_toc plugin
# For markdown extension settings, refer to http://pythonhosted.org/Markdown/extensions/index.html
MARKDOWN = {
        'extension_configs': {
            'markdown.extensions.codehilite': {'css_class': 'highlight'},
            'markdown.extensions.extra': {},
            'markdown.extensions.meta': {},
            # When set permalink to True the paragraph symbol (¶ or “&para;”) is used as the link text.
            'markdown.extensions.toc': {'permalink': True},
            },
        'output_format': 'html5',
        }
