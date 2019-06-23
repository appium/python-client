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

from .helper import desired_capabilities


class FindByElementWebelementTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        desired_caps = desired_capabilities.get_desired_capabilities('UICatalog.app.zip')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_find_element_by_path(self):
        el = self.driver.find_element_by_ios_predicate('wdName == "UICatalog"')
        self.assertEqual('UICatalog', el.get_attribute('name'))

        c_el = el.find_elements_by_ios_predicate('label == "Action Sheets"')
        self.assertEqual('Action Sheets', c_el[0].get_attribute('name'))

        c_el = el.find_elements_by_ios_class_chain('**/XCUIElementTypeStaticText')
        self.assertEqual('Action Sheets', c_el[0].get_attribute('name'))

        c_el = el.find_elements_by_accessibility_id('UICatalog')
        self.assertEqual('UICatalog', c_el[0].get_attribute('name'))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FindByElementWebelementTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
