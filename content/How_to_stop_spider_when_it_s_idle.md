Title: How to stop scrapy-redis spider when it's idle
Date: 2017-11-21 06:44
Category: Development
Tags: scrapy,python
Authors: Ace Fei


scrapy-redis是以redis为基础的组件替换了原本scrapy的部分功能，让它可以分布式运作。
但是在使用的时候发现，它一旦待爬队列为空，spider不会自动结束，而是一直在等待redis push新的urls，在日志末尾里可以看到如下内容：
```
2017-11-21 08:15:10 [scrapy.extensions.logstats] INFO: Crawled 1 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
```

在scrapy-redis的README中得知:
```
# Max idle time to prevent the spider from being closed when distributed crawling.
# This only works if queue class is SpiderQueue or SpiderStack,
# and may also block the same time when your spider start at the first time (because the queue is empty).
SCHEDULER_IDLE_BEFORE_CLOSE = 10
```
添加到settings后，发现spider还是不会退出，只是不停的报exception。

于是，我想既然log中能知道spider的状态，那我们就再加一个判断，连续出现X次scrapyed 0 itmes就退出不就好了么。

继续研读源码发现，这段log是scrapy extensions实现的，而且scrapy支持自定义extensions。

照着logsstats实现一个[close spider extension](https://github.com/acefei/ace-crawler/blob/master/prototypes/extensions.py)

并添加如下配置到settings中：
```
EXTENSIONS = {
     'prototypes.extensions.CloseSpiderRedis': 100,
},
CLOSE_SPIDER_AFTER_IDLE_TIMES = 5
```

*Done！*
```
2017-11-21 08:15:10 [scrapy.extensions.logstats] INFO: Crawled 1 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2017-11-21 08:16:10 [scrapy.extensions.logstats] INFO: Crawled 1 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2017-11-21 08:17:10 [scrapy.extensions.logstats] INFO: Crawled 1 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2017-11-21 08:18:10 [scrapy.extensions.logstats] INFO: Crawled 1 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2017-11-21 08:19:10 [scrapy.extensions.logstats] INFO: Crawled 1 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2017-11-21 08:19:10 [scrapy.core.engine] INFO: Closing spider (close spider after 5 times of spider idle)
2017-11-21 08:19:10 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 493,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 23397,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 1,
 'downloader/response_status_count/302': 1,
 'finish_reason': 'close spider after 5 times of spider idle',
 'finish_time': datetime.datetime(2017, 11, 21, 8, 19, 10, 770725),
 'log_count/DEBUG': 6,
 'log_count/INFO': 14,
 'memusage/max': 936964096,
 'memusage/startup': 936964096,
 'response_received_count': 1,
 'scheduler/dequeued/redis': 2,
 'scheduler/enqueued/redis': 2,
 'start_time': datetime.datetime(2017, 11, 21, 8, 13, 10, 735722)}
2017-11-21 08:19:10 [scrapy.core.engine] INFO: Spider closed (close spider after 5 times of spider idle)
```

最后要注意：
默认scrapy-redis退出后，会清掉requests/dupefilter的内容，如果你想保留配置，请务必加上：
```
# Don't cleanup redis queues, allows to pause/resume crawls.
#SCHEDULER_PERSIST = True
```

