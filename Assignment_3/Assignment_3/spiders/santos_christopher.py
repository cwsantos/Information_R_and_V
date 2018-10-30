# -*- coding: utf-8 -*-
import scrapy

"""""""""
Name: Assignment #3 - Crawling a Web URL using Scrapy
Author: Chris Santos
Last Modified: Oct. 29th, 2018
"""""""""

class SantosChristopherSpider(scrapy.Spider):
    name = 'santos_christopher'
    BASEURL = 'http://www.cs.utep.edu/makbar/A3'
    visited = [
        'http://www.cs.utep.edu/makbar/A3/A2.html'
    ]
    words = {}

    """
    Scrapy will start this method initial and send requests
    to allow crawling, respecting the rules of the robots.txt
    """
    def start_requests(self):
        for url in self.visited:
            yield scrapy.Request(url=url, callback=self.parse)

    """
    Parses through the output response and identifies the links
    to other URL pages, and crawls those links
    """
    def parse(self, response):
        output = 'santos_christopher.txt'
        for link in response.xpath('//a/@href').extract():
            if link in self.visited:
                continue
            else:
                self.log('>> Link found: %s' % link)
                self.visited.append(link)
                self.parseBody(link, response.body)
                link = link[:0] + link[1:]
                new_link = self.BASEURL + link
                yield scrapy.Request(url=new_link, callback=self.parse)

    """
    Creates a text file to parse through and count the number of
    words in the webpage, as well as count how many times they
    appear
    """
    def parseBody(self, link, body):
        link = link.replace('/', '-')
        link = link.replace('.html', '')
        link = link[2:4] + link[4:len(link)]
        with open(('%s_body.txt' % link), 'wb') as o:
            o.write(body)