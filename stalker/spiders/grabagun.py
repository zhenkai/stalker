# -*- coding: utf-8 -*-
import locale
from scrapy import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from urltools import normalize
from stalker.items import ProductItem

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

class GrabagunSpider(CrawlSpider):
    name = "grabagun.com"
    allowed_domains = ["grabagun.com"]
    start_urls = (
        'http://www.grabagun.com/',
    )

    rules = (
        #Rule(LinkExtractor(allow=(r"http://grabagun.com/(firearms|sale-items|accessories|magazines|scopes-optics|holsters|tactical-gear|gun-parts-for-sale)",),
        Rule(LinkExtractor(allow=(r"http://grabagun.com/sale-items",),
                           restrict_xpaths='//div[@class="nav-container"]//a[span]')),
        Rule(LinkExtractor(restrict_xpaths='//a[@class="next i-next"]')),
        Rule(LinkExtractor(allow=(r".*html",), restrict_xpaths='//h2[@class="product-name"]/a'), callback='parse_item')
    )

    def parse_item(self, response):
        item = ProductItem()
        item['url'] = normalize(response.url)
        sel = Selector(response)
        item['img'] = sel.xpath('//meta[@property="og:image"]/@content').extract()[0]
        in_stock = sel.xpath('//p[@class="availability in-stock"]/span/text()').extract()
        if "In stock" in in_stock:
            item['oos'] = False
        else:
            item['oos'] = True
        item['price'] = locale.atof(sel.xpath('//div[@class="price-block"]/div[@class="price-box"]/span/span[@class="price"]/text()').re(r"((\d+,)*\d+\.\d+)")[0])
        item['headline'] = sel.xpath('//meta[@property="og:title"]/@content').extract()[0]
        item['desc'] = sel.xpath('//meta[@name="description"]/@content').extract()[0]
        item['vendor'] = self.name

        return item
