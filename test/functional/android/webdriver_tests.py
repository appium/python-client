#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from appium.webdriver.common.mobileby import MobileBy

from .helper.test_helper import BaseTestCase, is_ci, wait_for_element


class WebdriverTests(BaseTestCase):

    def test_current_package(self):
        package = self.driver.current_package
        self.assertEqual('com.example.android.apis', package)

    def test_end_test_coverage(self):
        self.skipTest('Not sure how to set this up to run')
        self.driver.end_test_coverage(intent='android.intent.action.MAIN', path='')
        sleep(5)

    def test_reset(self):
        self.driver.reset()
        self.assertTrue(self.driver.is_app_installed('com.example.android.apis'))

    def test_open_notifications(self):
        if is_ci():
            # TODO Due to unexpected dialog, "System UI isn't responding"
            self.skipTest('Need to fix flaky test during running on CI.')
        for word in ['App', 'Notification', 'Status Bar', ':-|']:
            wait_for_element(self.driver, MobileBy.ANDROID_UIAUTOMATOR,
                             'new UiSelector().text("{}")'.format(word)).click()

        self.driver.open_notifications()
        sleep(1)
        self.assertRaises(NoSuchElementException,
                          self.driver.find_element_by_android_uiautomator, 'new UiSelector().text(":-|")')

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        # sometimes numbers shift
        title = False
        body = False
        for el in els:
            text = el.text
            if text == 'Mood ring':
                title = True
            elif text == 'I am ok':
                body = True
        self.assertTrue(title)
        self.assertTrue(body)

        self.driver.keyevent(4)
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text(":-|")')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WebdriverTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
