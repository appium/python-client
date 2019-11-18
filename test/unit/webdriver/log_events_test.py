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
    appium_command,
    get_httpretty_request_body,
    ios_w3c_driver
)


class TestWebDriverLogEvents(object):

    @httpretty.activate
    def test_get_events(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/events'),
            body=json.dumps({'value': {'appium:funEvent': [12347]}})
        )
        events = driver.get_events()
        assert events['appium:funEvent'] == [12347]

        d = get_httpretty_request_body(httpretty.last_request())
        assert 'type' not in d.keys()

    @httpretty.activate
    def test_get_events_args(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/events'),
            body=json.dumps({'value': {'appium:funEvent': [12347]}})
        )
        events_to_filter = ['appium:funEvent']
        events = driver.get_events(events_to_filter)
        assert events['appium:funEvent'] == [12347]

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['type'] == events_to_filter

    @httpretty.activate
    def test_log_event(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/log_event'),
            body=""
        )
        vendor_name = 'appium'
        event_name = 'funEvent'
        assert isinstance(driver.log_event(vendor_name, event_name), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['vendor'] == vendor_name
        assert d['event'] == event_name
