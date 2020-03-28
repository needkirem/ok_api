from hashlib import md5
import requests
from .ok_exceptions import *


class OkApi:
    """Основной класс для работы с REST API OK"""

    def __init__(self, access_token, application_key, application_secret_key):
        """
        Parameters:
            access_token (str): Токен доступа
            application_key (str): Публичный ключ приложения
            application_secret_key (str): Секретный ключ приложения

        """
        self.__API_URL = 'https://api.ok.ru/fb.do'
        self.__access_token = access_token
        self.__application_key = application_key
        self.__application_secret_key = application_secret_key
        self.__methods = None

    @property
    def http(self):
        return requests.Session()

    @property
    def __get_session_secret_key(self):
        return md5('{}{}'.format(self.__access_token,
                                 self.__application_secret_key).encode('utf-8')).hexdigest().lower()

    def __signature(self, params):
        params = ''.join(['{}={}'.format(key, params[key]) for key in sorted(params.keys())])
        return md5('{}{}'.format(params, self.__get_session_secret_key).encode('utf-8')).hexdigest().lower()

    def __getattr__(self, item):
        ok_api = OkApi(access_token=self.__access_token,
                       application_key=self.__application_key,
                       application_secret_key=self.__application_secret_key)
        ok_api.__methods = self.__methods + '.' + item if self.__methods else item
        return ok_api

    def __call__(self, *args, **kwargs):
        return self.__method(args, kwargs)

    def __method(self, args, kwargs):
        params = {
            'application_key': self.__application_key,
            'method': self.__methods
        }
        params.update(kwargs)
        params['sig'] = self.__signature(params)
        params['access_token'] = self.__access_token
        return self.__request(params)

    def __request(self, params):
        req = self.http.post(self.__API_URL, data=params, timeout=30)
        if not req:
            raise ApiError(req.text)
        return req
