#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Laura Santamaria'
SITETITLE = 'Yet Another Blog'
SITENAME = 'Yet Another Blog'
SITESUBTITLE = 'A Dev Advocate walks into a bar...'
SITEDESCRIPTION = 'A Dev Advocate walks into a bar...'
SITEURL = 'http://localhost:8000'
SITESRC = 'https://github.com/nimbinatus/nimbinatus.github.io'
SITELOGO = SITEURL + '/static/avatar.png'
FAVICON = SITEURL + '/static/favicon.ico'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Biography
BIO = "Developer Advocate @Pulumi"
PROFILE_IMAGE = 'avatar.png'

# Social widget
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/lauraasantamaria'),
    ('twitter', 'https://twitter.com/nimbinatus'),
    ('github', 'https://github.com/nimbinatus')
)

DEFAULT_PAGINATION = 10

DEFAULT_METADATA = {
    'status': 'draft',
}

# URL settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
# DRAFT_URL = '{slug}.html'
# DRAFT_SAVE_AS = 'drafts/{slug}.html'

# Theme
THEME = 'theme/flex'

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['neighbors', 'post_stats']

# static files
STATIC_PATHS = [
    'static'
]

JINJA_ENVIRONMENT = {
    'extensions': [
        'jinja2.ext.do'
    ]
}

COPYRIGHT_YEAR = 2022
COPYRIGHT_NAME = 'Laura A Santamaria'

MAIN_MENU = True

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

LINKS = (('Speaking', 'https://speaking.nimbinatus.com'),
         ('Archives', '/archives.html'),)
