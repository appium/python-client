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

from test.unit.helper.test_helper import (
    android_w3c_driver,
    appium_command,
    get_httpretty_request_body
)


class TestWebDriverPerformance(object):

    @httpretty.activate
    def test_get_performance_data(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/getPerformanceData'),
            body='{"value": [["user", "kernel"], ["2.5", "1.3"]]}'
        )
        assert driver.get_performance_data('my.app.package', 'cpuinfo', 5) == [['user', 'kernel'], ['2.5', '1.3']]

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['packageName'] == 'my.app.package'
        assert d['dataType'] == 'cpuinfo'
        assert d['dataReadTimeout'] == 5

    @httpretty.activate
    def test_get_performance_data_types(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/performanceData/types'),
            body='{"value": ["cpuinfo", "memoryinfo", "batteryinfo", "networkinfo"]}'
        )
        assert driver.get_performance_data_types() == ['cpuinfo', 'memoryinfo', 'batteryinfo', 'networkinfo']
