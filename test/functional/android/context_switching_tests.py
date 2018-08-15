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


class ContextSwitchingTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('selendroid-test-app.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_contexts_list(self):
        self._enter_webview()
        contexts = self.driver.contexts
        self.assertEqual(2, len(contexts))

    def test_move_to_correct_context(self):
        self._enter_webview()
        self.assertEqual('WEBVIEW_io.selendroid.testapp', self.driver.current_context)

    def test_actually_in_webview(self):
        self._enter_webview()
        self.driver.find_element_by_css_selector('input[type=submit]').click()
        el = self.driver.find_element_by_xpath("//h1[contains(., 'This is my way')]")
        self.assertIsNot(None, el)

    def test_move_back_to_native_context(self):
        self._enter_webview()
        self.driver.switch_to.context(None)
        self.assertEqual('NATIVE_APP', self.driver.current_context)

    def test_set_invalid_context(self):
        self.assertRaises(NoSuchContextException, self.driver.switch_to.context, 'invalid name')

    def tearDown(self):
        self.driver.quit()

    def _enter_webview(self):
        btn = self.driver.find_element_by_name('buttonStartWebviewCD')
        btn.click()
        self.driver.switch_to.context('WEBVIEW')


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ContextSwitchingTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
