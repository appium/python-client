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

import base64

import httpretty

from appium.common.helper import appium_bytes
from appium.webdriver.webdriver import WebDriver
from test.unit.helper.test_helper import (
    android_w3c_driver,
    appium_command,
    get_httpretty_request_body
)


class TestWebDriverRemoteFs(object):

    @httpretty.activate
    def test_push_file(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/push_file'),
            body='{"path":"/path/to/file.txt","data":"SGVsbG9Xb3JsZA=="}'
        )
        dest_path = '/path/to/file.txt'
        data = base64.b64encode(appium_bytes('HelloWorld', 'utf-8')).decode('utf-8')

        assert isinstance(driver.push_file(dest_path, data), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['path'] == dest_path
        assert d['data'] == str(data)
