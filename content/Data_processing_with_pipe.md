Title: Data processing with pipe
Date: 2018-02-24 14:44
Category: Development
Tags: python,function programming
Authors: Ace Fei


[TOC]


现如今云计算，大数据流式处理都会涉及到MapReduce，pipeline等概念，而[《左耳朵耗子：什么是函数式编程？》](https://mp.weixin.qq.com/s?src=11&timestamp=1518417170&ver=693&signature=wfyzH2b5BnDqNMSxwG-fFhxdBy9YkIT2C80e-NGu678wjs0KpMH4a*r8-bXfwUMg-bYxsCx7NQE290qrjRkButMGqbpk0Vu99EtpTeuqMw9E6zCSbZ4HgmF-NauP6859&new=1)对其深入浅出，尤其是最后一段Pipe相关的代码，very graceful and elegent！
那么这篇文章也将练习一下Pipe的用法。


首先，照着耗子哥文章，先来实现一个Pipe装饰器类
```
import functools

class Pipe:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __ror__(self, pipe_left_obj):
        return self.func(pipe_left_obj)

    def __call__(self, *args, **kwargs):
        def wrapped(pipe_left_obj):
            return self.func(pipe_left_obj, *args, **kwargs)

        return Pipe(wrapped)
```
这里用到的[spacial method](https://docs.python.org/3/reference/datamodel.html#special-method-names) `__ror__` 是重载了`|`运算符.
> 注意`__ror__`和`__or__`的区别，重载`__ror__`是因为我们需要数据是从`|`的左边对象传给右边对象，比如`x | y`等于`y.__ror__(x)`, 而`__or__`则相反, 它等于`x.__or__(y)`

Pipe的用法示例：
```
@Pipe
def to_str(data, sep=','):
    return sep.join(map(str, data))

print [1,2,3] | to_str   # output is '1,2,3'
print [4,5,6] | to_str('#')  # output is '1#2#3'
```
这里的`to_str('#')`会调用`Pipe.__call__()`, 实现`__call__`需要注意几点：
- 定义的时候带上`(*args, **kwargs)`来接受`to_str`的参数。
- 返回值应该是Pipe对象，用于`|`运算。
- Pipe初始化的时候需要传入函数对象（wrapped）做参数，且此函数的第一个参数是用于接受`|`左边对象。
- 在`__call__`中的`self.func`是指的`function to_str`, 而在`__ror__`里的`self.func`则是指的`function wrapped`。

教的曲唱不得，为了深刻理解，最好还是自己在pycharm里用debug单步调试一下看看。

接下来我们尝试一下大数据里常遇到场景，假设有一段英文文章，我们对它统计词频并排序后打印分哪几步？
- 先将整段文章分割成单词
- 然后聚合
- 对聚合后的数据进行计数统计
- 根据规则进行排序
- 打印

```
import itertools

@Pipe
def split_to_words(content):
    return content.split()

@Pipe
def groupby(iterable, keyfunc):
    return itertools.groupby(sorted(iterable, key=keyfunc), keyfunc)

@Pipe
def mapping(iterable, func):
    returm (func(x) for x in iterable)

@Pipe
def count(iterable):
    return sum(map(lambda x: 1, iterable))

@Pipe
def sort(iterable, **kwargs):
    return sorted(iterable, **kwargs)

@Pipe
def echo(iterable):
    print iterable
```

我们拿《The Zen of Python》来试试效果：
```
text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

text | split_to_words | groupby(lambda x: x) | mapping(lambda x: (x[0], x[1] | count)) | sort(key =lambda x: x[1], reverse=True) | echo
```
输出如下:
```
[('is', 10), ('better', 8), ('than', 8), ('the', 5), ('to', 5), ('Although', 3), ('be', 3), ('of', 3), ('If', 2), ('a', 2), ('do', 2), ('explain,', 2), ('idea.', 2), ('implementation', 2), ('may', 2), ('never', 2), ('one', 2), ('should', 2), ('way', 2), ('*right*', 1), ('--', 1), ('--obvious', 1), ('Beautiful', 1), ('Complex', 1), ('Dutch.', 1), ('Errors', 1), ('Explicit', 1), ('Flat', 1), ('In', 1), ('Namespaces', 1), ('Now', 1), ('Peters', 1), ('Python,', 1), ('Readability', 1), ('Simple', 1), ('Sparse', 1), ('Special', 1), ('The', 1), ('There', 1), ('Tim', 1), ('Unless', 1), ('Zen', 1), ('ambiguity,', 1), ('and', 1), ('are', 1), ("aren't", 1), ('at', 1), ('bad', 1), ('beats', 1), ('break', 1), ('by', 1), ('cases', 1), ('complex.', 1), ('complicated.', 1), ('counts.', 1), ('dense.', 1), ('easy', 1), ('enough', 1), ('explicitly', 1), ('face', 1), ('first', 1), ('good', 1), ('great', 1), ('guess.', 1), ('hard', 1), ('honking', 1), ('idea', 1), ('implicit.', 1), ('it', 1), ("it's", 1), ('it.', 1), ("let's", 1), ('more', 1), ('nested.', 1), ('never.', 1), ('not', 1), ('now.', 1), ('obvious', 1), ('often', 1), ('one--', 1), ('only', 1), ('pass', 1), ('practicality', 1), ('preferably', 1), ('purity.', 1), ('refuse', 1), ('rules.', 1), ('silenced.', 1), ('silently.', 1), ('special', 1), ('temptation', 1), ('that', 1), ('those!', 1), ('ugly.', 1), ('unless', 1), ("you're", 1)]
```
Works like a charm!

# 参考
- [简单地理解 Python 的装饰器](http://python.jobbole.com/88530/)
- [Python修饰器的函数式编程](https://coolshell.cn/articles/11265.html)
- [函数式编程](https://coolshell.cn/articles/10822.html)

