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

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from .helper import desired_capabilities
from .helper.test_helper import BaseTestCase, wait_for_element


class WebelementTests(BaseTestCase):
    def test_element_location_in_view(self):
        el = self.driver.find_element_by_accessibility_id('Content')
        loc = el.location_in_view
        self.assertIsNotNone(loc['x'])
        self.assertIsNotNone(loc['y'])

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

        el = wait_for_element(self.driver, MobileBy.ID, 'com.example.android.apis:id/left_text_edit')
        el.send_keys(' text')

        self.assertEqual('Left is best text', el.text)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WebelementTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
