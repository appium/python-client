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

from .helper.test_helper import BaseTestCase

ANDROID_LATIN = 'com.android.inputmethod.latin/.LatinIME'  # Android L/M/N
GOOGLE_LATIN = 'com.google.android.inputmethod.latin/com.android.inputmethod.latin.LatinIME'  # Android O/P


class IMETests(BaseTestCase):
    def test_available_ime_engines(self):
        engines = self.driver.available_ime_engines
        self.assertIsInstance(engines, list)
        self.assertTrue(ANDROID_LATIN in engines or GOOGLE_LATIN in engines)

    def test_is_ime_active(self):
        self.assertTrue(self.driver.is_ime_active())

    def test_active_ime_engine(self):
        engines = self.driver.available_ime_engines
        self.assertTrue(self.driver.active_ime_engine in engines)

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


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(IMETests)
    unittest.TextTestRunner(verbosity=2).run(suite)
