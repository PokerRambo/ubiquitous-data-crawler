# ubiquitous-data-crawler
This repository contains web crawlers to collect ubiquitous data on the Internet.

**1. Weather information collector.**

Since the website [Weather Underground](https://www.wunderground.com) no longer use static page for presenting data, we have to redesign our web crawler to deal  with JS rendering.

We adopt `scrapy` + `splash` to help us achieve our goals. Before coding the crawler, we need to do some tedious preparations.

+ Install splash.  The most convenient way to use splash  is to run it in docker. We highly recommend to install [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) on linux distributions rather than on windows to get rid of all kinds of troubles. 
+ Install splash python module.  ``` pip install scrapy-splash```
+ Install scrapy python module.   ``` pip install scrapy```

After all these, we should start the JS rendering service:

```shell
docker run -p 8050:8050 scrapinghub/splash
```

Then we need to add some configurations to `settings.py` of our weatherinfo project.

Details can be referred to https://github.com/scrapy-plugins/scrapy-splash

To run the crawler, first change directory into the scrapy project, in this case, the `weatherinfo folder`, and then type command:

```shell
scrapy crawl weathercrawler
```

TIPS:

If you want to change the city, just modify the variable `prefix` in the following function in `weathercrawler.py`.

```python
def genStartUrls():
    datelist = genDatalist(datetime(2015, 1, 1), datetime(2015, 12, 31))
    # In this example, we crawl the weather data of Seattle, WA.
    prefix = 'https://www.wunderground.com/history/daily/us/wa/seattle/KSEA/date/'
    urls = [prefix + x for x in datelist]
    return urls
```

