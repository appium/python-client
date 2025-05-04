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

from appium.webdriver.extensions.flutter_integration.flutter_commands import (
    FlutterCommand,
)
from test.unit.helper.test_helper import (
    appium_command,
    flutter_w3c_driver,
    get_httpretty_request_body,
)


class TestFlutterRenderTree:
    @httpretty.activate
    def test_get_render_tree_with_all_filters(self):
        expected_body = [{'<partial_tree>': 'LoginButton'}]
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/execute/sync'),
            body=json.dumps({'value': expected_body}),
        )

        driver = flutter_w3c_driver()
        flutter = FlutterCommand(driver)

        result = flutter.get_render_tree(widget_type='ElevatedButton', key='LoginButton', text='Login')

        request_body = get_httpretty_request_body(httpretty.last_request())
        assert request_body['script'] == 'flutter: renderTree'
        assert request_body['args'] == [
            {
                'widgetType': 'ElevatedButton',
                'key': 'LoginButton',
                'text': 'Login',
            }
        ]

        assert result == expected_body

    @httpretty.activate
    def test_get_render_tree_with_partial_filters(self):
        expected_body = [{'<partial_tree>': 'LoginScreen'}]

        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/execute/sync'),
            body=json.dumps({'value': expected_body}),
        )

        driver = flutter_w3c_driver()
        flutter = FlutterCommand(driver)

        result = flutter.get_render_tree(widget_type='LoginScreen')

        request_body = get_httpretty_request_body(httpretty.last_request())
        assert request_body['script'] == 'flutter: renderTree'
        assert request_body['args'] == [{'widgetType': 'LoginScreen'}]

        assert result == expected_body

    @httpretty.activate
    def test_get_render_tree_with_no_filters(self):
        expected_body = [{'<full_tree>': 'RootWidget'}]
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/execute/sync'),
            body=json.dumps({'value': expected_body}),
        )

        driver = flutter_w3c_driver()
        flutter = FlutterCommand(driver)

        result = flutter.get_render_tree()

        request_body = get_httpretty_request_body(httpretty.last_request())
        assert request_body['script'] == 'flutter: renderTree'
        assert request_body['args'] == [{}]

        assert result == expected_body
