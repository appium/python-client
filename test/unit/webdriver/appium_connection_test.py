import unittest
from urllib import parse

from appium.webdriver import appium_connection


class AppiumConnectionTest(unittest.TestCase):
    def test_get_remote_connection_headers(self):
        headers = appium_connection.AppiumConnection.get_remote_connection_headers(
            parse.urlparse('http://http://127.0.0.1:4723/session')
        )
        self.assertIsNotNone(headers.get('X-Idempotency-Key'))

        headers = appium_connection.AppiumConnection.get_remote_connection_headers(
            parse.urlparse('http://http://127.0.0.1:4723/session/session_id')
        )
        self.assertIsNone(headers.get('X-Idempotency-Key'))

        appium_connection.AppiumConnection.extra_headers = {'custom': 'header'}

        headers = appium_connection.AppiumConnection.get_remote_connection_headers(
            parse.urlparse('http://http://127.0.0.1:4723/session')
        )
        self.assertIsNotNone(headers.get('X-Idempotency-Key'))
        self.assertEqual(headers.get('custom'), 'header')

        headers = appium_connection.AppiumConnection.get_remote_connection_headers(
            parse.urlparse('http://http://127.0.0.1:4723/session/session_id')
        )
        self.assertIsNone(headers.get('X-Idempotency-Key'))
        self.assertEqual(headers.get('custom'), 'header')

    def test_remove_headers_case_insensitive(self):
        for h in ['X-Idempotency-Key', 'X-idempotency-Key', 'x-idempotency-key']:
            appium_connection.AppiumConnection.extra_headers = {h: 'value'}
            appium_connection.AppiumConnection.get_remote_connection_headers(
                parse.urlparse('http://http://127.0.0.1:4723/session/session_id')
            )
            self.assertEqual(appium_connection.AppiumConnection.extra_headers, {})
