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
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from appium import webdriver
import desired_capabilities


# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 1

LATIN_IME = u'com.android.inputmethod.latin/.LatinIME'


class IMETests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()


    def test_available_ime_engines(self):
        engines = self.driver.available_ime_engines
        self.assertIsInstance(engines, list)
        self.assertTrue(LATIN_IME in engines)

    def test_is_ime_active(self):
        self.assertTrue(self.driver.is_ime_active())

    def test_active_ime_engine(self):
        self.assertIsInstance(self.driver.active_ime_engine, unicode)

    def test_activate_ime_engine(self):
        engines = self.driver.available_ime_engines
        active_engine = self.driver.active_ime_engine

        self.driver.activate_ime_engine(engines[-1])
        self.assertEqual(self.driver.active_ime_engine, engines[-1])

    def test_deactivate_ime_engine(self):
        engines = self.driver.available_ime_engines
        self.driver.activate_ime_engine(engines[-1])

        self.assertEqual(self.driver.active_ime_engine, engines[-1])

        self.driver.deactivate_ime_engine()
        sleep(1)
        self.assertNotEqual(self.driver.active_ime_engine, engines[-1])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(IMETests)
    unittest.TextTestRunner(verbosity=2).run(suite)
