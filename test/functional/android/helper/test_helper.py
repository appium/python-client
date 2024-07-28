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
import base64
import os

from appium import webdriver
from appium.options.android import UiAutomator2Options
from test.functional.test_helper import is_ci
from test.helpers.constants import SERVER_URL_BASE

from . import desired_capabilities

# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 10

# The package name of ApiDemos-debug.apk.zip
APIDEMO_PKG_NAME = 'io.appium.android.apis'


class BaseTestCase(unittest.TestCase):
    def setup_method(self, method) -> None:  # type: ignore
        caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk.zip')
        self.driver = webdriver.Remote(SERVER_URL_BASE, options=UiAutomator2Options().load_capabilities(caps))
        if is_ci():
            self.driver.start_recording_screen()

    def teardown_method(self, method) -> None:  # type: ignore
        if not hasattr(self, 'driver'):
            return

        if is_ci():
            payload = self.driver.stop_recording_screen()
            video_path = os.path.join(os.getcwd(), method.__name__ + '.mp4')
            with open(video_path, 'wb') as fd:
                fd.write(base64.b64decode(payload))
        self.driver.quit()
