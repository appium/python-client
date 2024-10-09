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
from test.unit.helper.test_helper import android_w3c_driver, appium_command, get_httpretty_request_body, ios_w3c_driver


class TestWebDriverLockAndroid(object):
    @httpretty.activate
    def test_lock(self):
        driver = android_w3c_driver()
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/appium/device/lock'), body='{"value": ""}')
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'), body='{"value": ""}')
        driver.lock(1)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d.get('seconds', d['args'][0]['seconds']) == 1

    @httpretty.activate
    def test_lock_no_args(self):
        driver = android_w3c_driver()
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/appium/device/lock'), body='{"value": ""}')
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'), body='{"value": ""}')
        driver.lock()

    @httpretty.activate
    def test_islocked_false(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST, appium_command('/session/1234567890/appium/device/is_locked'), body='{"value": false}'
        )
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'), body='{"value": false}')
        assert driver.is_locked() is False

    @httpretty.activate
    def test_islocked_true(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST, appium_command('/session/1234567890/appium/device/is_locked'), body='{"value": true}'
        )
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'), body='{"value": true}')
        assert driver.is_locked() is True

    @httpretty.activate
    def test_unlock(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/unlock'),
        )
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'))
        assert isinstance(driver.unlock(), WebDriver)


class TestWebDriverLockIOS(object):
    @httpretty.activate
    def test_lock(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/appium/device/lock'), body='{"value": ""}')
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'), body='{"value": ""}')
        driver.lock(1)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d.get('seconds', d['args'][0]['seconds']) == 1

    @httpretty.activate
    def test_lock_no_args(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/appium/device/lock'), body='{"value": ""}')
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'), body='{"value": ""}')
        driver.lock()

    @httpretty.activate
    def test_islocked_false(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.POST, appium_command('/session/1234567890/appium/device/is_locked'), body='{"value": false}'
        )
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'), body='{"value": false}')
        assert driver.is_locked() is False

    @httpretty.activate
    def test_islocked_true(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.POST, appium_command('/session/1234567890/appium/device/is_locked'), body='{"value": true}'
        )
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'), body='{"value": true}')
        assert driver.is_locked() is True

    @httpretty.activate
    def test_unlock(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/unlock'),
        )
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'))
        assert isinstance(driver.unlock(), WebDriver)

    @httpretty.activate
    def test_touch_id(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'))
        assert isinstance(driver.touch_id(True), WebDriver)
        assert {
            'script': 'mobile: sendBiometricMatch',
            'args': [{'match': True, 'type': 'touchId'}],
        } == get_httpretty_request_body(httpretty.last_request())

    @httpretty.activate
    def test_enroll_biometric(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'))
        assert isinstance(driver.toggle_touch_id_enrollment(), WebDriver)
        assert {'script': 'mobile: enrollBiometric', 'args': [{'isEnabled': True}]} == get_httpretty_request_body(
            httpretty.last_request()
        )
