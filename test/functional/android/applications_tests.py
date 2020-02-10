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

import os
import unittest
from time import sleep

from appium.webdriver.applicationstate import ApplicationState

from .helper.desired_capabilities import PATH
from .helper.test_helper import APIDEMO_PKG_NAME, BaseTestCase


class ApplicationsTests(BaseTestCase):

    def test_background_app(self):
        self.driver.background_app(1)
        sleep(3)
        self.driver.launch_app()

    def test_is_app_installed(self):
        self.assertFalse(self.driver.is_app_installed('sdfsdf'))
        self.assertTrue(self.driver.is_app_installed(APIDEMO_PKG_NAME))

    def test_install_app(self):
        self.assertFalse(self.driver.is_app_installed('io.selendroid.testapp'))
        self.driver.install_app(PATH(os.path.join('../..', 'apps', 'selendroid-test-app.apk')))
        self.assertTrue(self.driver.is_app_installed('io.selendroid.testapp'))

    def test_remove_app(self):
        self.assertTrue(self.driver.is_app_installed(APIDEMO_PKG_NAME))
        self.driver.remove_app(APIDEMO_PKG_NAME)
        self.assertFalse(self.driver.is_app_installed(APIDEMO_PKG_NAME))

    def test_close_and_launch_app(self):
        self.driver.close_app()
        self.driver.launch_app()
        activity = self.driver.current_activity
        self.assertEqual('.ApiDemos', activity)

    def test_app_management(self):
        app_id = self.driver.current_package
        self.assertEqual(self.driver.query_app_state(app_id),
                         ApplicationState.RUNNING_IN_FOREGROUND)
        self.driver.background_app(-1)
        self.assertTrue(self.driver.query_app_state(app_id) <
                        ApplicationState.RUNNING_IN_FOREGROUND)
        self.driver.activate_app(app_id)
        self.assertEqual(self.driver.query_app_state(app_id),
                         ApplicationState.RUNNING_IN_FOREGROUND)

    def test_app_strings(self):
        strings = self.driver.app_strings()
        self.assertEqual(u'You can\'t wipe my data, you are a monkey!', strings[u'monkey_wipe_data'])

    def test_app_strings_with_language(self):
        strings = self.driver.app_strings('en')
        self.assertEqual(u'You can\'t wipe my data, you are a monkey!', strings[u'monkey_wipe_data'])

    def test_app_strings_with_language_and_file(self):
        strings = self.driver.app_strings('en', 'some_file')
        self.assertEqual(u'You can\'t wipe my data, you are a monkey!', strings[u'monkey_wipe_data'])

    def test_reset(self):
        self.driver.reset()
        self.assertTrue(self.driver.is_app_installed(APIDEMO_PKG_NAME))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ApplicationsTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
