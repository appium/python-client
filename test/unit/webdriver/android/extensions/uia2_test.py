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

from appium.webdriver.webelement import WebElement as MobileWebElement
from test.unit.helper.test_helper import (
    android_w3c_driver,
    appium_command,
    get_httpretty_request_body
)


class TestUia2(object):

    @httpretty.activate
    def test_flick_uia2_with_element(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/touch/flick')
        )

        el = MobileWebElement(driver, 'element_id', w3c=True)
        driver.flick_uia2(el, xoffset=0, yoffset=100, speed=100)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['element'] == 'element_id'
        assert d['xoffset'] == 0
        assert d['yoffset'] == 100
        assert d['speed'] == 100
        assert d.get('xspeed', -1) == -1
        assert d.get('yspeed', -1) == -1

    @httpretty.activate
    def test_flick_uia2_without_element(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/touch/flick')
        )

        driver.flick_uia2(xspeed=0, yspeed=100)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['xspeed'] == 0
        assert d['yspeed'] == 100
        assert d.get('element', 'foo') == 'foo'
        assert d.get('xoffset', -1) == -1
        assert d.get('yoffset', -1) == -1
