from ok_api import OkApi, Upload


def main():
    """
    Пример загрузки фотографий с помощтю модуля Upload и завершения
    загрузки методом photosV2.commit (https://apiok.ru/dev/methods/rest/photosV2/photosV2.commit)
    """

    ok = OkApi(access_token='OK_ACCESS_TOKEN',
               application_key='OK_APP_PUBLIC_TOKEN',
               application_secret_key='OK_APP_PRIVATE_TOKEN')

    upload = Upload(ok)
    upload_response = upload.photo(photos=['img_1.jpg', 'img_2.jpg'])

    for photo_id in upload_response['photos']:
        token = upload_response['photos'][photo_id]['token']
        response = ok.photosV2.commit(photo_id=photo_id, token=token)
        print(response.json())


if __name__ == '__main__':
    main()
