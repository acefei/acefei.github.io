Title: 使用cookiecutter+pypackage-minimal快速制作一个python package
Date: 2018-01-24 15:24
Category: DevOps
Tags: python,cookiecutter,package
Authors: Ace Fei


[TOC]
### Prerequisites
```
pip install scrapy
pip install cookiecutter
https://github.com/kragniz/cookiecutter-pypackage-minimal.git
```

### Start [cookiecutter](https://github.com/audreyr/cookiecutter)
```
$ cookiecutter cookiecutter-pypackage-minimal/
/usr/lib/python2.7/site-packages/requests/__init__.py:80: RequestsDependencyWarning: urllib3 (1.22) or chardet (2.2.1) doesn't match a supported version!
  RequestsDependencyWarning)
author_name [Louis Taylor]: acefei
author_email [louis@kragniz.eu]: acefei@163.com
package_name [cookiecutter_pypackage_minimal]: scrapy_templates
package_version [0.1.0]:
package_description [An opinionated, minimal cookiecutter template for Python packages]: Templates for creating new projects with startproject command and new spiders with genspider command.
package_url [https://github.com/borntyping/cookiecutter-pypackage-minimal]: https://github.com/acefei/scrapy_templates
readme_pypi_badge [True]:
readme_travis_badge [True]: False
readme_travis_url [https://travis-ci.org/borntyping/cookiecutter-pypackage-minimal]: False


$ ls scrapy_templates/*
scrapy_templates/README.rst  scrapy_templates/setup.py  scrapy_templates/tox.ini

scrapy_templates/scrapy_templates:
__init__.py

scrapy_templates/tests:
__init__.py  test_sample.py
```

### Create scrapy template 
Copy the original template from scrapy project.
```
cd scrapy_templates/scrapy_templates/
mkdir scrapy && cd scrapy
cp -r /usr/lib64/python2.7/site-packages/scrapy/templates/project .
```
Now, you can customize the template in `scrapy_templates/scrapy_templates/scrapy`

### Add non-package files
Since the templates path is not a python package, to specify those files to distribute, we should add  [MANIFEST](https://docs.python.org/2/distutils/sourcedist.html#manifest) file.       
```
# in MANIFEST
recursive-include  scrapy_templates/  *
```
In order for these files to be copied at install time to the package’s folder inside site-packages, you’ll need to supply `include_package_data=True` to the setup() function.

### Command Line Script
1. write a python script command_line.py with some functions in the package.

2. register those functihons to setup() function.
```
import setuptools

setuptools.setup(
    ...
    entry_points = {
        'console_scripts': [
            'scrapy-startproject=scrapy_templates.command_line:startproj',
            'scrapy-genspider=scrapy_templates.command_line:genspider',
        ],
    }
    ...
)
```

### Specifying Dependencies
Edit `setup.py`, we just add an install_requires keyword argument:
```
import setuptools

setuptools.setup(
    ...
    install_requires=[
        'scrapy-redis',
        'scrapy-splash',
        'scrapy-random-useragent',
        'scrapy-redis-bloomfilter',
    ],
    ...
)
```

### Summary
Now, we have finished an python package.  
It's easy to install this package by pip.
```
pip install git+https://github.com/acefei/scrapy_templates.git
```
About this package details, please find [acefei/scrapy_templates
](https://github.com/acefei/scrapy_templates.git)


### Inspiration
[python-packaging](http://python-packaging.readthedocs.io/en/latest/index.html)

