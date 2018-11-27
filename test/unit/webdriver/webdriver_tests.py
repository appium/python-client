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

class WebDriverWebDriverTests(unittest.TestCase):

    @httpretty.activate
    def test_create_session(self):
        httpretty.register_uri(
            httpretty.POST,
            'http://localhost:4723/wd/hub/session',
            body = '{ "sessionId": "session-id" }'
        )

        # WebDriver
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

        self.assertEqual(1, len(httpretty.HTTPretty.latest_requests))

        request = httpretty.HTTPretty.latest_requests[0]
        self.assertEqual('application/json;charset=UTF-8', request.headers['content-type'])

        self.assertEqual('session-id', driver.session_id)

    @httpretty.activate
    def test_clipboard(self):
        httpretty.register_uri(
            httpretty.POST,
            'http://localhost:4723/wd/hub/session',
            body = '{ "sessionId": "session-id" }'
        )

        # WebDriver
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

        httpretty.register_uri(
            httpretty.POST,
            'http://localhost:4723/wd/hub/session/session-id/appium/device/set_clipboard',
            body = '{"value": ""}'
        )
        driver.set_clipboard_text('hello')

        d = json.loads(httpretty.last_request().body)
        self.assertEqual("aGVsbG8=", d["content"])
        self.assertEqual("plaintext", d["contentType"])

if __name__ == "__main__":
    unittest.main()
