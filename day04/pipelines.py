# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 关于关键信息的处理  输出到控制台 文件 数据库


class Day04Pipeline(object):
    def process_item(self, item, spider):
        print('排名TOP：' + item['rank'][0])
        print('电影名称：' + item['title'[0]])
        print('主演信息：' + item['actor'])
        print('图片地址：' + item['pic_url'][0])
        return item
