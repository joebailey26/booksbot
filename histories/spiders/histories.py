# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider 

class HistoriesSpider(SitemapSpider):
    name = "histories"
    allowed_domains = ["localhistories.org"]
    sitemap_urls = ['http://localhistories.org/sitemap.xml'] 
    start_urls = [
        'http://localhistories.org/',
    ]

    def parse(self, response):
        item = {}
        item['title']: response.css("h1 ::text").extract_first()
        item['url']: response.url 
        yield item