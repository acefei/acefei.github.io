Title: Web Scraping Practice
Date: 2017-06-23 02:37
Category: Python
Authors: Ace Fei
Summary: Scraping and downloading MP3 in parallel by python grequests package

### Background
Recently, I found a [TOEIC test website](http://www.apexlegend.com/eas/media/) with enomous mp3 materials.

Just in time, I decided to download by automation script.

### Requirement
```
pip install lxml
# https://github.com/kennethreitz/grequests
pip install grequests
```

### HTML Scraping
[lxml](http://lxml.de/) is a pretty extensive library written for parsing XML and HTML documents very quickly, even handling messed up tags in the process. We will also be using the [Requests](http://docs.python-requests.org/en/latest/) module instead of the already built-in urllib2 module due to improvements in speed and readability. 

About the details, please refer to [the link](http://docs.python-guide.org/en/latest/scenarios/scrape/#html-scraping)


### Concurrency
We will use [GRequests](https://github.com/kennethreitz/grequests) which allows you to use Requests with Gevent to make asynchronous HTTP Requests easily. Or use the fork: [FRequests](https://github.com/i-trofimtschuk/frequests) 

*Note:*

1. Using pool to limit concurrency. 
GRequests doesn't use pool by default, please see below code snippet: 
```
def map(requests, stream=False, size=None, exception_handler=None, gtimeout=None):
    """Concurrently converts a list of Requests to Responses.
    :param requests: a collection of Request objects.
    :param stream: If True, the content will not be downloaded immediately.
    :param size: Specifies the number of requests to make at a time. If None, no throttling occurs.
    :param exception_handler: Callback function, called when exception occured. Params: Request, Exception
    :param gtimeout: Gevent joinall timeout in seconds. (Note: unrelated to requests timeout)
    """

    requests = list(requests)

    pool = Pool(size) if size else None

...
```

In my requirement, there are enomous links need to settle. If don't constrain concurrency, it would lead to the exception "gevent.hub.LoopExit: This operation would block forever".

2. Using session to avoid the fd consuming. 
There is a [same problem](https://github.com/kennethreitz/grequests/issues/54) with me.

The source code is available in [the gist](https://gist.github.com/acefei/2ca602d67e53011878dbf40f1ccda216#file-fetch_mp3_from_apexlegend-py)

### SEE ALSO: 
1. http://xlambda.com/gevent-tutorial/

