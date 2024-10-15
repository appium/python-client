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

from appium import webdriver
from appium.options.flutter_integration import FlutterOptions
from test.helpers.constants import SERVER_URL_BASE


class TestFlutterIntegrationDriver:
    @httpretty.activate
    def test_create_session(self):
        # Set flutter options
        flutterOptions = FlutterOptions()
        flutterOptions.flutter_system_port = 9999
        flutterOptions.flutter_enable_mock_camera = True
        flutterOptions.flutter_element_wait_timeout = 10000
        flutterOptions.flutter_server_launch_timeout = 120000

        httpretty.register_uri(
            httpretty.POST,
            f'{SERVER_URL_BASE}/session',
            body='{ "value": {"sessionId": "session-id", "capabilities": {"deviceName": "Android Emulator"}} }',
        )

        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'app': 'path/to/app',
        }
        driver = webdriver.Remote(SERVER_URL_BASE, options=flutterOptions.load_capabilities(desired_caps))

        request_json = json.loads(httpretty.HTTPretty.latest_requests[0].body.decode('utf-8'))
        assert request_json.get('capabilities') is not None
        assert request_json['capabilities']['alwaysMatch'] == {
            'platformName': 'Android',
            'appium:deviceName': 'Android Emulator',
            'appium:app': 'path/to/app',
            'appium:automationName': 'FlutterIntegration',
            'appium:flutterSystemPort': 9999,
            'appium:flutterEnableMockCamera': True,
            'appium:flutterElementWaitTimeout': 10000,
            'appium:flutterServerLaunchTimeout': 120000,
        }
        assert request_json.get('desiredCapabilities') is None
        assert driver.session_id == 'session-id'
