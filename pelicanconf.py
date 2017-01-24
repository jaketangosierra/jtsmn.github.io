#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os.path, time

AUTHOR = 'Jacob Thebault-Spieker'
SITENAME = 'Jacob Thebault-Spieker'
# SITEURL = 'http://localhost:8000'
SITEURL = 'http://jacob.thebault-spieker.com'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

THEME='jts'
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'stylesheet.css'
PROFILE_FILE = 'profile_pic.jpg'

PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'
INDEX_URL = '/'
ARTICLE_URL = 'ephemera/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'ephemera/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
DIRECT_TEMPLATES = (('ephemera', 'tags', 'categories', 'archives'))
PAGINATED_DIRECT_TEMPLATES = (('index', 'ephemera'))
TYPOGRFIY = True
STATIC_PATHS = ['files', 'files/CNAME', 'files/robots.txt']
EXTRA_PATH_METADATA = {'files/CNAME': {'path': 'CNAME'}, 'files/robots.txt': {'path': 'robots.txt'}}

HTML_PATH='curriculum-vitae.html'
PDF_OUTPUT_NAME='cv'

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['pandoc_reader', 'pelican-weasyprint']
PANDOC_ARGS = [
  '--smart',
  '--bibliography=/Users/theba004/Dropbox/sites/professional/content/publications.bib',
  '--csl=/Users/theba004/Dropbox/sites/professional/csl/acm-sigchi-proceedings.csl'
]
PANDOC_EXTENSIONS = [
  '+mmd_link_attributes',
  '+definition_lists',
]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SIDEBAR = (('Home', '/', 'home'),
            ('About', '/about.html', 'about'),
            ('Papers', '/papers.html', 'papers'),
            ('Ephemera', '/ephemera.html', 'ephemera'))
