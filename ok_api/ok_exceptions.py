class OkApiException(Exception):
    pass


class ApiError(OkApiException):

    def __init__(self, message):
        self.message = message


class OkUploadException(OkApiException):
    pass


class UploadPhotoError(OkUploadException):

    def __init__(self, message):
        self.message = message


class UploadVideoError(OkUploadException):

    def __init__(self, message):
        self.message = message