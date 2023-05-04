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

from test.unit.helper.test_helper import android_w3c_driver, appium_command


class TestWebDriverActivities(object):
    @httpretty.activate
    def test_current_activity(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/appium/device/current_activity'),
            body='{"value": ".ExampleActivity"}',
        )
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/execute/sync'),
            body='{"value": ".ExampleActivity"}',
        )
        assert driver.current_activity == '.ExampleActivity'

    @httpretty.activate
    def test_wait_activity(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/appium/device/current_activity'),
            body='{"value": ".ExampleActivity"}',
        )
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/execute/sync'),
            body='{"value": ".ExampleActivity"}',
        )
        assert driver.wait_activity('.ExampleActivity', 1) is True
