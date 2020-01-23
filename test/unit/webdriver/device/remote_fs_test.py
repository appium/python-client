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
import pytest
from selenium.common.exceptions import InvalidArgumentException

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
        )
        dest_path = '/path/to/file.txt'
        data = base64.b64encode(bytes('HelloWorld', 'utf-8')).decode('utf-8')

        assert isinstance(driver.push_file(dest_path, data), WebDriver)

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['path'] == dest_path
        assert d['data'] == str(data)

    @httpretty.activate
    def test_push_file_invalid_arg_exception_without_src_path_and_base64data(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/push_file'),
        )
        dest_path = '/path/to/file.txt'

        with pytest.raises(InvalidArgumentException):
            driver.push_file(dest_path)

    @httpretty.activate
    def test_push_file_invalid_arg_exception_with_src_file_not_found(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/push_file'),
        )
        dest_path = '/dest_path/to/file.txt'
        src_path = '/src_path/to/file.txt'

        with pytest.raises(InvalidArgumentException):
            driver.push_file(dest_path, source_path=src_path)

    @httpretty.activate
    def test_pull_file(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/pull_file'),
            body='{"value": "SGVsbG9Xb3JsZA=="}'
        )
        dest_path = '/path/to/file.txt'

        assert driver.pull_file(dest_path) == str(base64.b64encode(bytes('HelloWorld', 'utf-8')).decode('utf-8'))

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['path'] == dest_path

    @httpretty.activate
    def test_pull_folder(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/device/pull_folder'),
            body='{"value": "base64EncodedZippedFolderData"}'
        )
        dest_path = '/path/to/file.txt'

        assert driver.pull_folder(dest_path) == 'base64EncodedZippedFolderData'

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['path'] == dest_path
