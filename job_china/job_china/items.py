# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobChinaItem(scrapy.Item):
    name = scrapy.Field()
    campany_name= scrapy.Field()
    campany_name = scrapy.Field()
    work_position = scrapy.Field()
    salary = scrapy.Field()
    time = scrapy.Field()

    require=scrapy.Field()
    describe=scrapy.Field()
    type=scrapy.Field()
