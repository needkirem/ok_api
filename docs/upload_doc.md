# Upload

*class **Upload**(ok_api)*

Модуль упрощенной загрузки файлов

*Parameters:*

* ok_api (OkApi): Объект OkApi

---

### Методы

_**photo**(photos, album='', group_id='', **kwargs)_

*Загрузка изображений*

*Parameters:*

* photos (str, file-object or list): Путь к изображению(ям) или file-like объект(ы)
* album (str, optional): Id альбома, в который добавляется фото
* group_id (str, optional): Id группы, в которую добавляется фото
* **kwargs: Дополнительные именованые аргументы (https://apiok.ru/dev/methods/rest/photosV2/photosV2.getUploadUrl)

*Returns:*

* JSON: Ответ сервера в виде JSON объекта

*Notes:*

* Данный метод может загружать множество изображений за раз
* Для размещения изображения на странице пользователя необходимо дополнительно вызвать метод photosV2.commit

---

_**video**(video, file_name, **kwargs)_

*Загрузка видео*

*Parameters:*

* video (str or file-object): Путь к видео или file-like объект
* file_name (str): Название загружаемого файла
* **kwargs: Дополнительные именованые аргументы (https://apiok.ru/dev/methods/rest/video/video.getUploadUrl)

*Returns:*

* dict: Словарь с ключами upload_status и video_id

*Notes:*

* Данный метод загружает только одно видео за раз
* После получения video_id необходимо дополнительно вызвать метод video.update для завершения иницированной процедуры
 загрузки видео (https://apiok.ru/dev/methods/rest/video/video.update)