# -*- coding: utf-8 -*-
import scrapy

class SantosChristopherSpider(scrapy.Spider):
    name = 'santos_christopher'
    start_urls = {
        'http://www.cs.utep.edu/makbar/A3/A2.html':True
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        output = "santos_christopher.txt"
        with open(output, 'wb') as o:
            for link in response.xpath('//a/@href'):
                self.log('Link found: %s' % link)
        self.log('Spider has stopped crawling...')