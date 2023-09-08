# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from jinshidata.items import EconomicsItem,EventItem,HolidayItem
import pymongo
import os

class JinshidataSpiderPipeline:
    
    collection_name = "scrapy_items"
    collection_name_Economics = "scrapy_items_Economics"
    collection_name_Event = "scrapy_items_Event"

    # def __init__(self,mongo_uri,mongo_db):
    def __init__(self):
        self.mongo_uri = os.getenv("MONGO_URI")
        self.mongo_db = os.getenv("MONGO_DATABASE")

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         mongo_uri=crawler.settings.get("MONGO_URI"),
    #         mongo_db=crawler.settings.get("MONGO_DATABASE", "items"),
    #     )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item,EconomicsItem):
            self.db[self.collection_name_Economics].insert_one(ItemAdapter(item).asdict())
        if isinstance(item,EventItem):
            self.db[self.collection_name_Event].insert_one(ItemAdapter(item).asdict())
        if isinstance(item,HolidayItem):
            self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        return item
