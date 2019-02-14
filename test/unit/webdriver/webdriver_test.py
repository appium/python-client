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

from appium import version as appium_version

from test.unit.helper.test_helper import (
    appium_command,
    android_w3c_driver,
    get_httpretty_request_body
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
    def test_find_element_by_android_data_matcher(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element'),
            body='{"value": {"element-6066-11e4-a52e-4f735466cecf": "element-id"}}'
        )
        el = driver.find_element_by_android_data_matcher(
            name='title', args=['title', 'Animation'], className='class name')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d == {'sessionId': '1234567890', 'using': '-android datamatcher',
                     'value': '{"args": ["title", "Animation"], "name": "title", "class": "class name"}'}
        assert el.id == 'element-id'

    @httpretty.activate
    def test_find_elements_by_android_data_matcher(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/elements'),
            body='{"value": [{"element-6066-11e4-a52e-4f735466cecf": "element-id1"}, {"element-6066-11e4-a52e-4f735466cecf": "element-id2"}]}'
        )
        els = driver.find_elements_by_android_data_matcher(name='title', args=['title', 'Animation'])

        d = get_httpretty_request_body(httpretty.last_request())
        assert d == {'sessionId': '1234567890', 'using': '-android datamatcher',
                     'value': '{"args": ["title", "Animation"], "name": "title"}'}
        assert els[0].id == 'element-id1'
        assert els[1].id == 'element-id2'
