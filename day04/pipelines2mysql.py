# -*- coding: utf-8 -*-
__author__ = "NWPU Yushun Xiang"

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 导入MySQL模块
import pymysql


# DoubanmoviePipeline类，继承Object类
# 读取爬虫采集到的MySQL数据库，批量插入到数据库中
class Day04Pipeline(object):

    # process_item()函数，将获取到的数据添加到MySQL数据库scrapy的数据表movie_information中
    def process_item(self, item, spider):
        print("--> MySQL: insert to db...")
        # 获取MySQL数据库的链接对象
        db = pymysql.connect(host='localhost', user='root', passwd='xys123', database='scrapy_homework', port=3306,
                             use_unicode=True, charset="utf8")
        try:
            # 获取cur操作游标对象
            cur = db.cursor()
            # 设置cur操作游标字符集为utf-8
            cur.execute('SET NAMES utf8;')
            cur.execute('SET CHARACTER SET utf8;')
            cur.execute('SET character_set_connection=utf8;')

            # 获取电影排名
            movie_rank = item['rank'][0]

            # 获取电影名称
            movie_title = item['title'][0]

            # 获取电影主演名称
            movie_actor = item['actor'][0]

            # 获取电影图片网址
            movie_pic_url = item['pic_url'][0]

            # 定义sql语句模板
            sql = "insert into `movie_information`" \
                  "(movie_information.`排名`,movie_information.`电影名`,movie_information.`演员`,movie_information.`图片网址`)" \
                  "values" \
                  "(%s, %s, %s, %s)"

            # 发送SQL语句并设置参数

            cur.execute(sql, (movie_rank, movie_title, movie_actor, movie_pic_url))

            # 关闭游标
            if cur:
                cur.close()
            # 提交事务
            db.commit()

        finally:
            # 关闭数据链接对象
            if db:
                db.close()
        # 返回item
        return item
