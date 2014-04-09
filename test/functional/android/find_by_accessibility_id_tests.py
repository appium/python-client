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

import os
from time import sleep

from appium import webdriver

import unittest

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class FindByAccessibilityIDTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['device'] = 'Android'
        desired_caps['browserName'] = ''
        desired_caps['version'] = '4.2'
        desired_caps['app'] = PATH('../../apps/ApiDemos-debug.apk')
        desired_caps['app-package'] = 'com.example.android.apis'
        desired_caps['app-activity'] = '.ApiDemos'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_find_single_element(self):
        el = self.driver.find_element_by_accessibility_id('Animation')
        self.assertIsNotNone(el)

    def test_find_multiple_elements(self):
        els = self.driver.find_elements_by_accessibility_id('Animation')
        self.assertIsInstance(els, list)

if __name__ == "__main__":
    unittest.main()
