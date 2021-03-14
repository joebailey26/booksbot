# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider
import re

class HistoriesSpider(SitemapSpider):
    name = 'histories'
    allowed_domains = ["localhistories.org"]
    sitemap_urls = ['http://localhistories.org/sitemap.xml'] 
    start_urls = [
        'http://localhistories.org/',
    ]

    def parse(self, response):
        item = {}
        item['title'] = response.css("p::text").get()
        item['url'] = re.findall("(?<=\/)[^\/]*(?=\.\w+$)", response.url)
        item['content'] = response.css("p::text").getall()
        yield item