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
import os
import tempfile

import httpretty

from appium.webdriver.webelement import WebElement as MobileWebElement
from test.unit.helper.test_helper import (
    android_w3c_driver,
    appium_command,
    get_httpretty_request_body
)


class TestWebElement(object):

    @httpretty.activate
    def test_send_key(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element/element_id/value')
        )

        element = MobileWebElement(driver, 'element_id', w3c=True)
        element.send_keys('happy testing')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['text'] == ''.join(d['value'])

    @httpretty.activate
    def test_send_key_with_file(self):
        driver = android_w3c_driver()
        # Should not send this file
        tmp_f = tempfile.NamedTemporaryFile()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element/element_id/value')
        )

        try:
            element = MobileWebElement(driver, 'element_id', w3c=True)
            element.send_keys(tmp_f.name)
        finally:
            tmp_f.close()

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['text'] == ''.join(d['value'])
