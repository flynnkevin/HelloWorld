# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import pymongo
from JDCrawler.items import JDGood

class JdcrawlerPipeline(object):

    def __init__(self):
        self.server="121.42.197.131"
        self.port=27017
        self.db='studydb'
        self.col="jdgoods"
        conn=pymongo.MongoClient(self.server,self.port)
        db=conn[self.db]
        self.collection=db[self.col]

    def process_item(self, item, spider):
        if isinstance(item,JDGood):
            try:
                self.collection.insert(dict(item))
            except Exception as e:
                pass
        return item