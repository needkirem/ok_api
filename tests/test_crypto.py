import unittest

from ok_api import OkApi


class CryptoTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(CryptoTestCase, self).__init__(*args, **kwargs)
        self.ok = OkApi(access_token='token', application_key='key', application_secret_key='secret')

    def test_session_secret_key(self):
        self.assertEqual(self.ok._OkApi__get_session_secret_key, '1b0ebffcd35423aa7674c8cbb60581e4')

    def test_signature(self):
        self.assertEqual(self.ok._OkApi__signature({'key': 'value'}), '08948becfe27ee5d869ed76e2fffbae8')
