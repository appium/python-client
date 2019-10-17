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


class TestWebDriverKeyboard(object):

    @httpretty.activate
    def test_hide_keyboard(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/hide_keyboard')
        )
        assert isinstance(driver.hide_keyboard(), WebDriver)

    @httpretty.activate
    def test_press_keycode(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/press_keycode'),
            body='{"value": "86"}'
        )
        driver.press_keycode(86)
        d = get_httpretty_request_body((httpretty.last_request()))
        assert d['keycode'] == 86

    @httpretty.activate
    def test_long_press_keycode(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/long_press_keycode'),
            body='{"value": "86"}'
        )
        driver.long_press_keycode(86)
        d = get_httpretty_request_body((httpretty.last_request()))
        assert d['keycode'] == 86

    @httpretty.activate
    def test_keyevent(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/keyevent'),
            body='{keycode: 86}'
        )
        assert isinstance(driver.keyevent(86), WebDriver)

    @httpretty.activate
    def test_press_keycode_with_flags(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/press_keycode'),
            body='{keycode: 86, metastate: 2097153, flags: 44}'
        )
        # metastate is META_SHIFT_ON and META_NUM_LOCK_ON
        # flags is CANCELFLAG_CANCELEDED, FLAG_KEEP_TOUCH_MODE, FLAG_FROM_SYSTEM
        assert isinstance(
            driver.press_keycode(
                86, metastate=[
                    0x00000001, 0x00200000], flags=[
                    0x20, 0x00000004, 0x00000008]), WebDriver)

    @httpretty.activate
    def test_long_press_keycode_with_flags(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/long_press_keycode'),
            body='{keycode: 86, metastate: 2097153, flags: 44}'
        )
        # metastate is META_SHIFT_ON and META_NUM_LOCK_ON
        # flags is CANCELFLAG_CANCELEDED, FLAG_KEEP_TOUCH_MODE, FLAG_FROM_SYSTEM
        assert isinstance(
            driver.long_press_keycode(
                86, metastate=[
                    0x00000001, 0x00200000], flags=[
                    0x20, 0x00000004, 0x00000008]), WebDriver)
