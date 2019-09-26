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

from .helper.desired_capabilities import get_desired_capabilities


class SafariTests(unittest.TestCase):
    def setUp(self):
        desired_caps = get_desired_capabilities()
        desired_caps.update({
            'browserName': 'safari',
            'nativeWebTap': True,
            'safariIgnoreFraudWarning': True
        })

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_context(self):
        self.assertEqual('NATIVE_APP', self.driver.contexts[0])
        self.assertTrue(self.driver.contexts[1].startswith('WEBVIEW_'))
        self.assertTrue('WEBVIEW_' in self.driver.current_context)

    def test_get(self):
        self.driver.get("http://google.com")
        self.assertEqual('Google', self.driver.title)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SafariTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
