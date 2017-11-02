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
LINKS = (
        ('CSDN (legacy blog)', 'blog.csdn.com/ace_fei'),
        )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True

# SEO
SITE_DESCRIPTION = u'My name is acefei/ace_fei. This is my personal blog.'

###### elegant theme configuration #######
THEME = "pelican-themes/pelican-elegant"
# About Me
LANDING_PAGE_ABOUT = {
        'title': 'WHEN YOU AUTOMATE, YOU ACCELERATE',
        'details': """
        <div>
            <h1>欢迎来到Acefei的博客!</h1>
            <p>写博客目的:</p>
            <p>    ——未经你思考的知识是不属于你的。</p>
            <p>    ——要拒绝思维懒惰, 要勇于发现问题，勤于分析问题，善于解决问题。</p>
            <p>    ——好记忆不如烂笔头，定期梳理自己的掌握的技术，并记录下来。</p>
            <p>题外话：由于<a href='http://blog.csdn.net/csdnproduct/article/details/70145129'>特殊原因</a>(呵呵！看评论)，我的CSDN博客(<a href='http://blog.csdn.net/ace_fei'>ace_fei</a>)已经停止更新！</p>
            <p>
                <a href="https://gitter.im/acefei-github-io/Lobby?utm_source=badge&amp;utm_medium=badge&amp;utm_campaign=pr-badge&amp;utm_content=body_badge"><img src="https://camo.githubusercontent.com/afba4da91df6731efa687d0457c6fdf98f346f36/68747470733a2f2f6261646765732e6769747465722e696d2f6163656665692d6769746875622d696f2f4c6f6262792e737667" alt="Gitter" data-canonical-src="https://badges.gitter.im/acefei-github-io/Lobby.svg" style="max-width:100%;"></a>
            </p>

            <hr class="eye-protector-processed" style="transition: background-color 0.3s ease; border-color: rgba(0, 0, 0, 0.35); color: rgb(0, 0, 0); background-color: rgb(193, 230, 198);">
            <h2>博文分类</h2>
            <ul>
            <li>DevOps：持续交付、自动化 </li>
            <li>Development：编程语言 </li>
            <li>Misc：意趣、闲思、杂七杂八</li>
            </ul>
            <p>翻阅博客：<a href="/categories.html">文章归档</a> <a href="/tags.html">话题标签</a></p>
        </div>
        """
        }

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives','404'))
# Relative path with content/
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

# you can find the icons in http://fontawesome.io/icons/#brand
SOCIAL = (
        ('github', 'https://github.com/acefei'),
        ('linkedin', 'https://www.linkedin.com/in/fei-su-2b6b10104'),
          )


###### plugin configuration #######
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap',
           'extract_toc',
           'tipue_search',
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
