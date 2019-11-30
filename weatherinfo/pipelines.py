# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class WeatherinfoPipeline(object):
    # creat a file handle
    def __init__(self):
        self.f = open('./seattle/seattle_weatherdata_2015_F.csv', 'wb')
        headers = ['Date', 'Time', 'Temperature', 'DewPoint', 'Humidity', 'Wind',
                    'WindSpeed', 'WindGust', 'Pressure', 'Precip', 'Condition']
        self.writer = csv.DictWriter(self.f, fieldnames=headers)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow((dict(item)))
        return item

    def close_spider(self,spider):
        self.f.close()
        # close spider