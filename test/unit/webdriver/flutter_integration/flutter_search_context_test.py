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

from appium.webdriver.common.appiumby import AppiumBy
from test.unit.helper.test_helper import appium_command, flutter_w3c_driver, get_httpretty_request_body


class TestFlutterSearchContext(object):

    @httpretty.activate
    def test_find_element_by_flutter_key(self):
        driver = flutter_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element'),
            body='{"value": {"element-6066-11e4-a52e-4f735466cecf": "element-id"}}',
        )
        el = driver.find_element(AppiumBy.FLUTTER_INTEGRATION_KEY, 'Flutter UI Key')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-flutter key'
        assert d['value'] == 'Flutter UI Key'
        assert el.id == 'element-id'

    @httpretty.activate
    def test_find_elements_by_flutter_key(self):
        driver = flutter_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/elements'),
            body='{"value": [{"element-6066-11e4-a52e-4f735466cecf": "child-element-id1"}, '
            '{"element-6066-11e4-a52e-4f735466cecf": "child-element-id2"}]}',
        )
        els = driver.find_elements(AppiumBy.FLUTTER_INTEGRATION_KEY, 'Flutter UI Key')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-flutter key'
        assert d['value'] == 'Flutter UI Key'
        assert els[0].id == 'child-element-id1'
        assert els[1].id == 'child-element-id2'

    @httpretty.activate
    def test_find_element_by_flutter_text(self):
        driver = flutter_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element'),
            body='{"value": {"element-6066-11e4-a52e-4f735466cecf": "element-id"}}',
        )
        el = driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TEXT, 'Flutter UI Text')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-flutter text'
        assert d['value'] == 'Flutter UI Text'
        assert el.id == 'element-id'

    @httpretty.activate
    def test_find_elements_by_flutter_text(self):
        driver = flutter_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/elements'),
            body='{"value": [{"element-6066-11e4-a52e-4f735466cecf": "child-element-id1"}, '
            '{"element-6066-11e4-a52e-4f735466cecf": "child-element-id2"}]}',
        )
        els = driver.find_elements(AppiumBy.FLUTTER_INTEGRATION_TEXT, 'Flutter UI Text')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-flutter text'
        assert d['value'] == 'Flutter UI Text'
        assert els[0].id == 'child-element-id1'
        assert els[1].id == 'child-element-id2'

    @httpretty.activate
    def test_find_element_by_flutter_semantics_label(self):
        driver = flutter_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element'),
            body='{"value": {"element-6066-11e4-a52e-4f735466cecf": "element-id"}}',
        )
        el = driver.find_element(AppiumBy.FLUTTER_INTEGRATION_SEMANTICS_LABEL, 'Flutter UI Semantics Label')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-flutter semantics label'
        assert d['value'] == 'Flutter UI Semantics Label'
        assert el.id == 'element-id'

    @httpretty.activate
    def test_find_elements_by_flutter_semantics_label(self):
        driver = flutter_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/elements'),
            body='{"value": [{"element-6066-11e4-a52e-4f735466cecf": "child-element-id1"}, '
            '{"element-6066-11e4-a52e-4f735466cecf": "child-element-id2"}]}',
        )
        els = driver.find_elements(AppiumBy.FLUTTER_INTEGRATION_SEMANTICS_LABEL, 'Flutter UI Semantics Label')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-flutter semantics label'
        assert d['value'] == 'Flutter UI Semantics Label'
        assert els[0].id == 'child-element-id1'
        assert els[1].id == 'child-element-id2'

    @httpretty.activate
    def test_find_element_by_flutter_type(self):
        driver = flutter_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element'),
            body='{"value": {"element-6066-11e4-a52e-4f735466cecf": "element-id"}}',
        )
        el = driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TYPE, 'Flutter UI Type')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-flutter type'
        assert d['value'] == 'Flutter UI Type'
        assert el.id == 'element-id'

    @httpretty.activate
    def test_find_elements_by_flutter_type(self):
        driver = flutter_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/elements'),
            body='{"value": [{"element-6066-11e4-a52e-4f735466cecf": "child-element-id1"}, '
            '{"element-6066-11e4-a52e-4f735466cecf": "child-element-id2"}]}',
        )
        els = driver.find_elements(AppiumBy.FLUTTER_INTEGRATION_TYPE, 'Flutter UI Type')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-flutter type'
        assert d['value'] == 'Flutter UI Type'
        assert els[0].id == 'child-element-id1'
        assert els[1].id == 'child-element-id2'

    @httpretty.activate
    def test_find_element_by_flutter_text_containing(self):
        driver = flutter_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element'),
            body='{"value": {"element-6066-11e4-a52e-4f735466cecf": "element-id"}}',
        )
        el = driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TEXT_CONTAINING, 'Flutter UI Partial Text')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-flutter text containing'
        assert d['value'] == 'Flutter UI Partial Text'
        assert el.id == 'element-id'

    @httpretty.activate
    def test_find_elements_by_flutter_text_containing(self):
        driver = flutter_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/elements'),
            body='{"value": [{"element-6066-11e4-a52e-4f735466cecf": "child-element-id1"}, '
            '{"element-6066-11e4-a52e-4f735466cecf": "child-element-id2"}]}',
        )
        els = driver.find_elements(AppiumBy.FLUTTER_INTEGRATION_TEXT_CONTAINING, 'Flutter UI Partial Text',)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-flutter text containing'
        assert d['value'] == 'Flutter UI Partial Text'
        assert els[0].id == 'child-element-id1'
        assert els[1].id == 'child-element-id2'
