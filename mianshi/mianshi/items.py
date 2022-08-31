# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MianshiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    当前状态 = scrapy.Field()
    商品类别 = scrapy.Field()
    申请号 = scrapy.Field()
    申请日期 = scrapy.Field()
    初审日期 = scrapy.Field()
    注册日期 = scrapy.Field()
    申请人 = scrapy.Field()
    代理机构 = scrapy.Field()

    商品类别 = scrapy.Field()
    商品服务项 = scrapy.Field()
    初审公告期号 = scrapy.Field()
    注册公告期号 = scrapy.Field()
    专用权期限 = scrapy.Field()
    是否共有商标 = scrapy.Field()
    商标状态 = scrapy.Field()
    商标公告 = scrapy.Field()
    评审文书 = scrapy.Field()
    pass
