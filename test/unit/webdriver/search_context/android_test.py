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
import pytest

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webelement import WebElement as MobileWebElement
from test.unit.helper.test_helper import android_w3c_driver, appium_command, get_httpretty_request_body


class TestWebDriverAndroidSearchContext:
    @pytest.mark.parametrize('by', [AppiumBy, AppiumBy()])
    def test_android_uiautomator_deprecation(self, by):
        with pytest.warns(DeprecationWarning, match='Use ANDROID_PREDICATE or ANDROID_CLASS_CHAIN'):
            assert by.ANDROID_UIAUTOMATOR == '-android uiautomator'

    @pytest.mark.parametrize(
        ('by', 'strategy', 'selector'),
        [
            (AppiumBy.ID, 'id', 'id data'),
            (AppiumBy.ANDROID_TEXT, 'text', 'Sign in'),
            (AppiumBy.ANDROID_PREDICATE, '-android predicate string', "text == 'Gallery'"),
            (AppiumBy.ANDROID_CLASS_CHAIN, '-android class chain', '**/android.widget.Button[2]'),
        ],
    )
    @httpretty.activate
    def test_find_element(self, by, strategy, selector):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element'),
            body='{"value": {"element-6066-11e4-a52e-4f735466cecf": "element-id"}}',
        )
        el = driver.find_element(by=by, value=selector)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == strategy
        assert d['value'] == selector
        assert isinstance(el, MobileWebElement)

    @httpretty.activate
    def test_find_elements_by_id(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/elements'),
            body='{"value": [{"element-6066-11e4-a52e-4f735466cecf": "element-id1"}, '
            '{"element-6066-11e4-a52e-4f735466cecf": "element-id2"}]}',
        )
        els = driver.find_elements(
            by=AppiumBy.ID,
            value='id data',
        )

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == 'id'
        assert d['value'] == 'id data'
        assert isinstance(els[0], MobileWebElement)

    @httpretty.activate
    def test_find_child_element_by_id(self):
        driver = android_w3c_driver()
        element = MobileWebElement(driver, 'element_id')
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element/element_id/element'),
            body='{"value": {"element-6066-11e4-a52e-4f735466cecf": "child-element-id"}}',
        )
        el = element.find_element(
            by=AppiumBy.ID,
            value='id data',
        )

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == 'id'
        assert d['value'] == 'id data'
        assert isinstance(el, MobileWebElement)

    @httpretty.activate
    def test_find_element_by_android_data_matcher(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element'),
            body='{"value": {"element-6066-11e4-a52e-4f735466cecf": "element-id"}}',
        )
        el = driver.find_element(
            by=AppiumBy.ANDROID_DATA_MATCHER,
            value=json.dumps({'name': 'title', 'args': ['title', 'Animation'], 'class': 'class name'}),
        )

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-android datamatcher'
        value_dict = json.loads(d['value'])
        assert value_dict['args'] == ['title', 'Animation']
        assert value_dict['name'] == 'title'
        assert value_dict['class'] == 'class name'
        assert el.id == 'element-id'

    @httpretty.activate
    def test_find_elements_by_android_data_matcher(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/elements'),
            body='{"value": [{"element-6066-11e4-a52e-4f735466cecf": "element-id1"}, '
            '{"element-6066-11e4-a52e-4f735466cecf": "element-id2"}]}',
        )
        els = driver.find_elements(
            by=AppiumBy.ANDROID_DATA_MATCHER, value=json.dumps({'name': 'title', 'args': ['title', 'Animation']})
        )

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-android datamatcher'
        value_dict = json.loads(d['value'])
        assert value_dict['args'] == ['title', 'Animation']
        assert value_dict['name'] == 'title'
        assert els[0].id == 'element-id1'
        assert els[1].id == 'element-id2'

    @httpretty.activate
    def test_find_elements_by_android_data_matcher_no_value(self):
        driver = android_w3c_driver()
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/elements'), body='{"value": []}')
        els = driver.find_elements(by=AppiumBy.ANDROID_DATA_MATCHER, value='{}')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-android datamatcher'
        assert d['value'] == '{}'
        assert len(els) == 0

    @httpretty.activate
    def test_find_child_element_by_android_data_matcher(self):
        driver = android_w3c_driver()
        element = MobileWebElement(driver, 'element_id')
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element/element_id/element'),
            body='{"value": {"element-6066-11e4-a52e-4f735466cecf": "child-element-id"}}',
        )
        el = element.find_element(
            by=AppiumBy.ANDROID_DATA_MATCHER,
            value=json.dumps({'name': 'title', 'args': ['title', 'Animation'], 'class': 'class name'}),
        )

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-android datamatcher'
        value_dict = json.loads(d['value'])
        assert value_dict['args'] == ['title', 'Animation']
        assert value_dict['name'] == 'title'
        assert value_dict['class'] == 'class name'
        assert el.id == 'child-element-id'

    @httpretty.activate
    def test_find_child_elements_by_android_data_matcher(self):
        driver = android_w3c_driver()
        element = MobileWebElement(driver, 'element_id')
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element/element_id/elements'),
            body='{"value": [{"element-6066-11e4-a52e-4f735466cecf": "child-element-id1"}, '
            '{"element-6066-11e4-a52e-4f735466cecf": "child-element-id2"}]}',
        )
        els = element.find_elements(
            by=AppiumBy.ANDROID_DATA_MATCHER, value=json.dumps({'name': 'title', 'args': ['title', 'Animation']})
        )

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-android datamatcher'
        value_dict = json.loads(d['value'])
        assert value_dict['args'] == ['title', 'Animation']
        assert value_dict['name'] == 'title'
        assert els[0].id == 'child-element-id1'
        assert els[1].id == 'child-element-id2'

    @httpretty.activate
    def test_find_child_elements_by_android_data_matcher_no_value(self):
        driver = android_w3c_driver()
        element = MobileWebElement(driver, 'element_id')
        httpretty.register_uri(
            httpretty.POST, appium_command('/session/1234567890/element/element_id/elements'), body='{"value": []}'
        )
        els = element.find_elements(by=AppiumBy.ANDROID_DATA_MATCHER, value='{}')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-android datamatcher'
        assert d['value'] == '{}'
        assert len(els) == 0
