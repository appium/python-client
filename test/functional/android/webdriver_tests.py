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

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from .helper import desired_capabilities
from .helper.test_helper import wait_for_element


class WebdriverTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

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
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("App")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Notification")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Status Bar")').click()

        self.driver.find_element_by_android_uiautomator('new UiSelector().text(":-|")').click()

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

    def test_set_text(self):
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Views").instance(0));').click()

        wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Controls').click()
        wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, '1. Light Theme').click()

        el = wait_for_element(self.driver, MobileBy.CLASS_NAME, 'android.widget.EditText')
        el.send_keys('original text')
        el.set_text('new text')

        self.assertEqual('new text', el.text)

    def test_send_keys(self):
        for text in ['App', 'Activity', 'Custom Title']:
            wait_for_element(self.driver, MobileBy.XPATH,
                             "//android.widget.TextView[@text='{}']".format(text)).click()

        el = self.driver.find_element(MobileBy.ID, 'com.example.android.apis:id/left_text_edit')
        el.send_keys(' text')

        self.assertEqual('Left is best text', el.text)

    def test_element_location_in_view(self):
        el = self.driver.find_element_by_accessibility_id('Content')
        loc = el.location_in_view
        self.assertIsNotNone(loc['x'])
        self.assertIsNotNone(loc['y'])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WebdriverTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
