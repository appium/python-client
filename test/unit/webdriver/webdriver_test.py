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
from mock import patch

from appium import version as appium_version
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from test.unit.helper.test_helper import (
    android_w3c_driver,
    appium_command,
    ios_w3c_driver
)


class TestWebDriverWebDriver(object):

    @httpretty.activate
    def test_create_session(self):
        httpretty.register_uri(
            httpretty.POST,
            'http://localhost:4723/wd/hub/session',
            body='{ "value": { "sessionId": "session-id", "capabilities": {"deviceName": "Android Emulator"}}}'
        )

        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'app': 'path/to/app',
            'automationName': 'UIAutomator2'
        }
        driver = webdriver.Remote(
            'http://localhost:4723/wd/hub',
            desired_caps
        )

        assert len(httpretty.HTTPretty.latest_requests) == 1

        request = httpretty.HTTPretty.latest_requests[0]
        assert request.headers['content-type'] == 'application/json;charset=UTF-8'
        assert 'appium/python {} (selenium'.format(appium_version.version) in request.headers['user-agent']

        request_json = json.loads(httpretty.HTTPretty.latest_requests[0].body.decode('utf-8'))
        assert request_json.get('capabilities') is not None
        assert request_json.get('desiredCapabilities') is not None

        assert driver.session_id == 'session-id'
        assert driver.w3c
        assert driver.command_executor.w3c

    @httpretty.activate
    def test_create_session_forceMjsonwp(self):
        httpretty.register_uri(
            httpretty.POST,
            'http://localhost:4723/wd/hub/session',
            body='{ "capabilities": {"deviceName": "Android Emulator"}, "status": 0, "sessionId": "session-id"}'
        )

        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'app': 'path/to/app',
            'automationName': 'UIAutomator2',
            'forceMjsonwp': True
        }
        driver = webdriver.Remote(
            'http://localhost:4723/wd/hub',
            desired_caps
        )

        assert len(httpretty.HTTPretty.latest_requests) == 1

        request = httpretty.HTTPretty.latest_requests[0]
        assert request.headers['content-type'] == 'application/json;charset=UTF-8'
        assert 'appium/python {} (selenium'.format(appium_version.version) in request.headers['user-agent']

        request_json = json.loads(httpretty.HTTPretty.latest_requests[0].body.decode('utf-8'))
        assert request_json.get('capabilities') is None
        assert request_json.get('desiredCapabilities') is not None

        assert driver.session_id == 'session-id'
        assert driver.w3c is False
        assert driver.command_executor.w3c is False

    @httpretty.activate
    def test_create_session_change_session_id(self):
        httpretty.register_uri(
            httpretty.POST,
            'http://localhost:4723/wd/hub/session',
            body='{ "value": { "sessionId": "session-id", "capabilities": {"deviceName": "Android Emulator"}}}'
        )

        httpretty.register_uri(
            httpretty.GET,
            'http://localhost:4723/wd/hub/session/another-session-id/title',
            body='{ "value": "title on another session id"}'
        )

        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'app': 'path/to/app',
            'automationName': 'UIAutomator2'
        }
        driver = webdriver.Remote(
            'http://localhost:4723/wd/hub',
            desired_caps
        )

        # current session
        assert driver.session_id == 'session-id'

        # call against another session id
        driver.session_id = 'another-session-id'
        assert driver.title == 'title on another session id'
        assert driver.session_id == 'another-session-id'

    @httpretty.activate
    def test_create_session_register_uridirect(self):
        httpretty.register_uri(
            httpretty.POST,
            'http://localhost:4723/wd/hub/session',
            body=json.dumps({'value': {
                'sessionId': 'session-id',
                'capabilities': {
                    'deviceName': 'Android Emulator',
                    'directConnectProtocol': 'http',
                    'directConnectHost': 'localhost2',
                    'directConnectPort': 4800,
                    'directConnectPath': '/special/path/wd/hub',
                }
            }})
        )

        httpretty.register_uri(
            httpretty.GET,
            'http://localhost2:4800/special/path/wd/hub/session/session-id/contexts',
            body=json.dumps({'value': ['NATIVE_APP', 'CHROMIUM']})
        )

        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'app': 'path/to/app',
            'automationName': 'UIAutomator2'
        }
        driver = webdriver.Remote(
            'http://localhost:4723/wd/hub',
            desired_caps,
            direct_connection=True
        )

        assert 'http://localhost2:4800/special/path/wd/hub' == driver.command_executor._url
        assert ['NATIVE_APP', 'CHROMIUM'] == driver.contexts

    @httpretty.activate
    def test_create_session_register_uridirect_no_direct_connect_path(self):
        httpretty.register_uri(
            httpretty.POST,
            'http://localhost:4723/wd/hub/session',
            body=json.dumps({'value': {
                'sessionId': 'session-id',
                'capabilities': {
                    'deviceName': 'Android Emulator',
                    'directConnectProtocol': 'http',
                    'directConnectHost': 'localhost2',
                    'directConnectPort': 4800
                }
            }})
        )

        httpretty.register_uri(
            httpretty.GET,
            'http://localhost:4723/wd/hub/session/session-id/contexts',
            body=json.dumps({'value': ['NATIVE_APP', 'CHROMIUM']})
        )

        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'app': 'path/to/app',
            'automationName': 'UIAutomator2'
        }
        driver = webdriver.Remote(
            'http://localhost:4723/wd/hub',
            desired_caps,
            direct_connection=True
        )

        assert 'http://localhost:4723/wd/hub' == driver.command_executor._url
        assert ['NATIVE_APP', 'CHROMIUM'] == driver.contexts

    @httpretty.activate
    def test_get_all_sessions(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/sessions'),
            body=json.dumps({'value': {'deviceName': 'iPhone Simulator', 'events': {'simStarted': [1234567891]}}})
        )
        session = driver.all_sessions
        assert len(session) != 1

    @httpretty.activate
    def test_get_session(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890'),
            body=json.dumps({'value': {'deviceName': 'iPhone Simulator', 'events': {'simStarted': [1234567890]}}})
        )
        session = driver.session
        assert session['deviceName'] == 'iPhone Simulator'
        assert session['events']['simStarted'] == [1234567890]

    @httpretty.activate
    def test_get_events(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890'),
            body=json.dumps({'value': {'events': {'simStarted': [1234567890]}}})
        )
        events = driver.events
        assert events['simStarted'] == [1234567890]

    @httpretty.activate
    def test_get_events_catches_missing_events(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890'),
            body=json.dumps({'value': {}})
        )
        events = driver.events
        assert events == {}
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890'),
            body=json.dumps({})
        )
        events = driver.events
        assert events == {}

    @httpretty.activate
    @patch("appium.webdriver.webdriver.logger.warning")
    def test_session_catches_error(self, mock_warning):
        def exceptionCallback(request, uri, headers):
            raise Exception()

        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890'),
            body=exceptionCallback
        )
        events = driver.events
        mock_warning.assert_called_once()
        assert events == {}


