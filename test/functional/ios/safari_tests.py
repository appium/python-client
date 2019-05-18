#!/usr/bin/env python

import unittest

from appium import webdriver


class SafariTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'browserName': 'safari',
            'platformName': 'iOS',
            'platformVersion': '12.2',
            'deviceName': 'iPhone Simulator',
            'nativeWebTap': True,
            'safariIgnoreFraudWarning': True,
            'automationName': 'XCUITest'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_context(self):
        self.assertEqual('NATIVE_APP', self.driver.contexts[0])
        self.assertTrue(self.driver.contexts[1].startswith('WEBVIEW_'))
        self.assertTrue('WEBVIEW_' in self.driver.current_context)

    def test_get(self):
        self.driver.get("http://google.com")
        self.assertEqual('Google', self.driver.title)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SafariTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
