# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class WhiskyscraperPipeline:
    def __init__(self):
        self.connection = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.connection["test"]
        self.create_collection()

    def create_collection(self):
        self.collection = self.db["whiskies"]
        # self.collection.delete_many({}) # Clear the collection if you want to start from scratch.

    def process_item(self, item, spider):
        self.collection.insert_one(ItemAdapter(item).asdict())
        return item
