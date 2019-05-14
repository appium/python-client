#!/usr/bin/env python

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
import desired_capabilities


class FindByUIAutomatorTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_find_single_element(self):
        el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Animation")')
        self.assertIsNotNone(el)

    def test_find_multiple_elements(self):
        els = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
        self.assertIsInstance(els, list)

    def test_element_find_single_element(self):
        el = self.driver.find_element_by_class_name('android.widget.ListView')

        sub_el = el.find_element_by_android_uiautomator('new UiSelector().description("Animation")')
        self.assertIsNotNone(sub_el)

    def test_element_find_multiple_elements(self):
        el = self.driver.find_element_by_class_name('android.widget.ListView')

        sub_els = el.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
        self.assertIsInstance(sub_els, list)

    def test_scroll_into_view(self):
        el = self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Views").instance(0));')
        el.click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FindByUIAutomatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
