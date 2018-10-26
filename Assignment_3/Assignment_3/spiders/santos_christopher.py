# -*- coding: utf-8 -*-
import scrapy

"""""""""
Name: Assignment #3 - Crawling a Web URL using Scrapy
Author: Chris Santos
Last Modified: Oct. 29th, 2018
"""""""""

class SantosChristopherSpider(scrapy.Spider):
    name = 'santos_christopher'
    start_urls = {
        # Holds the base and accomponing urls, and if visited
        'http://www.cs.utep.edu/makbar/A3/A2.html':True
    }

    """
    Scrapy will start this method initial and send requests
    to allow crawling, respecting the rules of the robots.txt
    """
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    """
    Parses through the output response and identifies the links
    to other URL pages.
    """
    def parse(self, response):
        self.log('Crawling stopped (finished)')
        output = "santos_christopher.txt"
        for link in response.xpath('//a/@href'):
            self.log('\n\tLink found: %s' % link)
            self.start_urls[link] = False
        self.log('Stopping spider (finished)')