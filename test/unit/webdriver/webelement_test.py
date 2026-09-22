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
import tempfile

import httpretty

from appium.protocols.webdriver.can_find_elements import CanFindElements
from appium.webdriver.webelement import WebElement as MobileWebElement
from test.unit.helper.test_helper import android_w3c_driver, appium_command, get_httpretty_request_body


class TestWebElement:
    @httpretty.activate
    def test_status(self):
        driver = android_w3c_driver()
        response = {'ready': True, 'message': {'build': {'version': '2.0.0', 'revision': None}}}
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/status'),
            body=json.dumps({'value': response}),
        )
        s = driver.get_status()

        assert s == response

    @httpretty.activate
    def test_send_key(self):
        driver = android_w3c_driver()
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/element/element_id/value'))

        element = MobileWebElement(driver, 'element_id')
        element.send_keys('happy testing')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['text'] == ''.join(d['value'])

    @httpretty.activate
    def test_send_key_with_file(self):
        driver = android_w3c_driver()
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/element/element_id/value'))

        # Should not send this file
        with tempfile.NamedTemporaryFile() as tmp_f:
            element = MobileWebElement(driver, 'element_id')
            element.send_keys(tmp_f.name)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['text'] == ''.join(d['value'])

    @httpretty.activate
    def test_clear(self):
        driver = android_w3c_driver()
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/element/element_id/clear'))

        element = MobileWebElement(driver, 'element_id')
        element.clear()

    @httpretty.activate
    def test_get_attribute_with_dict(self):
        driver = android_w3c_driver()
        rect_dict = {'y': 200, 'x': 100, 'width': 300, 'height': 56}
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/element/element_id/attribute/rect'),
            body=json.dumps({'value': rect_dict}),
        )

        element = MobileWebElement(driver, 'element_id')
        ef = element.get_attribute('rect')

        httpretty.last_request()

        assert isinstance(ef, dict)
        assert ef == rect_dict

    @httpretty.activate
    def test_element_location_in_view(self):
        driver = android_w3c_driver()
        location_in_view = {'y': 200, 'x': 100}
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/element/element_id/location_in_view'),
            body=json.dumps({'value': location_in_view}),
        )

        element = MobileWebElement(driver, 'element_id')
        loc = element.location_in_view

        httpretty.last_request()

        assert loc == location_in_view

    @httpretty.activate
    def test_find_element_default_by(self):
        driver = android_w3c_driver()
        element = MobileWebElement(driver, 'element_id')
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element/element_id/element'),
            body='{"value": {"element-6066-11e4-a52e-4f735466cecf": "child-element-id"}}',
        )

        el = element.find_element(value='child_id')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == 'id'
        assert d['value'] == 'child_id'
        assert isinstance(el, MobileWebElement)
        assert el.id == 'child-element-id'

    @httpretty.activate
    def test_find_elements_default_by(self):
        driver = android_w3c_driver()
        element = MobileWebElement(driver, 'element_id')
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element/element_id/elements'),
            body='{"value": [{"element-6066-11e4-a52e-4f735466cecf": "child-1"}, {"element-6066-11e4-a52e-4f735466cecf": "child-2"}]}',
        )

        els = element.find_elements(value='child_ids')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == 'id'
        assert d['value'] == 'child_ids'
        assert len(els) == 2
        assert isinstance(els[0], MobileWebElement)
        assert els[0].id == 'child-1'
        assert isinstance(els[1], MobileWebElement)
        assert els[1].id == 'child-2'

    @httpretty.activate
    def test_can_find_elements_protocol_conformance(self):
        driver = android_w3c_driver()
        element = MobileWebElement(driver, 'element_id')

        assert isinstance(element, CanFindElements)
        assert isinstance(driver, CanFindElements)
