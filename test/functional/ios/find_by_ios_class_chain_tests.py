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

class FindByIOClassChainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = desired_capabilities.get_desired_capabilities('UICatalog.app.zip')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_find_element_by_path(self):
        el = self.driver.find_element_by_ios_class_chain('XCUIElementTypeWindow/**/XCUIElementTypeStaticText')
        self.assertEqual('UICatalog', el.get_attribute('name'))

    def test_find_multiple_elements_by_path(self):
        el = self.driver.find_elements_by_ios_class_chain('XCUIElementTypeWindow/*/*/*')
        self.assertEqual(6, len(el))
        self.assertEqual('UICatalog', el[0].get_attribute('name'))
        self.assertEqual(None, el[1].get_attribute('name'))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(FindByIOClassChainTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
