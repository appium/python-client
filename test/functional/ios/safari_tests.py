#!/usr/bin/env python

import unittest
from time import sleep


from appium import webdriver


class SafariTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'browserName': 'safari',
            'platformName': 'iOS',
            'platformVersion': '7.1',
            'deviceName': 'iPhone Simulator',
            'nativeWebTap': True,
            'safariIgnoreFraudWarning': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_context(self):
        self.assertEqual([u'NATIVE_APP', u'WEBVIEW_1'], self.driver.contexts)
        self.assertEqual('WEBVIEW_1', self.driver.current_context)

    def test_get(self):
        self.driver.get("http://google.com")
        self.assertEqual('Google', self.driver.title)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SafariTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
