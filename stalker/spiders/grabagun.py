# -*- coding: utf-8 -*-
import locale
import mmh3
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from urltools import normalize
from stalker.items import ProductItem
from django.utils import timezone

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

class GrabagunSpider(CrawlSpider):
    name = "grabagun.com"
    allowed_domains = ["grabagun.com"]
    start_urls = (
        'http://www.grabagun.com/',
    )

    rules = (
        Rule(LinkExtractor(allow=(r"http://grabagun.com/(firearms|sale-items|accessories|magazines|scopes-optics|holsters|tactical-gear|gun-parts-for-sale)",),
                           restrict_xpaths='//div[@class="nav-container"]//a[span]',
                           process_value=lambda url: "%s?limit=100" % url), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//a[@class="next i-next"]'), callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        for sel in response.xpath('//ul[@class="products-grid"]/li[starts-with(@class, "item")]'):
            yield self._parse_single_item(sel)


    def _parse_single_item(self, sel):
        item = ProductItem()

        item['url'] = normalize(sel.xpath('a[@class="product-image"]/@href').extract()[0])
        item['pid'] = mmh3.hash(item['url'])
        item['img'] = sel.xpath('a[@class="product-image"]/img[@alt]/@src').extract()[0]
        oos = sel.xpath('.//p[@class="availability out-of-stock"]/span/text()').extract()
        if "Out of stock" in oos:
            item['oos'] = True
        else:
            item['oos'] = False

        has_sale = sel.xpath('.//div[starts-with(@class,"price-box")]//a/text()').re("[Cc]lick for [pP]rice")
        if len(has_sale) > 0:
            sale_price = sel.xpath('.//div[starts-with(@class,"price-box")]//script/text()').re(r"\$((\d+,)*\d+\.\d+)")
            item['price'] = locale.atof(sale_price[0])
        else:
            regular_price = sel.xpath('.//div[starts-with(@class,"price-box")]/span/span[@class="price"]/text()').re(r"((\d+,)*\d+\.\d+)")
            item['price'] = locale.atof(regular_price[0])

        item['headline'] = sel.xpath('.//h2[@class="product-name"]/a/text()').extract()[0]
        item['vendor'] = self.name
        item['last_modified'] = timezone.now()

        return item
