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
from test.functional.android.helper import desired_capabilities


class HwActionsTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_lock(self):
        self.driver.lock(-1)
        try:
            self.assertTrue(self.driver.is_locked())
        finally:
            self.driver.unlock()
        self.assertFalse(self.driver.is_locked())


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HwActionsTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
