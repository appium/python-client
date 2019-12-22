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

from selenium.webdriver.support.ui import WebDriverWait

from appium import webdriver
from appium.webdriver.applicationstate import ApplicationState
from test.functional.ios.helper.test_helper import BaseTestCase
from test.functional.test_helper import get_available_from_port_range

from ..test_helper import is_ci
from .helper import desired_capabilities


class WebDriverTests(BaseTestCase):

    def test_all_sessions(self):
        if is_ci():
            # TODO Due to not created 2nd session somehow
            self.skipTest('Need to fix flaky test during running on CI.')
        port = get_available_from_port_range(8200, 8300)
        desired_caps = desired_capabilities.get_desired_capabilities('UICatalog.app.zip')
        desired_caps['deviceName'] = 'iPhone Xs Max'
        desired_caps['wdaLocalPort'] = port

        class session_counts_is_two(object):
            TIMEOUT = 10

            def __call__(self, driver):
                return len(driver.all_sessions) == 2

        driver2 = None
        try:
            driver2 = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            WebDriverWait(
                driver2, session_counts_is_two.TIMEOUT).until(session_counts_is_two())
            self.assertEqual(2, len(self.driver.all_sessions))
        finally:
            if driver2 is not None:
                driver2.quit()

    def test_app_management(self):
        # this only works in Xcode9+
        if float(desired_capabilities.get_desired_capabilities(
                desired_capabilities.BUNDLE_ID)['platformVersion']) < 11:
            return
        self.assertEqual(self.driver.query_app_state(desired_capabilities.BUNDLE_ID),
                         ApplicationState.RUNNING_IN_FOREGROUND)
        self.driver.background_app(-1)
        self.assertTrue(self.driver.query_app_state(desired_capabilities.BUNDLE_ID) <
                        ApplicationState.RUNNING_IN_FOREGROUND)
        self.driver.activate_app(desired_capabilities.BUNDLE_ID)
        self.assertEqual(self.driver.query_app_state(desired_capabilities.BUNDLE_ID),
                         ApplicationState.RUNNING_IN_FOREGROUND)

    def test_clear(self):
        self._move_to_textbox()

        el = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]

        # Verify default text
        def_text = 'Placeholder text'
        text = el.get_attribute('value')
        self.assertEqual(text, def_text)

        # Input some text, verify
        input_text = 'blah'
        el.click()
        el.send_keys(input_text)
        # TODO Needs to get the element again to update value in the element. Remove below one line when it's fixed.
        el = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]
        text = el.get_attribute('value')
        self.assertEqual(text, input_text)

        # Clear text, verify
        el.clear()
        text = el.get_attribute('value')
        self.assertEqual(text, def_text)

    def test_press_button(self):
        self.driver.press_button("Home")
        if float(desired_capabilities.get_desired_capabilities(
                desired_capabilities.BUNDLE_ID)['platformVersion']) < 11:
            return
        self.assertEqual(self.driver.query_app_state(desired_capabilities.BUNDLE_ID),
                         ApplicationState.RUNNING_IN_FOREGROUND)

    def _move_to_textbox(self):
        el1 = self.driver.find_element_by_accessibility_id('Sliders')
        el2 = self.driver.find_element_by_accessibility_id('Buttons')
        self.driver.scroll(el1, el2)

        # Click text fields
        self.driver.find_element_by_accessibility_id('Text Fields').click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WebDriverTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
