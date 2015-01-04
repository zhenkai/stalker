# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy

class ProductItem(scrapy.Item):
    headline = scrapy.Field()
    img = scrapy.Field()
    desc = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    vendor = scrapy.Field()
    oos = scrapy.Field()
    timestamp = scrapy.Field()
