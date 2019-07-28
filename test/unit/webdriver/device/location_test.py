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

FLT_EPSILON = 1e-9


class TestWebDriverLocation(object):

    @httpretty.activate
    def test_toggle_location_services(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/toggle_location_services')
        )
        assert isinstance(driver.toggle_location_services(), WebDriver)

    @httpretty.activate
    def test_set_location_float(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/location')
        )
        assert isinstance(driver.set_location(11.1, 22.2, 33.3), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert abs(d['location']['latitude'] - 11.1) <= FLT_EPSILON
        assert abs(d['location']['longitude'] - 22.2) <= FLT_EPSILON
        assert abs(d['location']['altitude'] - 33.3) <= FLT_EPSILON

    @httpretty.activate
    def test_set_location_str(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/location')
        )
        assert isinstance(driver.set_location('11.1', '22.2', '33.3'), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['location']['latitude'] == '11.1'
        assert d['location']['longitude'] == '22.2'
        assert d['location']['altitude'] == '33.3'

    @httpretty.activate
    def test_set_location_without_altitude(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/location')
        )
        assert isinstance(driver.set_location(11.1, 22.2), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert abs(d['location']['latitude'] - 11.1) <= FLT_EPSILON
        assert abs(d['location']['longitude'] - 22.2) <= FLT_EPSILON
        assert d['location'].get('altitude') is None

    @httpretty.activate
    def test_location(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/location'),
            body='{"value": {"latitude": 11.1, "longitude": 22.2, "altitude": 33.3}}'
        )
        val = driver.location
        assert abs(val['latitude'] - 11.1) <= FLT_EPSILON
        assert abs(val['longitude'] - 22.2) <= FLT_EPSILON
        assert abs(val['altitude'] - 33.3) <= FLT_EPSILON
