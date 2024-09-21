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

import os
import httpretty

from appium.common.helper import encode_file_to_base64
from appium.webdriver.extensions.flutter_integration.scroll_directions import ScrollDirection
from appium.webdriver.webelement import WebElement as MobileWebElement
from appium.webdriver.extensions.flutter_integration.flutter_commands import FlutterCommand
from appium.webdriver.flutter_finder import FlutterFinder
from test.unit.helper.test_helper import flutter_w3c_driver, appium_command, get_httpretty_request_body


class TestFlutterActions(object):
    
    @httpretty.activate
    def test_double_click(self):
        driver = flutter_w3c_driver()
        flutter = FlutterCommand(driver)
        
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/execute/sync'),
        )
        
        element = MobileWebElement(driver, 'element_id')
        flutter.perform_double_click(element, (10,20))

        request_body = get_httpretty_request_body(httpretty.last_request())
        arguments = request_body['args'][0]
        assert request_body['script'] == 'flutter: doubleClick'
        assert list(arguments['origin'].values())[0] == 'element_id'
        assert arguments['offset'] == {'x': 10, 'y': 20}

    @httpretty.activate
    def test_drag_and_drop(self):
        driver = flutter_w3c_driver()
        flutter = FlutterCommand(driver)
        
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/execute/sync'),
        )
        
        drag_element = MobileWebElement(driver, 'element_id1')
        drop_element = MobileWebElement(driver, 'element_id2')
        flutter.perform_drag_and_drop(drag_element, drop_element)

        request_body = get_httpretty_request_body(httpretty.last_request())
        arguments = request_body['args'][0]
        assert request_body['script'] == 'flutter: dragAndDrop'
        assert list(arguments['source'].values())[0] == 'element_id1'
        assert list(arguments['target'].values())[0] == 'element_id2'
        
    @httpretty.activate
    def test_scroll_till_visible(self):
        driver = flutter_w3c_driver()
        flutter = FlutterCommand(driver)
        
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/execute/sync'),
        )
        
        finder = FlutterFinder.by_key('message_field')
        flutter.scroll_till_visible(finder)

        request_body = get_httpretty_request_body(httpretty.last_request())
        arguments = request_body['args'][0]
        expected_arguments = {
            'finder': {'using': '-flutter key', 'value': 'message_field'},
            'scrollDirection': 'down'
        }
        assert request_body['script'] == 'flutter: scrollTillVisible'
        assert arguments == expected_arguments
    
    @httpretty.activate
    def test_scroll_till_visible_with_kwargs(self):
        driver = flutter_w3c_driver()
        flutter = FlutterCommand(driver)
        
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/execute/sync'),
        )
        
        finder = FlutterFinder.by_key('message_field')
        scroll_params = {'scrollView': FlutterFinder.by_type('Scrollable').to_dict(),
                         'delta': 30,
                         'maxScrolls': 30,
                         'settleBetweenScrollsTimeout': 5000,
                         'dragDuration': 35
                         }
        flutter.scroll_till_visible(finder, ScrollDirection.UP, **scroll_params)

        request_body = get_httpretty_request_body(httpretty.last_request())
        arguments = request_body['args'][0]
        assert request_body['script'] == 'flutter: scrollTillVisible'
        expected_arguments = {
            'finder': {'using': '-flutter key', 'value': 'message_field'},
            'scrollView': {'using': '-flutter type', 'value': 'Scrollable'},
            'scrollDirection': 'up',
            'dragDuration': 35,
            'settleBetweenScrollsTimeout': 5000,
            'maxScrolls': 30,
            'delta': 30
        }
        assert arguments == expected_arguments

    @httpretty.activate
    def test_inject_mock_image_with_file(self):
        driver = flutter_w3c_driver()
        flutter = FlutterCommand(driver)
        
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/execute/sync'),
        )
        
        success_qr_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'file', 'success_qr.png')
        base64_encoded_image = encode_file_to_base64(success_qr_file_path)
        flutter.inject_mock_image(success_qr_file_path)

        request_body = get_httpretty_request_body(httpretty.last_request())
        arguments = request_body['args'][0]
        assert request_body['script'] == 'flutter: injectImage'
        assert arguments == {'base64Image': base64_encoded_image}

    @httpretty.activate
    def test_activate_injected_image(self):
        driver = flutter_w3c_driver()
        flutter = FlutterCommand(driver)
        
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/execute/sync'),
        )
        
        flutter.activate_injected_image('213476478')

        request_body = get_httpretty_request_body(httpretty.last_request())
        arguments = request_body['args'][0]
        assert request_body['script'] == 'flutter: activateInjectedImage'
        assert arguments == {'imageId': '213476478'}

