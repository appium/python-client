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
        driver.start_activity('com.example.myapp', '.ExampleActivity')

        d = json.loads(httpretty.last_request().body.decode('utf-8'))
        assert d['sessionId'] == '1234567890'
        assert d['appPackage'] == 'com.example.myapp'
        assert d['appActivity'] == '.ExampleActivity'

    @httpretty.activate
    def test_start_activity_with_opts(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/start_activity'),
            body='{"value": ""}'
        )
        driver.start_activity(
            app_package='com.example.myapp',
            app_activity='.ExampleActivity',
            app_wait_package='',
            intent_action='',
            intent_category='',
            intent_flags='',
            optional_intent_arguments='',
            dont_stop_app_on_reset=''
        )

        d = json.loads(httpretty.last_request().body.decode('utf-8'))
        assert d['sessionId'] == '1234567890'
        assert d['appPackage'] == 'com.example.myapp'
        assert d['appActivity'] == '.ExampleActivity'
        assert d['appWaitPackage'] == ''
        assert d['intentAction'] == ''
        assert d['intentCategory'] == ''
        assert d['optionalIntentArguments'] == ''
        assert d['dontStopAppOnReset'] == ''

    @httpretty.activate
    def test_current_activity(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/appium/device/current_activity'),
            body='{"value": ".ExampleActivity"}'
        )
        assert driver.current_activity == '.ExampleActivity'

    @httpretty.activate
    def test_wait_activity(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/appium/device/current_activity'),
            body='{"value": ".ExampleActivity"}'
        )
        assert driver.wait_activity('.ExampleActivity', 1) is True
