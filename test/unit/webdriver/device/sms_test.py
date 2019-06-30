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

import httpretty

from appium.webdriver.webdriver import WebDriver
from test.unit.helper.test_helper import (
    android_w3c_driver,
    appium_command,
    get_httpretty_request_body
)


class TestWebDriverSms(object):

    @httpretty.activate
    def test_send_sms(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/send_sms'),
        )
        assert isinstance(driver.send_sms('555-123-4567', 'Hey lol'), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['phoneNumber'] == '555-123-4567'
        assert d['message'] == 'Hey lol'
