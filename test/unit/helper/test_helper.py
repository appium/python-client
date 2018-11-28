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
import httpretty
import json

from appium import webdriver


class TestHelper():
    def mock_android_driver():
        httpretty.register_uri(
            httpretty.POST,
            'http://localhost:4723/wd/hub/session',
            body='{ "value": { "sessionId": "session-id", "capabilities": {"deviceName": "Android Emulator"}}}'
        )

        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'app': 'path/to/app',
            'newCommandTimeout': 240,
            'automationName': 'UIAutomator2'
        }
        driver = webdriver.Remote(
            'http://localhost:4723/wd/hub',
            desired_caps
        )
        return driver
