Title: 如何在unittest cases之间传递变量
Date: 2017-10-26 09:53
Category: Development
Tags: Python,unittest
Authors: Ace Fei


想必大家在写Python UT的时候，偶尔会遇到一些测试用例需要同时测试CRUD的接口。
这时需要在test cases之间传递变量该如何做呢？

一开始，我们想既然是在一个class里，直接给instance增加attribute不就好了么?
```
import unittest

class TestA(unittest.TestCase):
    def __init__(self, testname):
        super(TestA, self).__init__(testname)
        self.transmit_var = None

    def test_1(self):
        self.transmit_var = 'hello world'

    def test_2(self):
        print self.transmit_var

if __name__ == "__main__":
    unittest.main(verbosity=2)

```
结果...想当然了。
```
test_1 (__main__.TestA) ... ok
test_2 (__main__.TestA) ... None
ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
**知识点一：在unittest中, 执行每个testcase的时候，会刷新instance attribute**

既然self不行，那cls呢？

那我们再想想unittest在执行class级别的setup，teardown的时候，其中的class attribute是不是对每个testcase都生效。

> 通过查看源码可以知道self.__class__ is cls。

```
import unittest

class TestA(unittest.TestCase):
    def test_1(self):
        self.__class__.transmit_var = 'hello world'

    def test_2(self):
        print self.__class__.transmit_var

if __name__ == "__main__":
    unittest.main(verbosity=2)
```
Bingo！ 
```
test_1 (__main__.TestA) ... ok
test_2 (__main__.TestA) ... hello world
ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
**知识点二：在unittest中，绑定在class的attribute可以在testcase之间传递**

温故而知新：
[Class and Instance Attributes](https://www.python-course.eu/python3_class_and_instance_attributes.php)
