# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_splash import SplashRequest
from datetime import datetime
import pandas as pd


from weatherinfo.items import WeatherinfoItem


def genDatalist(begin, end):
    date_l = [datetime.strftime(x, '%Y-%m-%d') for x in list(pd.date_range(start=begin, end=end))]
    return  date_l


def genStartUrls():
    datelist = genDatalist(datetime(2015, 1, 1), datetime(2015, 12, 31))
    # prefix = 'https://www.wunderground.com/history/daily/us/ca/burbank/KBUR/date/'
    prefix = 'https://www.wunderground.com/history/daily/us/wa/seattle/KSEA/date/'
    urls = [prefix + x for x in datelist]
    return urls


class WeathercrawlerSpider(scrapy.Spider):
    name = 'weathercrawler'
    allowed_domains = ['https://www.wunderground.com/']

    # start_urls = ['https://www.wunderground.com/history/daily/us/ca/burbank/KBUR/date/2015-1-1']
    start_urls = genStartUrls()
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url,
                                callback=self.parse,
                                endpoint='render.html',
                                args={
                                    'wait': 30,
                                    'timeout': 60
                                })

    def fill_field(self, row, item, name, path):
        """
        a helper function to fill each field
        """
        try:
            item[name] = row.xpath(path).extract()[0]
        except IndexError:
            item[name] = ''

    def parse(self, response):

        date = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", response.url).group(0)

        tbody_xpath = '//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/' \
                      'lib-city-history-observation/div/div[2]/table/tbody//tr'

        tbody = response.xpath(tbody_xpath)

        for row in tbody:
            item = WeatherinfoItem()

            item['Date'] = date

            # Field Time
            self.fill_field(row, item, 'Time', 'td[1]/span/text()')

            # Field Temperature
            self.fill_field(row, item, 'Temperature', 'td[2]/lib-display-unit/span/span[1]/text()')

            # Field DewPoint
            self.fill_field(row, item, 'DewPoint', 'td[3]/lib-display-unit/span/span[1]/text()')

            # Field Humidity
            self.fill_field(row, item, 'Humidity', 'td[4]/lib-display-unit/span/span[1]/text()')

            # Field Wind
            self.fill_field(row, item, 'Wind', 'td[5]/span/text()')

            # Field WindSpeed
            self.fill_field(row, item, 'WindSpeed', 'td[6]/lib-display-unit/span/span[1]/text()')

            # Field WindGust
            self.fill_field(row, item, 'WindGust', 'td[7]/lib-display-unit/span/span[1]/text()')

            # Field Pressure
            self.fill_field(row, item, 'Pressure', 'td[8]/lib-display-unit/span/span[1]/text()')

            # Field Precip
            self.fill_field(row, item, 'Precip', 'td[9]/lib-display-unit/span/span[1]/text()')

            # Field Condition
            self.fill_field(row, item, 'Condition', 'td[10]/span/text()')

            yield item

