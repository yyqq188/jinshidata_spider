# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class EconomicsItem(Item):
    _id = Field()
    actual = Field()
    affect = Field()
    consensus = Field()
    country = Field()
    id = Field()
    indicator_id = Field()
    name = Field()
    previous = Field()
    pub_time = Field()
    pub_time_unix = Field()
    revised = Field()
    show_affect = Field()
    star = Field()
    time_period = Field()
    time_status = Field()
    unit = Field()
    video_url = Field()
    vip_resource = Field()
    url = Field()


class EventItem(Item):
    _id = Field()
    country = Field()
    determine = Field()
    emergencies = Field()
    event_content = Field()
    event_time = Field()
    id = Field()
    note = Field()
    people = Field()
    region = Field()
    star = Field()
    vip_resource = Field()
    url = Field()


class HolidayItem(Item):
    _id = Field()
    country = Field()
    date = Field()
    exchange_name = Field()
    id = Field()
    name = Field()
    rest_note = Field()
    url = Field()
