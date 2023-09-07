"""
这是布隆过滤器的生成方法
从现有的数据库中,获得所有已经成功爬取过的url
然后生成布隆过滤器
"""
from bloomfilter import BloomFilter
import pymongo
from jinshidata.settings_custom import MONGO_URI,MONGO_DATABASE


class BloomFilterGen:
    collection_name = "scrapy_items"
    collection_name_Economics = "scrapy_items_Economics"
    collection_name_Event = "scrapy_items_Event"

    def gen_bloomfilter(self):

        client = pymongo.MongoClient(MONGO_URI)
        db = client[MONGO_DATABASE]
        table1 = db[self.collection_name].find({}, {"url": 1})
        table2 = db[self.collection_name_Economics].find({}, {"url": 1})
        table3 = db[self.collection_name_Event].find({}, {"url": 1})
        table1_count = db[self.collection_name].count_documents({})
        table2_count = db[self.collection_name_Economics].count_documents({})
        table3_count = db[self.collection_name_Event].count_documents({})
        total_count = table1_count + table2_count + table3_count
        bloomfilter = BloomFilter(expected_insertions=total_count,err_rate=0.01)
        for i in table1:
            bloomfilter.put(i["url"])
        for i in table2:
            bloomfilter.put(i["url"])
        for i in table3:
            bloomfilter.put(i["url"])
        return bloomfilter



# def main():
#     return BloomFilterGen().gen_bloomfilter()
    
# if __name__ == '__main__':
#     main()
    

