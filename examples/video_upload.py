from ok_api import OkApi, Upload


def main():
    """
    Пример загрузки видео с помощью модуля Upload и завершения
    загрузки методом video.update (https://apiok.ru/dev/methods/rest/video/video.update)
    """

    ok = OkApi(access_token='OK_ACCESS_TOKEN',
               application_key='OK_APP_PUBLIC_TOKEN',
               application_secret_key='OK_APP_PRIVATE_TOKEN')

    upload = Upload(ok)
    upload_response = upload.video(video='video.mp4', file_name='video')

    response = ok.video.update(vid=upload_response['video_id'], title='VideoTitle')
    print(response.content)


if __name__ == '__main__':
    main()
