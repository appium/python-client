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

from test.unit.helper.test_helper import (
    android_w3c_driver,
    appium_command,
    get_httpretty_request_body
)


class TestWebDriverDeviceTime(object):

    @httpretty.activate
    def test_device_time(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/appium/device/system_time'),
            body='{"value": "2019-01-05T14:46:44+09:00"}'
        )
        assert driver.device_time == '2019-01-05T14:46:44+09:00'

    @httpretty.activate
    def test_get_device_time(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/appium/device/system_time'),
            body='{"value": "2019-01-05T14:46:44+09:00"}'
        )
        assert driver.get_device_time() == '2019-01-05T14:46:44+09:00'

    @httpretty.activate
    def test_get_formatted_device_time(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/system_time'),
            body='{"value": "2019-01-08"}'
        )
        assert driver.get_device_time('YYYY-MM-DD') == '2019-01-08'

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['format'] == 'YYYY-MM-DD'
