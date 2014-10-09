#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'webmaster'
SITENAME = u'Website'
SITEURL = u'https://www.example.net'
TIMEZONE = u'Europe/Zurich'
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%a %d. %B %Y'

# Page path
PAGE_PATHS = ['pages']

# Menu
MENUITEMS = (   ('Page1', 'page1.html', None),
                ('Page2', '#', [
                    ('Page2.1', 'page2-1.html'),
                    ('Page2.2', 'page2-2.html'),
                ]),
                ('Page3', 'page3.html', None),)

# Sole author and don't use categories ... disable these features
#AUTHOR_SAVE_AS = ''
#AUTHORS_SAVE_AS = ''
#CATEGORY_SAVE_AS = ''
#CATEGORIES_SAVE_AS = ''

# don't show categories and pages in the menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_RSS = None
FEED_ALL_ATOM = None
FEED_RSS = 'feeds/rss.xml'
FEED_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL settings
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
ARTICLE_URL = '{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tag-{slug}.html'
TAG_SAVE_AS = 'tag-{slug}.html'
TAGS_URL = 'tags.html'
TAGS_SAVE_AS = 'tags.html'
ARCHIVES_URL = 'archives.html'
ARCHIVES_SAVE_AS = 'archives.html'

# Contact
EMAIL_ADDR = 'webmaster@example.net'

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = []

# Theme
THEME = 'theme'
STATIC_PATHS = ['images', 'docs', 'extra/robots.txt', 'extra/favicon.ico']
PATH_METADATA = 'pages/(?P<path>.*)\..*'
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Licence
LICENCE_NAME = 'BY-NC-SA'
LICENCE_URL = 'http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US'
LICENCE_URL_IMG = 'http://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png'

# Tag cloud
TAG_CLOUD_STEPS = 4
