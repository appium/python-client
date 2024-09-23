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

from test.unit.helper.test_helper import android_w3c_driver, appium_command, get_httpretty_request_body


class TestWebDriverContext(object):
    @httpretty.activate
    def test_current_contexts(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET, appium_command('/session/1234567890/context'), body='{"value": "NATIVE_APP"}'
        )
        assert driver.current_context == 'NATIVE_APP'

    @httpretty.activate
    def test_get_contexts(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET, appium_command('/session/1234567890/contexts'), body='{"value": ["NATIVE_APP", "CHROMIUM"]}'
        )

        assert ['NATIVE_APP', 'CHROMIUM'] == driver.contexts

    @httpretty.activate
    def test_switch_to_context(self):
        driver = android_w3c_driver()
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/context'), body='{"value": null}')

        driver.switch_to.context(None)

        assert {'name': None}, get_httpretty_request_body(httpretty.last_request())

    @httpretty.activate
    def test_switch_to_context_native_app(self):
        driver = android_w3c_driver()
        httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/context'), body='{"value": null}')

        driver.switch_to.context('NATIVE_APP')

        assert {'name': 'NATIVE_APP'}, get_httpretty_request_body(httpretty.last_request())
