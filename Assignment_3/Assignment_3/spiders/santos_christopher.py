# -*- coding: utf-8 -*-
import scrapy


class SantosChristopherSpider(scrapy.Spider):
    name = 'santos_christopher'
    start_urls = [
        'http://www.cs.utep.edu/makbar/A3/A2.html'
        ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        output = "santos_christopher.txt"
        with open(output, 'wb') as o:
            o.write(response.body)
        self.log('Saved file to %s' % output)