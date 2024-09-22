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

from appium.webdriver.extensions.flutter_integration.flutter_commands import FlutterCommand
from appium.webdriver.extensions.flutter_integration.flutter_finder import FlutterFinder
from appium.webdriver.webelement import WebElement as MobileWebElement
from test.unit.helper.test_helper import appium_command, flutter_w3c_driver, get_httpretty_request_body


class TestFlutterWaits(object):

    @httpretty.activate
    def test_wait_for_visible_with_finder(self):
        driver = flutter_w3c_driver()
        flutter = FlutterCommand(driver)

        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/execute/sync'),
        )

        finder = FlutterFinder.by_key('message_field')
        flutter.wait_for_visible(finder, 5)

        request_body = get_httpretty_request_body(httpretty.last_request())
        arguments = request_body['args'][0]
        assert request_body['script'] == 'flutter: waitForVisible'
        expected_arguments = {
            'locator': {'using': '-flutter key', 'value': 'message_field'},
            'timeout': 5,
        }
        assert arguments == expected_arguments

    @httpretty.activate
    def test_wait_for_visible_with_webelement(self):
        driver = flutter_w3c_driver()
        flutter = FlutterCommand(driver)

        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/execute/sync'),
        )

        element = MobileWebElement(driver, 'element_id')
        flutter.wait_for_visible(element, 5)

        request_body = get_httpretty_request_body(httpretty.last_request())
        arguments = request_body['args'][0]
        assert request_body['script'] == 'flutter: waitForVisible'
        assert list(arguments['element'].values())[0] == 'element_id'
        assert arguments['timeout'] == 5

    @httpretty.activate
    def test_wait_for_invisible_with_finder(self):
        driver = flutter_w3c_driver()
        flutter = FlutterCommand(driver)

        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/execute/sync'),
        )

        message_field_finder = FlutterFinder.by_key('message_field')
        flutter.wait_for_invisible(message_field_finder, 5)

        request_body = get_httpretty_request_body(httpretty.last_request())
        arguments = request_body['args'][0]
        assert request_body['script'] == 'flutter: waitForAbsent'
        expected_arguments = {
            'locator': {'using': '-flutter key', 'value': 'message_field'},
            'timeout': 5,
        }
        assert arguments == expected_arguments

    @httpretty.activate
    def test_wait_for_invisible_with_webelement(self):
        driver = flutter_w3c_driver()
        flutter = FlutterCommand(driver)

        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/execute/sync'),
        )

        element = MobileWebElement(driver, 'element_id')
        flutter.wait_for_invisible(element, 5)

        request_body = get_httpretty_request_body(httpretty.last_request())
        arguments = request_body['args'][0]
        assert request_body['script'] == 'flutter: waitForAbsent'
        assert list(arguments['element'].values())[0] == 'element_id'
        assert arguments['timeout'] == 5
