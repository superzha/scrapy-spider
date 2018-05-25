# -*- coding: utf-8 -*-
import scrapy


class InstitutionSpider(scrapy.Spider):
    name = 'institution'
    allowed_domains = ['www.ynzp.com']
    start_urls = ['http://www.ynzp.com/cms/publicnotice/530100.html']

    def parse(self, response):
        pass
