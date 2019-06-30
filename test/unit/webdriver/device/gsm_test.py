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

from appium.webdriver.extensions.android.gsm import (
    GsmCallActions,
    GsmSignalStrength,
    GsmVoiceState
)
from appium.webdriver.webdriver import WebDriver
from test.unit.helper.test_helper import (
    android_w3c_driver,
    appium_command,
    get_httpretty_request_body
)


class TestWebDriveGsm(object):

    @httpretty.activate
    def test_make_gsm_call(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/gsm_call'),
        )
        assert isinstance(driver.make_gsm_call('5551234567', GsmCallActions.CALL), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['phoneNumber'] == '5551234567'
        assert d['action'] == GsmCallActions.CALL

    @httpretty.activate
    def test_set_gsm_signal(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/gsm_signal'),
        )
        assert isinstance(driver.set_gsm_signal(GsmSignalStrength.GREAT), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['signalStrength'] == GsmSignalStrength.GREAT
        assert d['signalStrengh'] == GsmSignalStrength.GREAT

    @httpretty.activate
    def test_set_gsm_voice(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/gsm_voice'),
        )
        assert isinstance(driver.set_gsm_voice(GsmVoiceState.ROAMING), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['state'] == GsmVoiceState.ROAMING
