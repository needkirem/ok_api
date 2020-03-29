# ok_api [![PyPI](https://img.shields.io/pypi/v/ok-api?style=flat-square)](https://pypi.org/project/ok-api/) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ok-api?style=flat-square)

**ok_api** - python библиотека для работы с API Одноклассников (API Wrapper ok.ru)

## Установка
```
$ pip install ok_api
```

## Простой пример

```python
from ok_api import OkApi

ok = OkApi(access_token='token', 
           application_key='key', 
           application_secret_key='secret')

print(ok.friends.get())
```
