# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# 关键信息的提取类

import scrapy


class Day04Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 声明爬取对象
    rank = scrapy.Field()
    title = scrapy.Field()
    pic_url = scrapy.Field()
    actor = scrapy.Field()
    pass
