# -*- coding: utf-8 -*-

# Scrapy settings for stalker project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
from scrapy import log
import sys
import os

BOT_NAME = 'stalker'

SPIDER_MODULES = ['stalker.spiders']
NEWSPIDER_MODULE = 'stalker.spiders'

CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 8

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'stalker (+http://www.stalker.com)'

ITEM_PIPELINES = {
    'stalker.pipelines.StalkerPipeline': 1000
}

# Setting up django's project full path.
sys.path.insert(0, '/Users/zhenkai/Develop/site/xgunicorn-site/xgunicorn')

# Setting up django's settings module name.
# This module is located at /home/rolando/projects/myweb/myweb/settings.py.
os.environ['DJANGO_SETTINGS_MODULE'] = 'xgunicorn.settings'

import django
django.setup()