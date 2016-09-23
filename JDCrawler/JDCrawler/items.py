# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class JdcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JDGood(scrapy.Item):
    #商品名称
    gName = Field()
    #商品价格
    # gPrice = Field()
    #商品介绍
    gIntro=Field()
