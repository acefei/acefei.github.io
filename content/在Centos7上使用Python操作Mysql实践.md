Title: 在Centos7上使用Python操作Mysql实践
Date: 2017-10-27 01:14
Category: Development
Tags: Python,dataset
Authors: Ace Fei


[TOC]

### Centos7上安装mysql
```
sudo yum install mysql mysql-devel
# centos7上已经使用mariadb替换了mysql，它们仅在安装配置上有些区别，使用上没有差别。
sudo yum install mariadb-server
```

### 配置mysql
```
# 第一次启动会检查/var/lib/mysql目录是否为空，不为空将返回失败
sudo service mariadb start
# 设置mysql密码
sudo mysql_secure_installation
```
如果配置时有任何错误，可在/var/log/mariadb/mariadb.log里查看具体原因


### Python Mysql库安装
```
sudo yum install python-devel
sudo pip install mysql-python
# Toolkit for Python-based database access.
sudo pip install dataset
```

### dataset常见操作
[dataset](http://dataset.readthedocs.io/en/latest/api.html)库是对SQLAlchemy二次封装，使其操作数据库就像操作json文件一样方便。

#### 连接Mysql
```
db = dataset.connect('mysql://username:password@port/dbname?charset=utf8')
```

#### 添加记录
```
data = {
    'key': 1,
    'column2': 2,
    'column3': 3,
}
# 插入记录，如果key，存在则报错
db[t_name].insert(data, ['key'])
# 插入记录，如果key，存在则更新
db[t_name].upsert(data, ['key'])
```
#### 查找记录
```
# 打印表的字段
print self.db['t_name'].columns

# 打印表中所有数据
for row_data in self.db['t_name'].all():
    print row_data

# 根据多个条件找记录, 返回的是列表
self.db['t_name'].find(key1 = 1, key2 =2)

# 返回一条记录
self.db['t_name'].find_one(key1 = 1, key2 =2)
```
考虑到find()查找性能，也可以使用原生的sql语句来进行query
```
select * from t_name limit 99
```


#### 更新记录
```
data = {
    'key': 1,
    'column2': 2,
    'column3': 3,
}
self.db['t_name'].update(data, ['key'])
```

#### 删除记录
```
self.db['t_name'].delete(key1=1, key2=2)
# 删除所有记录
self.db['t_name'].delete()
```

#### 关于dataset导出数据
现在dataset被分离成两个模块，如果想导出数据请看[datafreeze](https://github.com/pudo/datafreeze)

详细用法请见[dataset readthedocs](https://dataset.readthedocs.io/en/latest/)

