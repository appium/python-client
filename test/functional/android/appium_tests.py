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
import json
from time import sleep

from appium import webdriver
import desired_capabilities


# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 1


class AppiumTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_app_strings(self):
        strings = self.driver.app_strings
        self.assertEqual(u'You can\'t wipe my data, you are a monkey!', strings[u'monkey_wipe_data'])

    def test_press_keycode(self):
        # not sure how to test this.
        self.driver.press_keycode(176)

    def test_long_press_keycode(self):
        # not sure how to test this.
        self.driver.long_press_keycode(176)

    def test_current_activity(self):
        activity = self.driver.current_activity
        self.assertEqual('.ApiDemos', activity)

    def test_set_value(self):
        el = self.driver.find_element_by_class_name('android.widget.ListView')
        js_params = {'element': el.id, 'text': "Views"}
        self.driver.execute_script("mobile: scrollTo", js_params)

        el = self.driver.find_element_by_name('Views')
        el.click()

        el = self.driver.find_element_by_name('Auto Complete')
        el.click()

        el = self.driver.find_element_by_name('4. Contacts')
        el.click()

        el = self.driver.find_element_by_class_name('android.widget.EditText')
        self.driver.set_value(el, 'Isaac')

        text = el.get_attribute('text')
        self.assertEqual('Isaac', text)

    def test_element_set_value(self):
        el = self.driver.find_element_by_class_name('android.widget.ListView')
        js_params = {'element': el.id, 'text': "Views"}
        self.driver.execute_script("mobile: scrollTo", js_params)

        el = self.driver.find_element_by_name('Views')
        el.click()

        el = self.driver.find_element_by_name('Auto Complete')
        el.click()

        el = self.driver.find_element_by_name('4. Contacts')
        el.click()
        sleep(SLEEPY_TIME)

        el = self.driver.find_element_by_class_name('android.widget.EditText')
        el.set_value('Isaac')

        text = el.get_attribute('text')
        self.assertEqual('Isaac', text)

    def test_pull_file(self):
        data = self.driver.pull_file('data/local/tmp/strings.json')
        strings = json.loads(data.decode('base64', 'strict'))
        self.assertEqual('You can\'t wipe my data, you are a monkey!', strings[u'monkey_wipe_data'])

    def test_push_file(self):
        path = 'data/local/tmp/test_push_file.txt'
        data = 'This is the contents of the file to push to the device.'
        self.driver.push_file(path, data.encode('base64'))
        data_ret = self.driver.pull_file('data/local/tmp/test_push_file.txt').decode('base64')
        self.assertEqual(data, data_ret)

    def test_complex_find(self):
        # this only works with a three dimensional array like here.
        el = self.driver.complex_find([[[2, 'Ani']]])
        self.assertIsNotNone(el)

    def test_background_app(self):
        self.driver.background_app(1)
        sleep(5)
        el = self.driver.find_element_by_name('Animation')
        self.assertIsNotNone(el)

    def test_is_app_installed(self):
        self.assertFalse(self.driver.is_app_installed('sdfsdf'))
        self.assertTrue(self.driver.is_app_installed('com.example.android.apis'))

    def test_install_app(self):
        self.skipTest('This causes the server to crash. no idea why')
        self.assertFalse(self.driver.is_app_installed('io.selendroid.testapp'))
        self.driver.install_app('/Users/isaac/code/python-client/test/apps/selendroid-test-app.apk')
        self.assertTrue(self.driver.is_app_installed('io.selendroid.testapp'))

    def test_remove_app(self):
        self.assertTrue(self.driver.is_app_installed('com.example.android.apis'))
        self.driver.remove_app('com.example.android.apis')
        self.assertFalse(self.driver.is_app_installed('com.example.android.apis'))

    def test_close__and_launch_app(self):
        el = self.driver.find_element_by_name('Animation')
        self.assertIsNotNone(el)

        self.driver.close_app()
        self.driver.launch_app()

        el = self.driver.find_element_by_name('Animation')
        self.assertIsNotNone(el)

    def test_end_test_coverage(self):
        self.skipTest('Not sure how to set this up to run')
        self.driver.end_test_coverage(intent='android.intent.action.MAIN', path='')
        sleep(5)

    def test_reset(self):
        el = self.driver.find_element_by_name('App')
        el.click()

        self.driver.reset()
        sleep(5)

        el = self.driver.find_element_by_name('App')
        self.assertIsNotNone(el)


if __name__ == "__main__":
    unittest.main()
