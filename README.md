# ok_api
**ok_api** - python библиотека для работы с API Одноклассников (API Wrapper ok.ru)

## Простой пример

```python
from ok_api import OkApi

ok = OkApi(access_token='token', 
           application_key='key', 
           application_secret_key='secret')

print(ok.friends.get())
```
