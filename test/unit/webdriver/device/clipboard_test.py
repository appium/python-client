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


class WebDriverDeviceClipboardTests(unittest.TestCase):

    @httpretty.activate
    def test_clipboard(self):
        driver = TestHelper.mock_android_driver()
        httpretty.register_uri(
            httpretty.POST,
            'http://localhost:4723/wd/hub/session/1234567890/appium/device/set_clipboard',
            body='{"value": ""}'
        )
        driver.set_clipboard_text('hello')

        d = json.loads(httpretty.last_request().body)
        self.assertEqual("aGVsbG8=", d["content"])
        self.assertEqual("plaintext", d["contentType"])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(WebDriverDeviceClipboardTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
