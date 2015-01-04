# -*- coding: utf-8 -*-

# Scrapy settings for stalker project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
from scrapy import log

BOT_NAME = 'stalker'

SPIDER_MODULES = ['stalker.spiders']
NEWSPIDER_MODULE = 'stalker.spiders'

CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 8

LOG_LEVEL = log.INFO

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'stalker (+http://www.stalker.com)'

ITEM_PIPELINES = {
    'stalker.pipelines.JsonLinePipeline': 1000
}