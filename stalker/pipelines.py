# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.contrib.exporter import JsonLinesItemExporter

class JsonLinePipeline(object):

    output_dir = '.'

    def __init__(self):
        self.files = {}
        self.exporter = None
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        if settings['JSON_OUTPUT_DIR']:
            JsonLinePipeline.output_dir = settings['JSON_OUTPUT_DIR']

    def spider_opened(self, spider):
        f = open('/%s/%s_%s_items.json' % (JsonLinePipeline.output_dir, spider.name, time.time()), 'w+b')
        self.files[spider] = f
        self.exporter = JsonLinesItemExporter(f)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        f = self.files.pop(spider)
        f.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return  item
