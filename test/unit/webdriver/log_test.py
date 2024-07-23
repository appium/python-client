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

from test.unit.helper.test_helper import appium_command, get_httpretty_request_body, ios_w3c_driver


class TestWebDriverLog(object):
    @httpretty.activate
    def test_get_log_types(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/log/types'),
            body=json.dumps({'value': ['syslog']}),
        )
        log_types = driver.log_types
        assert log_types == ['syslog']

    @httpretty.activate
    def test_get_log(self):
        driver = ios_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/log'),
            body=json.dumps({'value': ['logs as array']}),
        )
        log_types = driver.get_log('syslog')
        assert log_types == ['logs as array']

        d = get_httpretty_request_body(httpretty.last_request())
        assert {'type': 'syslog'} == d
