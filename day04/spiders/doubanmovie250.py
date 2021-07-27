# -*- coding: utf-8 -*-

# 实现爬取内容的下载  抽取关键信息

"""
    student ID: 2020302877
    author:项裕顺
"""


import scrapy

from day04.items import Day04Item


class Doubanmovie250Spider(scrapy.Spider):
    name = 'doubanmovie250'
    allowed_domains = ['movie.douban.com']

    # 爬取的地址
    start_urls = ['http://movie.douban.com/top250']

    # def parse(self, response):
    #     print(response.text)
    #     pass

    def parse(self, response):
        currentpPage_movie_item = response.xpath('//div[@class="item"]')
        for movie_item in currentpPage_movie_item:
            # 创建一个movie对象
            movie = Day04Item()
            # 获取电影排名并赋值rank属性
            movie['rank'] = movie_item.xpath(
                'div[@class="pic"]/em/text()'
            ).extract()
            # 获取电影名称并赋值title属性
            movie['title'] = movie_item.xpath(
                'div[@class="info"]/div[@class="hd"]/a/span[@class="title"][1]/text()'
            ).extract()
            # 获取电影海报地址并赋值pic_url属性
            movie['pic_url'] = movie_item.xpath(
                'div[@class="pic"]/a/img/@src'
            ).extract()
            movie['actor'] = movie_item.xpath(
                'div[@class="info"]/div[@class="bd"]/p/text()[1]'
            ).extract()

            # 合并主演信息，删去前面无用信息
            movie['actor'] = movie['actor'][0].split()
            while len(movie['actor']) > 0 and movie['actor'][0] != "主演:":
                del movie['actor'][0]
                pass
            if len(movie['actor']) > 1:
                for oneMovie in movie['actor'][1:]:
                    movie['actor'][0] += oneMovie
                    pass
                pass
            while len(movie['actor']) > 1:
                del movie['actor'][1]
                pass

            # 将封装好的一个电影信息添加到容器中，yield作用是创建一个列表并添加元素
            yield movie
            pass

        # 下一页请求跳转，实现自动翻页
        nextPage = response.xpath('//span[@class="next"]/a/@href')
        # 判断nextPage是否有效（无效代表当前页面为最后一页）
        if nextPage:
            # 获取nextPage中的下一页链接地址并加入到respones对象的请求地址中
            url = response.urljoin(nextPage[0].extract())
            # 发送下一页请求并调用parse()函数继续解析
            yield scrapy.Request(url, self.parse)
        pass
