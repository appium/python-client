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

from test.unit.helper.test_helper import appium_command, android_w3c_driver

import json
import httpretty


class TestWebDriverDeviceActivities(object):

    @httpretty.activate
    def test_start_activity(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/start_activity'),
            body='{"value": ""}'
        )
        driver.start_activity('com.example.myapp', 'ExampleActivity')

        d = json.loads(httpretty.last_request().body.decode('utf-8'))
        assert d['appPackage'] == 'com.example.myapp'
        assert d['appActivity'] == 'ExampleActivity'
        assert d['sessionId'] == '1234567890'
