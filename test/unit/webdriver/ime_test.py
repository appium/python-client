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


import json

import httpretty

from appium.webdriver.webdriver import WebDriver
from test.unit.helper.test_helper import (
    android_w3c_driver,
    appium_command,
    get_httpretty_request_body
)


class TestWebDriverIme(object):

    @httpretty.activate
    def test_available_ime_engines(self):
        ANDROID_LATIN = 'com.android.inputmethod.latin/.LatinIME'
        GOOGLE_LATIN = 'com.google.android.inputmethod.latin/com.android.inputmethod.latin.LatinIME'

        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/ime/available_engines'),
            body=json.dumps({'value': [ANDROID_LATIN, GOOGLE_LATIN]})
        )
        assert driver.available_ime_engines == [ANDROID_LATIN, GOOGLE_LATIN]

    @httpretty.activate
    def test_is_ime_active(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/ime/activated'),
            body=json.dumps({'value': True})
        )
        assert driver.is_ime_active() is True

    @httpretty.activate
    def test_activate_ime_engine(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/ime/activate'),
        )
        engine = 'com.android.inputmethod.latin/.LatinIME'
        assert isinstance(driver.activate_ime_engine(engine), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['engine'] == 'com.android.inputmethod.latin/.LatinIME'

    @httpretty.activate
    def test_deactivate_ime_engine(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/ime/deactivate'),
        )
        assert isinstance(driver.deactivate_ime_engine(), WebDriver)

    @httpretty.activate
    def test_active_ime_engine(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/ime/active_engine'),
            body=json.dumps({'value': 'com.android.inputmethod.latin/.LatinIME'})
        )
        assert driver.active_ime_engine == 'com.android.inputmethod.latin/.LatinIME'
