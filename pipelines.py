# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import xlwt


class ScrabblePipeline:
    def open_spider(self, spider):
        spider.logger.info('Creating workbook.')
        self.workbook = xlwt.Workbook()

    def close_spider(self, spider):
        spider.logger.info('Saving workbook.')
        self.workbook.save('words.xls')

    def process_item(self, item, spider):
        words = item['words']
        sheet = self.workbook.add_sheet(f'{len(words[0])} letter words')
        for i, word in enumerate(words):
            sheet.write(i, 0, word)
        return item
