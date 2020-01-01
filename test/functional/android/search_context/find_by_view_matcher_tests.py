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
import unittest

from appium import webdriver
from test.functional.android.helper.test_helper import (
    desired_capabilities,
    is_ci
)


class FindByViewMatcherTests(unittest.TestCase):

    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk.zip')
        desired_caps['automationName'] = 'Espresso'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        if is_ci():
            # Take the screenshot to investigate when tests failed only on CI
            img_path = os.path.join(os.getcwd(), self._testMethodName + '.png')
            self.driver.get_screenshot_as_file(img_path)
        self.driver.quit()

    def test_find_single_element(self):
        els = self.driver.find_elements_by_android_view_matcher(name='hasEntry', args=['title', 'Animation'])
        assert len(els) == 1


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FindByViewMatcherTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
