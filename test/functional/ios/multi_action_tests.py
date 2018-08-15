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
from time import sleep

from appium import webdriver
import desired_capabilities


class MultiActionTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('TestApp.app.zip')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    # this test does not assert anything.
    # it has to be watched in order to see if it works
    def test_driver_pinch_zoom(self):
        els = self.driver.find_elements_by_class_name('UIAButton')
        els[5].click()

        sleep(1)
        el = self.driver.find_element_by_name('OK')
        el.click()

        sleep(1)
        el = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAMapView[1]')
        self.driver.zoom(el)

        sleep(5)
        self.driver.pinch(el)
        sleep(5)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MultiActionTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
