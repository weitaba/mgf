# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter


class MianshiPipeline:
    # pass
    def __init__(self):
        self.file = open('mianshi.csv','wb')

    def process_item(self, item, spider):
        item = dict(item)

        str_data = json.dumps(item , ensure_ascii=False) + ',\n'

        self.file.write(bytes(str_data,encoding = 'utf-8'))

        return item

    def __del__(self):
        self.file.close()