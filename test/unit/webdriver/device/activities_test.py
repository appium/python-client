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


class TestWebDriverActivities(object):

    @httpretty.activate
    def test_start_activity(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/start_activity'),
            body='{"value": ""}'
        )
        driver.start_activity('com.example.myapp', '.ExampleActivity')

        d = get_httpretty_request_body(httpretty.last_request())
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
            app_wait_package='com.example.waitapp',
            intent_action='android.intent.action.MAIN',
            intent_category='android.intent.category.LAUNCHER',
            intent_flags='0x10200000',
            optional_intent_arguments='--es "activity" ".ExampleActivity"',
            dont_stop_app_on_reset=True
        )

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['appPackage'] == 'com.example.myapp'
        assert d['appActivity'] == '.ExampleActivity'
        assert d['appWaitPackage'] == 'com.example.waitapp'
        assert d['intentAction'] == 'android.intent.action.MAIN'
        assert d['intentCategory'] == 'android.intent.category.LAUNCHER'
        assert d['intentFlags'] == '0x10200000'
        assert d['optionalIntentArguments'] == '--es "activity" ".ExampleActivity"'
        assert d['dontStopAppOnReset'] is True

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
