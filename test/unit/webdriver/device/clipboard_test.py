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

from appium.webdriver.clipboard_content_type import ClipboardContentType
from test.unit.helper.test_helper import (
    android_w3c_driver,
    appium_command,
    get_httpretty_request_body,
    ios_w3c_driver
)


class TestWebDriverClipboard(object):

    @httpretty.activate
    def test_set_clipboard_with_url(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/set_clipboard'),
            body='{"value": ""}'
        )
        driver.set_clipboard(bytes(str('http://appium.io/'), 'UTF-8'),
                             ClipboardContentType.URL, 'label for android')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['content'] == 'aHR0cDovL2FwcGl1bS5pby8='
        assert d['contentType'] == 'url'
        assert d['label'] == 'label for android'

    @httpretty.activate
    def test_set_clipboard_text(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/set_clipboard'),
            body='{"value": ""}'
        )
        driver.set_clipboard_text('hello')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['content'] == 'aGVsbG8='
        assert d['contentType'] == 'plaintext'
