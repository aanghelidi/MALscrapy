# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

from scrapy.item import Item
from scrapy.spiders import Spider


class MalscraperPipeline:
    def process_item(self, item: Item, spider: Spider) -> Item:
        return item
