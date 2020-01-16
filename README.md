[![Build Status](https://travis-ci.org/Apkawa/pytest-ngrok.svg?branch=master)](https://travis-ci.org/Apkawa/pytest-ngrok)
[![codecov](https://codecov.io/gh/Apkawa/pytest-ngrok/branch/master/graph/badge.svg)](https://codecov.io/gh/Apkawa/pytest-ngrok)
[![Requirements Status](https://requires.io/github/Apkawa/pytest-ngrok/requirements.svg?branch=master)](https://requires.io/github/Apkawa/pytest-ngrok/requirements/?branch=master)
[![PyUP](https://pyup.io/repos/github/Apkawa/pytest-ngrok/shield.svg)](https://pyup.io/repos/github/Apkawa/pytest-ngrok)
[![PyPI](https://img.shields.io/pypi/pyversions/pytest-ngrok.svg)]()

Template repository for django-app.
After create find and replace 
* `pytest-ngrok` to new repository name
* `pytest_ngrok` to new app package name

# Installation

```bash
pip install pytest-ngrok

```

or from git

```bash
pip install -e git+https://githib.com/Apkawa/pytest-ngrok.git#egg=pytest-ngrok
```

## Django and python version

| Python<br/>Django |        3.5         |      3.6           |      3.7           |       3.8          |
|:-----------------:|--------------------|--------------------|--------------------|--------------------|
| 1.8               |       :x:          |      :x:           |       :x:          |      :x:           |
| 1.11              | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |      :x:           |
| 2.2               | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| 3.0               |       :x:          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |


# Usage



# Contributing

## run example app

```bash
pip install -r requirements.txt
./test/manage.py migrate
./test/manage.py runserver
```

## run tests

```bash
pip install -r requirements.txt
pytest
tox
```

## Update version

```bash
python setup.py bumpversion
```

## publish pypi

```bash
python setup.py publish
```






