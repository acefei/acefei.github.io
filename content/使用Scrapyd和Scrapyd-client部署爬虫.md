Title: 使用Scrapyd和Scrapyd-client部署爬虫
Date: 2017-10-30 09:17
Category: Development
Tags: python,scrapy
Authors: Ace Fei

### 基本介绍
#### [Scrapyd](https://github.com/scrapy/scrapyd)
Scrapyd is a service for running Scrapy spiders.
It allows you to deploy your Scrapy projects and control their spiders using a HTTP JSON API.    
Scrapyd can manage multiple projects and each project can have multiple versions uploaded, but only the latest one will be used for launching new spiders.

#### [Scrapyd-client](https://github.com/scrapy/scrapyd-client)
Scrapyd-client is a client for Scrapyd. It provides the general scrapyd-client and the scrapyd-deploy utility which allows you to deploy your project to a Scrapyd server.

### 安装
```
pip install scrapyd scrapyd-client
```

### 配置服务器信息
当我们使用scrapy startnewproject来创建新工程时，会自动生成一个scrapy.cfg文件。
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
其中有两个地方是需要我们更新的：
> proto_server是自定义的服务器名称         
> url是指scrapyd启动后，默认的服务器地址


### 启动scrapyd服务
执行scrapyd，然后用浏览器打开http://localhost:6800/查看界面是否启动成功

### 部署project
部署有两种方式：
1. 通过json API:
[addversion.json](http://scrapyd.readthedocs.io/en/stable/api.html?highlight=egg#addversion-json) 
```
curl http://localhost:6800/addversion.json -F project=prototypes -F version=r23 -F egg=@prototypes.egg
```
其中egg需要用scrapyd-deploy来生成
```
# 进入scrapy工程目录
scrapyd-deploy --build-egg prototypes.egg
```

2. 通过scrapyd-deploy一键部署
```
scrapyd-deploy proto_server -p prototypes
```

部署好后，我们可以用命令查看
```
scrapyd-deploy -L proto_server
```

然后在http://localhost:6800/查看界面发现Available projects：**prototypes**    
![image](http://note.youdao.com/favicon.ico)

### 运行spider
```
curl http://localhost:6800/schedule.json -d project=prototypes -d spider=qichacha
```
> Note:
请务必确认在spider脚本中的初始化中对父类也进行初始化，否则会报错`exceptions.TypeError: __init__() got an unexpected keyword argument '_job'`

### Further
[ ]  集成[DormyMo/SpiderKeeper](https://github.com/DormyMo/SpiderKeeper)或[Gerapy/Gerapy](https://github.com/Gerapy/Gerapy)

