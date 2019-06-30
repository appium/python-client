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

from appium.webdriver.extensions.android.power import Power
from appium.webdriver.webdriver import WebDriver
from test.unit.helper.test_helper import (
    android_w3c_driver,
    appium_command,
    get_httpretty_request_body
)


class TestWebDriverPower(object):

    @httpretty.activate
    def test_set_power_capacity(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/power_capacity'),
        )
        assert isinstance(driver.set_power_capacity(50), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['percent'] == 50

    @httpretty.activate
    def test_set_power_ac(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/power_ac'),
        )
        assert isinstance(driver.set_power_ac(Power.AC_ON), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['state'] == Power.AC_ON
