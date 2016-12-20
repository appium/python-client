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


class FindByIOSPredicateTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = desired_capabilities.get_desired_capabilities('UICatalog.app.zip')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_find_element_by_name(self):
        # Will throw exception if element is not found
        self.driver.find_element_by_ios_predicate('wdName == "Buttons"')

    def test_find_multiple_element_by_type(self):
        e = self.driver.find_elements_by_ios_predicate('wdType == "XCUIElementTypeStaticText"')
        self.assertNotEqual(len(e), 0)

    def test_find_element_by_label(self):
        # Will throw exception if element is not found
        self.driver.find_element_by_ios_predicate('label == "TextFields"')

    def test_find_element_by_value(self):
        # Will throw exception if element is not found
        self.driver.find_element_by_ios_predicate('wdValue == "Controls"')

    def test_find_element_by_isvisible(self):
        # Will throw exception if element is not found
        self.driver.find_element_by_ios_predicate('wdValue == "SearchBar" AND isWDVisible == 1')

        # Should not find any elements
        e = self.driver.find_elements_by_ios_predicate('wdValue == "SearchBar" AND isWDVisible == 0')
        self.assertEqual(len(e), 0)

    def test_find_element_by_isenabled(self):
        # Will throw exception if element is not found
        self.driver.find_element_by_ios_predicate('wdValue == "SearchBar" AND isWDEnabled == 1')

        # Should not find any elements
        e = self.driver.find_elements_by_ios_predicate('wdValue == "SearchBar" AND isWDEnabled == 0')
        self.assertEqual(len(e), 0)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(FindByIOSPredicateTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
