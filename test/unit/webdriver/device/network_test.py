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

from appium.webdriver.extensions.android.network import NetSpeed
from appium.webdriver.webdriver import WebDriver
from test.unit.helper.test_helper import (
    android_w3c_driver,
    appium_command,
    get_httpretty_request_body
)


class TestWebDriverNetwork(object):

    @httpretty.activate
    def test_network_connection(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/network_connection'),
            body='{"value": 2}'
        )
        assert driver.network_connection == 2

    @httpretty.activate
    def test_set_network_connection(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/network_connection'),
            body='{"value": ""}'
        )
        driver.set_network_connection(2)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['parameters']['type'] == 2

    @httpretty.activate
    def test_set_network_speed(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/network_speed'),
        )
        assert isinstance(driver.set_network_speed(NetSpeed.LTE), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['netspeed'] == NetSpeed.LTE

    @httpretty.activate
    def test_toggle_wifi(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/toggle_wifi'),
        )
        assert isinstance(driver.toggle_wifi(), WebDriver)
