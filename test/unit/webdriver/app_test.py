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

from appium.webdriver.applicationstate import ApplicationState
from appium.webdriver.webdriver import WebDriver
from test.unit.helper.test_helper import (
    android_w3c_driver,
    appium_command,
    get_httpretty_request_body
)


class TestWebDriverApp(object):

    @httpretty.activate
    def test_reset(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/app/reset'),
            body='{"value": ""}'
        )
        result = driver.reset()

        assert {'sessionId': '1234567890'}, get_httpretty_request_body(httpretty.last_request())
        assert isinstance(result, WebDriver)

    @httpretty.activate
    def test_install_app(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/install_app'),
            body='{"value": ""}'
        )
        result = driver.install_app('path/to/app')

        assert {'app': 'path/to/app'}, get_httpretty_request_body(httpretty.last_request())
        assert isinstance(result, WebDriver)

    @httpretty.activate
    def test_remove_app(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/remove_app'),
            body='{"value": ""}'
        )
        result = driver.remove_app('com.app.id')

        assert {'app': 'com.app.id'}, get_httpretty_request_body(httpretty.last_request())
        assert isinstance(result, WebDriver)

    @httpretty.activate
    def test_app_installed(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/app_installed'),
            body='{"value": true}'
        )
        result = driver.is_app_installed("com.app.id")
        assert {'app': "com.app.id"}, get_httpretty_request_body(httpretty.last_request())
        assert result is True

    @httpretty.activate
    def test_terminate_app(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/terminate_app'),
            body='{"value": true}'
        )
        result = driver.terminate_app("com.app.id")
        assert {'app': "com.app.id"}, get_httpretty_request_body(httpretty.last_request())
        assert result is True

    @httpretty.activate
    def test_activate_app(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/activate_app'),
            body='{"value": ""}'
        )
        result = driver.activate_app("com.app.id")

        assert {'app': 'com.app.id'}, get_httpretty_request_body(httpretty.last_request())
        assert isinstance(result, WebDriver)

    @httpretty.activate
    def test_background_app(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/app/background'),
            body='{"value": ""}'
        )
        result = driver.background_app(0)
        assert {'app': 0}, get_httpretty_request_body(httpretty.last_request())
        assert isinstance(result, WebDriver)

    @httpretty.activate
    def test_launch_app(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/app/launch'),
            body='{"value": }'
        )
        assert isinstance(driver.launch_app(), WebDriver)

    @httpretty.activate
    def test_close_app(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/app/close'),
            body='{"value": }'
        )
        assert isinstance(driver.close_app(), WebDriver)

    @httpretty.activate
    def test_query_app_state(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/app_state'),
            body='{"value": 3 }'
        )
        result = driver.query_app_state('com.app.id')

        assert {'app': 3}, get_httpretty_request_body(httpretty.last_request())
        assert result is ApplicationState.RUNNING_IN_BACKGROUND
