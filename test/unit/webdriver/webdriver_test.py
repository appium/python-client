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
from test.unit.helper.test_helper import TestHelper


class WebDriverWebDriverTests(unittest.TestCase):

    @httpretty.activate
    def test_create_session(self):
        httpretty.register_uri(
            httpretty.POST,
            'http://localhost:4723/wd/hub/session',
            body='{ "value": { "sessionId": "session-id", "capabilities": {"deviceName": "Android Emulator"}}}'
        )

        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'app': 'path/to/app',
            'automationName': 'UIAutomator2'
        }
        driver = webdriver.Remote(
            'http://localhost:4723/wd/hub',
            desired_caps
        )

        self.assertEqual(1, len(httpretty.HTTPretty.latest_requests))

        request = httpretty.HTTPretty.latest_requests[0]
        self.assertEqual('application/json;charset=UTF-8', request.headers['content-type'])

        request_json = json.loads(httpretty.HTTPretty.latest_requests[0].body)
        self.assertTrue(request_json.get('capabilities') is not None)
        self.assertTrue(request_json.get('desiredCapabilities') is not None)

        self.assertEqual('session-id', driver.session_id)
        self.assertEqual(True, driver.w3c)

    @httpretty.activate
    def test_create_session_forceMjsonwp(self):
        httpretty.register_uri(
            httpretty.POST,
            'http://localhost:4723/wd/hub/session',
            body='{ "capabilities": {"deviceName": "Android Emulator"}, "status": 0, "sessionId": "session-id"}'
        )

        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'app': 'path/to/app',
            'automationName': 'UIAutomator2',
            'forceMjsonwp': True
        }
        driver = webdriver.Remote(
            'http://localhost:4723/wd/hub',
            desired_caps
        )

        self.assertEqual(1, len(httpretty.HTTPretty.latest_requests))

        request = httpretty.HTTPretty.latest_requests[0]
        self.assertEqual('application/json;charset=UTF-8', request.headers['content-type'])

        request_json = json.loads(httpretty.HTTPretty.latest_requests[0].body)
        self.assertTrue(request_json.get('capabilities') is None)
        self.assertTrue(request_json.get('desiredCapabilities') is not None)

        self.assertEqual('session-id', driver.session_id)
        self.assertEqual(False, driver.w3c)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(WebDriverWebDriverTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
