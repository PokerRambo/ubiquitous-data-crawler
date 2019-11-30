# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class WeatherinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Date = scrapy.Field()
    Time = scrapy.Field()
    Temperature = scrapy.Field()
    DewPoint = scrapy.Field()
    Humidity = scrapy.Field()
    Wind = scrapy.Field()
    WindSpeed = scrapy.Field()
    WindGust = scrapy.Field()
    Pressure = scrapy.Field()
    Precip = scrapy.Field()
    Condition = scrapy.Field()

