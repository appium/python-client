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

import copy
import json

import httpretty

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from test.helpers.constants import SERVER_URL_BASE


def create_session(options):
    httpretty.register_uri(
        httpretty.POST,
        f'{SERVER_URL_BASE}/session',
        body=json.dumps({'value': {'sessionId': 'options-session', 'capabilities': {}}}),
    )
    driver = webdriver.Remote(SERVER_URL_BASE, options=options)
    assert driver.session_id == 'options-session'
    return json.loads(httpretty.last_request().body.decode('utf-8'))['capabilities']


@httpretty.activate
def test_options_list_preserves_common_and_alternative_capabilities():
    proxy = {'proxyType': 'manual', 'httpProxy': 'proxy.example:8080'}
    options = [
        UiAutomator2Options().set_capability('deviceName', name).set_capability('proxy', proxy)
        for name in ['first-device', 'second-device']
    ]
    original_capabilities = copy.deepcopy([option.to_capabilities() for option in options])

    assert create_session(options) == {
        'alwaysMatch': {'platformName': 'Android', 'appium:automationName': 'UIAutomator2', 'proxy': proxy},
        'firstMatch': [{'appium:deviceName': 'first-device'}, {'appium:deviceName': 'second-device'}],
    }
    assert [option.to_capabilities() for option in options] == original_capabilities


@httpretty.activate
def test_options_list_normalizes_automation_overrides_before_matching():
    default_options = UiAutomator2Options()
    overridden_options = UiAutomator2Options().set_capability('automationName', 'Espresso')

    assert create_session([default_options, overridden_options]) == {
        'alwaysMatch': {'platformName': 'Android'},
        'firstMatch': [{'appium:automationName': 'UIAutomator2'}, {'appium:automationName': 'Espresso'}],
    }


@httpretty.activate
def test_options_list_supports_different_platform_alternatives():
    assert create_session([UiAutomator2Options(), XCUITestOptions()]) == {
        'alwaysMatch': {},
        'firstMatch': [
            {'platformName': 'Android', 'appium:automationName': 'UIAutomator2'},
            {'platformName': 'iOS', 'appium:automationName': 'XCUITest'},
        ],
    }


@httpretty.activate
def test_single_item_options_list_matches_single_options_request():
    options = UiAutomator2Options().set_capability('deviceName', 'single-device')
    assert create_session([options]) == create_session(options)
