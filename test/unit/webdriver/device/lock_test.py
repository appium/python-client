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


class TestWebDriverLock(object):

    @httpretty.activate
    def test_lock(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/lock'),
            body='{"value": ""}'
        )
        driver.lock(1)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['seconds'] == 1

    @httpretty.activate
    def test_lock_no_args(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/lock'),
            body='{"value": ""}'
        )
        driver.lock()

        d = get_httpretty_request_body(httpretty.last_request())
        assert d == {}

    @httpretty.activate
    def test_islocked_false(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/is_locked'),
            body='{"value": false}'
        )
        assert driver.is_locked() is False

    @httpretty.activate
    def test_islocked_true(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/is_locked'),
            body='{"value": true}'
        )

        assert driver.is_locked() is True

    @httpretty.activate
    def test_unlock(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/unlock'),
        )
        assert isinstance(driver.unlock(), WebDriver)
