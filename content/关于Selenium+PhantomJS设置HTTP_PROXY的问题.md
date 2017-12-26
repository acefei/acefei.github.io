Title: 关于Selenium+PhantomJS设置HTTP PROXY的问题
Date: 2017-12-21 15:12
Category: Development
Tags: python,phantomjs,spider
Authors: Ace Fei


[TOC]

在写爬虫的时候，经常会遇到anti-spider，这时候我们可以采取切换代理ip来绕过限制。但是最近在Selenium+PhantomJS实践过程中遇到一个很trick的问题，在此做一下记录。

## python requests with proxy
一开始我们还是用pythonic的方式来看看，http proxy是如何隐藏真实ip的。
```
import requests
print "--No Proxy--"
print requests.get("http://httpbin.org/ip").content

# 在网上随便找个免费http代理
proxy='182.121.201.9:9999'
print "--Proxy {0}--".format(proxy)
proxies = { "http": "http://{0}".format(proxy) }
print requests.get("http://httpbin.org/ip", proxies=proxies).content
```
output:
```
--No Proxy--
{
  "origin": "36.152.29.163"
}

--Proxy 182.121.201.9:9999--
{
  "origin": "36.152.29.163, 182.121.204.0"
}
```

可以看出来origin的值插入了一条新的ip，证明设置proxy生效了。

但是我们要注意，上面使用的代理并不是高匿的，所以从origin里面还是能找到机器的真实ip(仍然会被反爬)。
高匿ip的输出应该是以下结果：
```
--No Proxy--
{
  "origin": "36.152.29.163"
}

--Proxy 113.218.218.86:808--
{
  "origin": "113.218.218.86"
}
```


## phantomjs with proxy
编辑httpbin_test.js，
```
"use strict";
var page = require('webpage').create();
page.open('http://httpbin.org/ip', function (status) {
    if (status !== 'success') {
        console.log('Unable to access network');
    } else {
        console.log(page.content);
    }
    phantom.exit();
});
```
执行phantomjs命令，

```
$ phantomjs --proxy=182.121.201.9:9999 httpbin_test.js
<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">{
  "origin": "36.152.29.163, 182.121.204.0"
}
</pre></body></html>

```
Ok，proxy设置成功。

## selenium + phantomjs with proxy
Stackoverflow上有人推荐方案，
```
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': '182.121.201.9:9999'  # 代理ip和端口
})

desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()

proxy.add_to_capabilities(desired_capabilities)
print "add proxy" + proxy.http_proxy

driver = webdriver.PhantomJS(desired_capabilities=desired_capabilities)
driver.get('http://httpbin.org/ip')
print driver.page_source
driver.close()
```
output：
```
add proxy182.121.201.9:9999
<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">{
  "origin": "36.152.29.163"
}
</pre></body></html>
```
奇怪，这里发现proxy并没有生效，不知道是不是我的phantomjs 1.9.7版本的bug。

那换个方案试试，
```
from selenium import webdriver

service_args = [
    '--proxy=182.121.201.9:9999',
]
driver = webdriver.PhantomJS(service_args=service_args)
driver.get('http://httpbin.org/ip')
print driver.page_source
driver.close()
```
output：
```
<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">{
  "origin": "36.152.29.163, 182.121.204.0"
}
</pre></body></html>
```
Ok, proxy设置成功了。

可以看出来，通过service_args传递参数其实跟phantomjs命令行传参的是一样效果。

那么，如果想使用带auth的代理，只要加上对应的option就好了，很方便。
```
$phantomjs -h
Usage:
   phantomjs [switchs] [options] [script] [argument [argument [...]]]

Options:
  --cookies-file=<val>                 Sets the file name to store the persistent cookies
  --config=<val>                       Specifies JSON-formatted configuration file
  --debug=<val>                        Prints additional warning and debug message: 'true' or 'false' (default)
  --disk-cache=<val>                   Enables disk cache: 'true' or 'false' (default)
  --ignore-ssl-errors=<val>            Ignores SSL errors (expired/self-signed certificate errors): 'true' or 'false' (default)
  --load-images=<val>                  Loads all inlined images: 'true' (default) or 'false'
  --local-storage-path=<val>           Specifies the location for offline local storage
  --local-storage-quota=<val>          Sets the maximum size of the offline local storage (in KB)
  --local-to-remote-url-access=<val>   Allows local content to access remote URL: 'true' or 'false' (default)
  --max-disk-cache-size=<val>          Limits the size of the disk cache (in KB)
  --output-encoding=<val>              Sets the encoding for the terminal output, default is 'utf8'
  --remote-debugger-port=<val>         Starts the script in a debug harness and listens on the specified port
  --remote-debugger-autorun=<val>      Runs the script in the debugger immediately: 'true' or 'false' (default)
  --proxy=<val>                        Sets the proxy server, e.g. '--proxy=http://proxy.company.com:8080'
  --proxy-auth=<val>                   Provides authentication information for the proxy, e.g. ''-proxy-auth=username:password'
  --proxy-type=<val>                   Specifies the proxy type, 'http' (default), 'none' (disable completely), or 'socks5'
  --script-encoding=<val>              Sets the encoding used for the starting script, default is 'utf8'
  --web-security=<val>                 Enables web security, 'true' (default) or 'false'
  --ssl-protocol=<val>                 Sets the SSL protocol (supported protocols: 'SSLv3' (default), 'SSLv2', 'TLSv1', 'any')
  --ssl-certificates-path=<val>        Sets the location for custom CA certificates (if none set, uses system default)
  --webdriver=<val>                    Starts in 'Remote WebDriver mode' (embedded GhostDriver): '[[<IP>:]<PORT>]' (default '127.0.0.1:8910')
  --webdriver-logfile=<val>            File where to write the WebDriver's Log (default 'none') (NOTE: needs '--webdriver')
  --webdriver-loglevel=<val>           WebDriver Logging Level: (supported: 'ERROR', 'WARN', 'INFO', 'DEBUG') (default 'INFO') (NOTE: needs '--webdriver')
  --webdriver-selenium-grid-hub=<val>  URL to the Selenium Grid HUB: 'URL_TO_HUB' (default 'none') (NOTE: needs '--webdriver')
  -w,--wd                              Equivalent to '--webdriver' option above
  -h,--help                            Shows this message and quits
  -v,--version                         Prints out PhantomJS version

Any of the options that accept boolean values ('true'/'false') can also accept 'yes'/'no'.

Without any argument, PhantomJS will launch in interactive mode (REPL).

Documentation can be found at the web site, http://phantomjs.org.

```
