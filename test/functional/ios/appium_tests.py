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

from webdriver.applicationstate import ApplicationState
from appium import webdriver
import desired_capabilities


class AppiumTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('UICatalog.app.zip')
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

    def test_screen_record(self):
        self.driver.start_recording_screen()
        sleep(5)
        result = self.driver.stop_recording_screen()
        self.assertTrue(len(result) > 0)

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

    def test_shake(self):
        # what can we assert about this?
        self.driver.shake()

    def test_touch_id(self):
        # nothing to assert, just verify that it doesn't blow up
        self.driver.touch_id(True)
        self.driver.touch_id(False)

    def test_toggle_touch_id_enrollment(self):
        # nothing to assert, just verify that it doesn't blow up
        self.driver.toggle_touch_id_enrollment()

    def test_hide_keyboard(self):
        el = self.driver.find_element_by_name('Uses of UITextField')
        el.click()

        # get focus on text field, so keyboard comes up
        el = self.driver.find_element_by_class_name('UIATextField')
        el.set_value('Testing')

        el = self.driver.find_element_by_class_name('UIAKeyboard')
        self.assertTrue(el.is_displayed())

        self.driver.hide_keyboard(key_name='Done')

        self.assertFalse(el.is_displayed())

    def test_hide_keyboard_presskey_strategy(self):
        el = self.driver.find_element_by_name('Uses of UITextField')
        el.click()

        # get focus on text field, so keyboard comes up
        el = self.driver.find_element_by_class_name('UIATextField')
        el.set_value('Testing')

        el = self.driver.find_element_by_class_name('UIAKeyboard')
        self.assertTrue(el.is_displayed())

        self.driver.hide_keyboard(strategy='pressKey', key='Done')

        self.assertFalse(el.is_displayed())

    def test_hide_keyboard_no_key_name(self):
        el = self.driver.find_element_by_name('Uses of UITextField')
        el.click()

        # get focus on text field, so keyboard comes up
        el = self.driver.find_element_by_class_name('UIATextField')
        el.set_value('Testing')

        el = self.driver.find_element_by_class_name('UIAKeyboard')
        self.assertTrue(el.is_displayed())

        self.driver.hide_keyboard()
        sleep(10)

        # currently fails.
        self.assertFalse(el.is_displayed())

    def test_clear(self):
        # Click text fields
        self.driver.find_element_by_accessibility_id('TextFields').click()

        # Verify default text
        def_text = '<enter text>'
        text = self.driver.find_element_by_accessibility_id('Normal').get_attribute('value')
        self.assertEqual(text, def_text)

        # Input some text, verify
        input_text = 'blah'
        self.driver.find_element_by_accessibility_id('Normal').send_keys(input_text)
        text = self.driver.find_element_by_accessibility_id('Normal').get_attribute('value')
        self.assertEqual(text, input_text)

        # Clear text, verify
        self.driver.find_element_by_accessibility_id('Normal').clear()
        text = self.driver.find_element_by_accessibility_id('Normal').get_attribute('value')
        self.assertEqual(text, def_text)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
