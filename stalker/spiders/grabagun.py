# -*- coding: utf-8 -*-
from django.utils import timezone
import mmh3
from scrapy import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from urltools import normalize
from stalker.items import ProductItem


class GrabagunSpider(CrawlSpider):
    name = "grabagun.com"
    allowed_domains = ["grabagun.com"]
    start_urls = (
        'http://www.grabagun.com/',
    )

    rules = (
        Rule(LinkExtractor(allow=(r"http://grabagun.com/[firearms|accessories|magazines|scopes-optics|holsters|tactical-gear|gun-parts-for-sale]",),
                           restrict_xpaths="//a[span]")),
        Rule(LinkExtractor(restrict_xpaths='//a[@class="next i-next"]')),
        Rule(LinkExtractor(allow=(r"http://grabagun.com/.+\.html",), restrict_xpaths='//ol[@class="products-list"/li[@class="item"', callback='parse_item'))
    )

    def parse_item(self, response):
        url = normalize(response.url)
        pid = mmh3.hash(url)
        sel = Selector(response)
        img = sel.xpath('//meta[@property="og:image"]/@content').extract()
        in_stock = sel.xpath('//p[@class="availability in-stock"]/*/text()').extract()
        if "In stock" == in_stock:
            price = sel.xpath('//div[@class="price-box"]/span/span[@class="price"]/text()').extract()
        else:
            price = -999
        headline = sel.xpath('//meta[@property="og:title"]/@content').extract()
        desc = sel.xpath('//meta[@name="description]/@content').extract()
        vendor = self.name
        last_modified = timezone.now()

        return ProductItem(pid=pid, url=url, img=img, headline=headline, desc=desc, vendor=vendor, price=price, last_modified=last_modified)

