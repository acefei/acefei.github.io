Title: scä½¿ç”¨Scrapydå’ŒScrapyd-clientéƒ¨ç½²çˆ¬è™«
Date: 2017-10-30 09:17
Category: Development
Tags: pythonï,scrapy
Authors: Ace Fei


### ¿¿¿¿
#### [Scrapyd](https://github.com/scrapy/scrapyd)
Scrapyd is a service for running Scrapy spiders.
It allows you to deploy your Scrapy projects and control their spiders using a HTTP JSON API.
Scrapyd can manage multiple projects and each project can have multiple versions uploaded, but only the latest one will be used for launching new spiders.

#### [Scrapyd-client](https://github.com/scrapy/scrapyd-client)
Scrapyd-client is a client for Scrapyd. It provides the general scrapyd-client and the scrapyd-deploy utility which allows you to deploy your project to a Scrapyd server.

### ¿¿
```
pip install scrapyd scrapyd-client
```

### ¿¿¿¿¿¿¿
¿¿¿¿¿scrapy startnewproject¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿scrapy.cfg¿¿¿
```
# Automatically created by: scrapy startproject
#
# For more information about the [deploy] section see:
# https://scrapyd.readthedocs.org/en/latest/deploy.html

[settings]
default = prototypes.settings

[deploy:proto_server]
url = http://localhost:6800/
project = prototypes
```
¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿
> proto_server¿¿¿¿¿¿¿¿¿¿
> url¿¿scrapyd¿¿¿¿¿¿¿¿¿¿¿¿


### ¿¿scrapyd¿¿
¿¿scrapyd¿¿¿¿¿¿¿¿¿http://localhost:6800/¿¿¿¿¿¿¿¿¿¿

### ¿¿project
¿¿¿¿¿¿¿¿
1. ¿¿json API:
[addversion.json](http://scrapyd.readthedocs.io/en/stable/api.html?highlight=egg#addversion-json)
```
curl http://localhost:6800/addversion.json -F project=prototypes -F version=r23 -F egg=@prototypes.egg
```
¿¿egg¿¿¿scrapyd-deploy¿¿¿
```
# ¿¿scrapy¿¿¿¿
scrapyd-deploy --build-egg prototypes.egg
```

2. ¿¿scrapyd-deploy¿¿¿¿
```
scrapyd-deploy proto_server -p prototypes
```

¿¿¿¿¿¿¿¿¿¿¿¿¿¿
```
scrapyd-deploy -L proto_server
```

¿¿¿http://localhost:6800/¿¿¿¿¿¿Available projects¿**prototypes**
![image](http://note.youdao.com/favicon.ico)

### ¿¿spider
```
curl http://localhost:6800/schedule.json -d project=prototypes -d spider=qichacha
```
> Note:
¿¿¿¿¿¿spider¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿`exceptions.TypeError: __init__() got an unexpected keyword argument '_job'`

### Further
[ ]  ¿¿[DormyMo/SpiderKeeper](https://github.com/DormyMo/SpiderKeeper)¿[Gerapy/Gerapy](https://github.com/Gerapy/Gerapy)

