
import json

import scrapy
import datetime
import uuid

from jinshidata.items import EconomicsItem,EventItem,HolidayItem

class RilispiderSpider(scrapy.Spider):
    name = "rilispider"
    allowed_domains = ["rili.jin10.com"]
    start_urls = []

    def start_requests(self):
        begin = datetime.date(2010, 1, 1)
        end = datetime.date(2014, 12, 31)
        delta = datetime.timedelta(1)
        tmp = begin
        while tmp <= end:
            year = tmp.strftime("%Y")
            month = tmp.strftime("%m")
            day = tmp.strftime("%d")
            monthday = tmp.strftime("%m%d")
            # 经济数据
            economics_url = f"https://cdn-rili.jin10.com/web_data/{year}/daily/{month}/{day}/economics.json"
            # 事件
            event_url = f"https://cdn-rili.jin10.com/web_data/{year}/daily/{month}/{day}/event.json"
            # 假期
            holiday_url = f"https://cdn-rili.jin10.com/data/{year}/{monthday}/holiday.json"

            yield scrapy.Request(economics_url, callback=self.parse_economics, dont_filter=True)
            yield scrapy.Request(event_url, callback=self.parse_event, dont_filter=True)
            yield scrapy.Request(holiday_url, callback=self.parse_holiday, dont_filter=True)

            tmp += delta

    def parse_economics(self, response):
        for e in json.loads(response.text):
            economics_item = EconomicsItem()
            economics_item['_id'] = str(uuid.uuid4())
            economics_item['actual'] = e['actual']
            economics_item['actual'] = e['actual']
            economics_item['affect'] = e['affect']
            economics_item['consensus'] = e['consensus']
            economics_item['country'] = e['country']
            economics_item['id'] = e['id']
            economics_item['indicator_id'] = e['indicator_id']
            economics_item['name'] = e['name']
            economics_item['previous'] = e['previous']
            economics_item['pub_time'] = e['pub_time']
            economics_item['pub_time_unix'] = e['pub_time_unix']
            economics_item['revised'] = e['revised']
            economics_item['show_affect'] = e['show_affect']
            economics_item['star'] = e['star']
            economics_item['time_period'] = e['time_period']
            economics_item['time_status'] = e['time_status']
            economics_item['unit'] = e['unit']
            economics_item['video_url'] = e['video_url']
            economics_item['vip_resource'] = e['vip_resource']
            economics_item['url'] = response.url

            yield economics_item

    def parse_event(self, response):
        for e in json.loads(response.text):
            event_item = EventItem()
            event_item['_id'] = str(uuid.uuid4())
            event_item['country'] = e['country']
            event_item['determine'] = e['determine']
            event_item['emergencies'] = e['emergencies']
            event_item['event_content'] = e['event_content']
            event_item['event_time'] = e['event_time']
            event_item['id'] = e['id']
            event_item['note'] = e['note']
            event_item['people'] = e['people']
            event_item['region'] = e['region']
            event_item['star'] = e['star']
            event_item['vip_resource'] = e['vip_resource']
            event_item['url'] = response.url

            yield event_item 

    def parse_holiday(self, response):
        for e in json.loads(response.text):
            holiday_item = HolidayItem()
            holiday_item['_id'] = str(uuid.uuid4())
            holiday_item['exchange_name'] = e['exchange_name']
            holiday_item['date'] = e['date']
            holiday_item['name'] = e['name']
            holiday_item['rest_note'] = e['rest_note']
            holiday_item['id'] = e['id']
            holiday_item['country'] = e['country']
            holiday_item['url'] = response.url
            
            yield holiday_item


