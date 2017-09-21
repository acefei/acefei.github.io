Title: BloomFilter For Scrapy Redis
Date: 2017-09-21 15:29
Category: Development
Tags: Python,Scrapy
Authors: Ace Fei

### Summary: 
This article will illustrate how to renovate scrapy-redis to dupefilter.

### Why use bloomfilter
[Tips on optimizing scrapy for a high performance](http://alexeyvishnevsky.com/2013/11/tips-on-optimizing-scrapy-for-a-high-performance/)

### How to integrate bloomfilter into scrapy redis
1. copy scrapy_redis into the path alongside settings in scrapy project

2. implement bloom_filter.py in scrapy_redis path
   the code in https://github.com/acefei/scrapy-redis-docker/blob/master/scrapy_redis_demo/scrapy_redis_demo/bloom_filter.py

3. modify scrapy_redis/dupefilter.py
```
    def __init__(self, server, key, debug=False):
        """Initialize the duplicates filter.

        Parameters
        ----------
        server : redis.StrictRedis
            The redis server instance.
        key : str
            Redis key Where to store fingerprints.
        debug : bool, optional
            Whether to log filtered requests.

        """
        self.server = server
        self.key = key
        self.debug = debug
        self.logdupes = True

        # 集成布隆过滤器
        self.bf = BloomFilter(conn=server, key=key)     # 利用连接池连接Redis

```
```
    def request_seen(self, request):
        """Returns True if request was already seen.

        Parameters
        ----------
        request : scrapy.http.Request

        Returns
        -------
        bool

        """
        # 集成布隆过滤器
        if self.bf.is_exist(fp):    # 判断如果域名在Redis里存在
            return True
        else:
            self.bf.add(fp)         # 如果不存在，将域名添加到Redis
            return False

        #fp = self.request_fingerprint(request)
        # This returns the number of values added, zero if already exists.
        #added = self.server.sadd(self.key, fp)
        #return added == 0

```
4. Add scrapy_redis configration into settings.py
Note: use our scrapy_redis code like <scrapy_project_name>.scrapy_redis instead of scrapy_redis that created by pip install
```
##################################
# Configuration for scrapy-redis {
DUPEFILTER_CLASS = "scrapy_redis_demo.scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis_demo.scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True

ITEM_PIPELINES = {
  'scrapy_redis_demo.scrapy_redis.pipelines.RedisPipeline': 400,
}

# if u add 'network_mode: "host"' in scraper service in docker-compose.yaml
# use host ip to access redis server
REDIS_HOST = '172.16.100.62'
# else use redis hostname to access redis server
#REDIS_HOST = 'redis'
REDIS_PORT = 6379

# Specify your redis uri
# the uri scheme syntax: http://www.iana.org/assignments/uri-schemes/prov/redis
#REDIS_URL = 'redis://172.16.100.62:6379'

# }
##################################

```
5. import <scrapy_project_name>.scrapy_redis in your spiders/xxxxx.py
```
from scrapy_redis_demo.scrapy_redis.spiders import RedisCrawlSpider
```
