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


class TestWebDriverSettings(object):

    @httpretty.activate
    def test_get_settings_bool(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/appium/settings'),
            body='{"value": {"sample": true}}'
        )
        assert driver.get_settings()['sample'] is True

    @httpretty.activate
    def test_update_settings_bool(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/settings'),
        )
        assert isinstance(driver.update_settings({"sample": True}), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['settings']['sample'] is True

    @httpretty.activate
    def test_get_settings_string(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/appium/settings'),
            body='{"value": {"sample": "string"}}'
        )
        assert driver.get_settings()['sample'] == 'string'

    @httpretty.activate
    def test_update_settings_string(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/settings'),
        )
        assert isinstance(driver.update_settings({"sample": 'string'}), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['settings']['sample'] == 'string'
