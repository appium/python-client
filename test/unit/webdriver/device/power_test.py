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

from test.unit.helper.test_helper import (
    appium_command,
    android_w3c_driver,
    get_httpretty_request_body
)

import httpretty
import pytest

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.extensions.power import Power


class TestWebDriverPower(object):

    @httpretty.activate
    def test_set_power_capacity_percent_0_within_range(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/power_capacity'),
        )
        assert isinstance(driver.set_power_capacity(0), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['percent'] == 0

    @httpretty.activate
    def test_set_power_capacity_percent_100_within_range(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/power_capacity'),
        )
        assert isinstance(driver.set_power_capacity(100), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['percent'] == 100

    @httpretty.activate
    def test_set_power_capacity_out_of_range(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/power_capacity'),
        )
        with pytest.raises(TypeError):
            driver.set_power_capacity(101)

    def test_power_state(self):
        assert Power.AC_OFF == 'off'
        assert Power.AC_ON == 'on'

    @httpretty.activate
    def test_set_power_ac_on(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/power_ac'),
        )
        assert isinstance(driver.set_power_ac(Power.AC_ON), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['state'] == Power.AC_ON

    @httpretty.activate
    def test_set_power_ac_invalid_value(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/power_ac'),
        )
        with pytest.raises(TypeError):
            driver.set_power_ac('broken')
