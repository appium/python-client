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

import textwrap

import httpretty

from test.unit.helper.test_helper import (
    android_w3c_driver,
    appium_command,
    get_httpretty_request_body
)


class TestWebDriverExecuteDriver(object):

    @httpretty.activate
    def test_batch(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/execute_driver'),
            body='{"value": {"result":['
            '{"element-6066-11e4-a52e-4f735466cecf":"39000000-0000-0000-D39A-000000000000",'
            '"ELEMENT":"39000000-0000-0000-D39A-000000000000"},'
            '{"y":237,"x":18,"width":67,"height":24}],"logs":{'
            '"error":[],"warn":["warning message"],"log":[]}}}'
        )

        script = """
            console.warn('warning message');
            const element = await driver.findElement('accessibility id', 'Buttons');
            const rect = await driver.getElementRect(element.ELEMENT);
            return [element, rect];
        """
        response = driver.execute_driver(script=textwrap.dedent(script))
        # Python client convert an element item as WebElement in the result
        assert response.result[0].id == '39000000-0000-0000-D39A-000000000000'
        assert response.result[1]['y'] == 237
        assert response.logs['warn'] == ['warning message']

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['script'] == textwrap.dedent(script)
        assert d['type'] == 'webdriverio'
        assert 'timeout' not in d

    @httpretty.activate
    def test_batch_with_timeout(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/execute_driver'),
            body='{"value": {"result":['
            '{"element-6066-11e4-a52e-4f735466cecf":"39000000-0000-0000-D39A-000000000000",'
            '"ELEMENT":"39000000-0000-0000-D39A-000000000000"},'
            '{"y":237,"x":18,"width":67,"height":24}],"logs":{'
            '"error":[],"warn":["warning message"],"log":[]}}}'
        )

        script = """
            console.warn('warning message');
            const element = await driver.findElement('accessibility id', 'Buttons');
            const rect = await driver.getElementRect(element.ELEMENT);
            return [element, rect];
        """
        response = driver.execute_driver(script=textwrap.dedent(script), timeout_ms=10000)
        assert response.result[0].id == '39000000-0000-0000-D39A-000000000000'
        assert response.result[1]['y'] == 237
        assert response.logs['error'] == []

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['script'] == textwrap.dedent(script)
        assert d['type'] == 'webdriverio'
        assert d['timeout'] == 10000
