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
from zipfile import ZipFile
import json
import os
import random
from time import sleep

from selenium.common.exceptions import NoSuchElementException

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

        # remove zipped file from `test_pull_folder`
        if os.path.isfile(self.zipfilename):
            os.remove(self.zipfilename)

    def test_app_strings(self):
        strings = self.driver.app_strings()
        self.assertEqual(u'You can\'t wipe my data, you are a monkey!', strings[u'monkey_wipe_data'])

    def test_app_strings_with_language(self):
        strings = self.driver.app_strings("en")
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

    def test_pull_folder(self):
        string_data = 'random string data %d' % random.randint(0, 1000)
        path = '/data/local/tmp'
        self.driver.push_file(path + '/1.txt', string_data.encode('base64'))
        self.driver.push_file(path + '/2.txt', string_data.encode('base64'))
        folder = self.driver.pull_folder(path)

        # python doesn't have any functionality for unzipping streams
        # save temporary file, which will be deleted in `tearDown`
        self.zipfilename = 'folder_%d.zip' % random.randint(0, 1000000)
        file = open(self.zipfilename, "w")
        file.write(folder.decode('base64', 'strict'))
        file.close()

        with ZipFile(self.zipfilename, 'r') as myzip:
            # should find these. otherwise it will raise a `KeyError`
            myzip.read('1.txt')
            myzip.read('2.txt')

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

    def test_open_notifications(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("App")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Notification")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Status Bar")').click()

        self.driver.find_element_by_android_uiautomator('new UiSelector().text(":-|")').click()

        self.driver.open_notifications()
        sleep(1)
        self.assertRaises(NoSuchElementException, \
            self.driver.find_element_by_android_uiautomator, 'new UiSelector().text(":-|")')

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        # sometimes numbers shift
        title = False
        body = False
        for el in els:
            text = el.text
            if text == 'Mood ring':
                title = True
            elif text == 'I am ok':
                body = True
        self.assertTrue(title)
        self.assertTrue(body)

        self.driver.keyevent(4)
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text(":-|")')


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
