# Документация ok_api

**ok_api** - python библиотека для работы с API Одноклассников (API Wrapper ok.ru)

* ##### [OkApi (основной класс API)](./ok_api_doc.md)
* ##### [Upload](./upload_doc.md)

## Установка библиотеки
```
$ pip install ok_api
```

## Примеры использования

* [Простой запрос к API](../examples/simple_request.py)
* [Загрузка фото](../examples/photos_upload.py)
* [Загрузка видео](../examples/video_upload.py)

## Получение access_token, application_key, application_secret_key

Всю необходимую информацию можно найти здесь: https://apiok.ru/dev/app/group_app

Если кратко, то

* Получаем права разработчика здесь https://ok.ru/devaccess
* Создаем приложение и разрешаем OAuth авторизацию
* Необходимые ключи придут на почту, а токен получаем в настройках приложения
* Если нужны дополнительные [права приложения](https://apiok.ru/ext/oauth/permissions), то
связываемся с разработчиками по почте