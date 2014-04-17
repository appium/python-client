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

from appium import webdriver

import desired_capabilities

import unittest
import time
from time import sleep

class AppiumTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('UICatalog.app.zip')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_lock(self):
        el = self.driver.find_element_by_id('ButtonsExplain')
        self.assertIsNotNone(el)
        self.driver.lock(1)
        try:
            self.driver.find_element_by_id('ButtonsExplain')
        except Exception as e:
            pass # we should not be able to find this anymore
        sleep(5)
        el = self.driver.find_element_by_id('ButtonsExplain')
        self.assertIsNotNone(el)

    def test_shake(self):
        # what can we assert about this?
        self.driver.shake()


if __name__ == "__main__":
    unittest.main()