class SubWebDriver(WebDriver):
    def __init__(self, command_executor, desired_capabilities, direct_connection=False):
        super().__init__(
            command_executor=command_executor,
            desired_capabilities=desired_capabilities,
            direct_connection=direct_connection
        )


class SubSubWebDriver(SubWebDriver):
    def __init__(self, command_executor, desired_capabilities, direct_connection=False):
        super().__init__(
            command_executor=command_executor,
            desired_capabilities=desired_capabilities,
            direct_connection=direct_connection
        )


class TestSubModuleWebDriver(object):
    def android_w3c_driver(self, driver_class):
        response_body_json = json.dumps(
            {
                'value': {
                    'sessionId': '1234567890',
                    'capabilities': {
                        'platform': 'LINUX',
                        'desired': {
                            'platformName': 'Android',
                            'automationName': 'uiautomator2',
                            'platformVersion': '7.1.1',
                            'deviceName': 'Android Emulator',
                            'app': '/test/apps/ApiDemos-debug.apk',
                        },
                        'platformName': 'Android',
                        'automationName': 'uiautomator2',
                        'platformVersion': '7.1.1',
                        'deviceName': 'emulator-5554',
                        'app': '/test/apps/ApiDemos-debug.apk',
                        'deviceUDID': 'emulator-5554',
                        'appPackage': 'io.appium.android.apis',
                        'appWaitPackage': 'io.appium.android.apis',
                        'appActivity': 'io.appium.android.apis.ApiDemos',
                        'appWaitActivity': 'io.appium.android.apis.ApiDemos'
                    }
                }
            }
        )

        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session'),
            body=response_body_json
        )

        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'app': 'path/to/app',
            'automationName': 'UIAutomator2'
        }

        driver = driver_class(
            'http://localhost:4723/wd/hub',
            desired_caps
        )
        return driver

    @httpretty.activate
    def test_clipboard_with_subclass(self):
        driver = self.android_w3c_driver(SubWebDriver)
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/context'),
            body='{"value": "NATIVE"}'
        )
        assert driver.current_context == 'NATIVE'

    @httpretty.activate
    def test_clipboard_with_subsubclass(self):
        driver = self.android_w3c_driver(SubSubWebDriver)
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/context'),
            body='{"value": "NATIVE"}'
        )
        assert driver.current_context == 'NATIVE'

    @httpretty.activate
    def test_compare_commands(self):
        driver_base = android_w3c_driver()
        driver_sub = self.android_w3c_driver(SubWebDriver)
        driver_subsub = self.android_w3c_driver(SubSubWebDriver)

        assert len(driver_base.command_executor._commands) == len(driver_sub.command_executor._commands)
        assert len(driver_base.command_executor._commands) == len(driver_subsub.command_executor._commands)
