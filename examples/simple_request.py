from ok_api import OkApi


def main():
    """
        Простой запрос на примере метода friends.get с
        необязательным параметром типа сортировки
        (https://apiok.ru/dev/methods/rest/friends/friends.get)
    """

    ok = OkApi(access_token='OK_ACCESS_TOKEN',
               application_key='OK_APP_PUBLIC_TOKEN',
               application_secret_key='OK_APP_PRIVATE_TOKEN')

    response = ok.friends.get(sort_type='PRESENT')
    print(response.json())


if __name__ == '__main__':
    main()
