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
import re
import datetime

BOT_NAME = 'stalker'

SPIDER_MODULES = ['stalker.spiders']
NEWSPIDER_MODULE = 'stalker.spiders'

CONCURRENT_REQUESTS = 64
CONCURRENT_REQUESTS_PER_DOMAIN = 32

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'stalker (+http://www.stalker.com)'

LOG_LEVEL = log.INFO
LOG_FILE = re.sub(r'[ :\.]', '_', "/usr/local/var/log/stalker_%s.log" % datetime.datetime.now())

ITEM_PIPELINES = {
    'stalker.pipelines.StalkerPipeline': 1000
}

# Setting up django's project full path.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DJANGO_DIR = os.path.dirname(BASE_DIR)
sys.path.insert(0, DJANGO_DIR)

# Setting up django's settings module name.
os.environ['DJANGO_SETTINGS_MODULE'] = 'xgunicorn.settings'

# this is required or else it would say model not ready etc.
import django
django.setup()
