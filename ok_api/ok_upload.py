from .ok_api import OkApi
from .ok_exceptions import *


class Upload:
    """Загрузка файлов с помощью API"""

    def __init__(self, ok_api):
        """
        Parameters:
            ok_api (OkApi): Объект OkApi

        """
        if not isinstance(ok_api, OkApi):
            raise TypeError('The argument must be of type OkApi')
        self.__ok_api = ok_api

    def photo(self, photos, album='', group_id='', **kwargs):
        """Загрузка изображений

        Notes:
            - Данный метод может загружать множество изображений за раз

            - Возможно потребуется дополнительно вызвать метод photosV2.commit
            (https://apiok.ru/dev/methods/rest/photosV2/photosV2.commit)

        Parameters:
            photos (str, file-object or list): Путь к изображениям или file-like объекты
            album (str, optional): Id альбома, в который добавляется фото
            group_id (str, optional): Id группы, в которую добавляется фото
            **kwargs: Дополнительные именованые аргументы (https://apiok.ru/dev/methods/rest/photosV2/photosV2.getUploadUrl)

        Returns:
            JSON: Ответ сервера в виде JSON объекта

        """
        amount_photos = len(photos) if isinstance(photos, list) else 1

        params = {
            'count': amount_photos,
            'aid': album,
            'gid': group_id
        }
        params.update(kwargs)

        answer = self.__ok_api.photosV2.getUploadUrl(**params).json()
        upload_url = answer.get('upload_url', None)

        if not upload_url:
            raise UploadPhotoError(answer)

        with FileOpener(photos, content_type='image') as open_photos:
            req = self.__ok_api.http.post(upload_url, files=open_photos)

        return req.json()

    def video(self, video, file_name, **kwargs):
        """Загрузка видео

        Notes:
            - Данный метод загружает только одно видео за раз

            - После получения video_id необходимо дополнительно вызвать метод video.update
            для завершения иницированной процедуры загрузки видео
            (https://apiok.ru/dev/methods/rest/video/video.update)

        Parameters:
            video (str or file-object): Путь к видео или file-like объект
            file_name (str): Название загружаемого файла
            **kwargs: Дополнительные именованые аргументы (https://apiok.ru/dev/methods/rest/video/video.getUploadUrl)

        Returns:
            dict: Словарь с ключами upload_status и video_id

        """
        params = {
            'file_name': file_name,
            'file_size': 0
        }
        params.update(kwargs)

        answer = self.__ok_api.video.getUploadUrl(**params).json()
        upload_url = answer.get('upload_url', None)

        if not upload_url:
            raise UploadVideoError(answer)

        with FileOpener(video, content_type='video') as open_video:
            req = self.__ok_api.__http.post(upload_url, files=open_video)

        return {'upload_status': req.status_code, 'video_id': answer.get('video_id', None)}


class FileOpener:

    def __init__(self, files_, content_type):
        if not isinstance(files_, list):
            files_ = [files_]
        self.files = files_
        self.content_type = content_type
        self.opened_files = list()

    def __enter__(self):
        return self.open_files()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_files()

    def open_files(self):
        files = list()
        for i, file in enumerate(self.files):
            if hasattr(file, 'read'):
                temp_file = file
            else:
                temp_file = open(file, 'rb')
                self.opened_files.append(temp_file)
            files.append((f'{i}_{temp_file.name}', (temp_file.name, temp_file, self.content_type)))
        return files

    def close_files(self):
        for file in self.opened_files:
            file.close()
        self.opened_files.clear()
