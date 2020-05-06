# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrabbleItem


class WordsSpider(scrapy.Spider):
    name = 'words'
    allowed_domains = ['www.allscrabblewords.com']
    start_urls = [
        'https://www.allscrabblewords.com/{n}-letter-words/'.\
        format(n=n) for n in range(2, 13)]    # There are words 2 to 12-letters long

    def parse(self, response):
        self.logger.info(f"Successful response from {response.url}")
        items = ScrabbleItem()

        words = response.xpath('//ul[@class="list-inline"]//a/text()').getall()

        items['words'] = words
        yield items
