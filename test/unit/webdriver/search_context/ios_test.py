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
from appium.webdriver.webelement import WebElement as MobileWebElement
from test.unit.helper.test_helper import appium_command, get_httpretty_request_body, ios_w3c_driver


class TestWebDriverIOSSearchContext(object):
    @httpretty.activate
    def test_find_element_by_ios_predicate(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element'),
            body='{"value": {"element-6066-11e4-a52e-4f735466cecf": "element-id"}}',
        )
        el = driver.find_element(by=AppiumBy.IOS_PREDICATE, value='wdName == "UIKitCatalog"')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-ios predicate string'
        assert d['value'] == 'wdName == "UIKitCatalog"'
        assert el.id == 'element-id'

    @httpretty.activate
    def test_find_elements_by_ios_predicate(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/elements'),
            body='{"value": [{"element-6066-11e4-a52e-4f735466cecf": "element-id1"}, '
            '{"element-6066-11e4-a52e-4f735466cecf": "element-id2"}]}',
        )
        els = driver.find_elements(by=AppiumBy.IOS_PREDICATE, value='wdName == "UIKitCatalog"')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-ios predicate string'
        assert d['value'] == 'wdName == "UIKitCatalog"'
        assert els[0].id == 'element-id1'
        assert els[1].id == 'element-id2'

    @httpretty.activate
    def test_find_child_elements_by_ios_predicate(self):
        driver = ios_w3c_driver()
        element = MobileWebElement(driver, 'element_id')
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element/element_id/elements'),
            body='{"value": [{"element-6066-11e4-a52e-4f735466cecf": "child-element-id1"}, '
            '{"element-6066-11e4-a52e-4f735466cecf": "child-element-id2"}]}',
        )
        els = element.find_elements(by=AppiumBy.IOS_PREDICATE, value='wdName == "UIKitCatalog"')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-ios predicate string'
        assert d['value'] == 'wdName == "UIKitCatalog"'
        assert els[0].id == 'child-element-id1'
        assert els[1].id == 'child-element-id2'

    @httpretty.activate
    def test_find_element_by_ios_class_chain(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element'),
            body='{"value": {"element-6066-11e4-a52e-4f735466cecf": "element-id"}}',
        )
        el = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeStaticText')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-ios class chain'
        assert d['value'] == '**/XCUIElementTypeStaticText'
        assert el.id == 'element-id'

    @httpretty.activate
    def test_find_elements_by_ios_class_chain(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/elements'),
            body='{"value": [{"element-6066-11e4-a52e-4f735466cecf": "element-id1"}, '
            '{"element-6066-11e4-a52e-4f735466cecf": "element-id2"}]}',
        )
        els = driver.find_elements(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeStaticText')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-ios class chain'
        assert d['value'] == '**/XCUIElementTypeStaticText'
        assert els[0].id == 'element-id1'
        assert els[1].id == 'element-id2'

    @httpretty.activate
    def test_find_child_elements_by_ios_class_chain(self):
        driver = ios_w3c_driver()
        element = MobileWebElement(driver, 'element_id')
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element/element_id/elements'),
            body='{"value": [{"element-6066-11e4-a52e-4f735466cecf": "child-element-id1"}, '
            '{"element-6066-11e4-a52e-4f735466cecf": "child-element-id2"}]}',
        )
        els = element.find_elements(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeStaticText')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-ios class chain'
        assert d['value'] == '**/XCUIElementTypeStaticText'
        assert els[0].id == 'child-element-id1'
        assert els[1].id == 'child-element-id2'
