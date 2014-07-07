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
from appium.common.exceptions import NoSuchContextException
import desired_capabilities
from time import sleep

from selenium.webdriver.common.touch_actions import TouchActions


class SelendroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        desired_caps['automationName'] = 'Selendroid'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_contexts_list(self):
        el = self.driver.find_element_by_class_name('android.widget.ListView')
        els = el.find_elements_by_class_name('android.widget.TextView')

        ta = TouchActions(self.driver).flick_element(el, 0, -300, 0)
        ta.perform()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def _enter_webview(self):
        btn = self.driver.find_element_by_name('buttonStartWebviewCD')
        btn.click()
        self.driver.switch_to.context('WEBVIEW')


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SelendroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
