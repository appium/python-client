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

import time

from appium import webdriver
from appium.options.common import AppiumOptions
from test.helpers.constants import SERVER_URL_BASE

from .helper.desired_capabilities import get_desired_capabilities


class TestSafari:
    def setup_method(self) -> None:
        caps = get_desired_capabilities()
        caps.update(
            {
                'bundleId': 'com.apple.mobilesafari',
                'nativeWebTap': True,
                'safariIgnoreFraudWarning': True,
                'webviewConnectTimeout': 100000
            }
        )
        self.driver = webdriver.Remote(SERVER_URL_BASE, options=AppiumOptions().load_capabilities(caps))

        # Fresh iOS 17.4 simulator may not show up the webview context with "safari"
        self.driver.terminate_app('com.apple.mobilesafari')
        self.driver.activate_app('com.apple.mobilesafari')

    def teardown_method(self) -> None:
        self.driver.quit()

    def test_context(self) -> None:
        contexts = self.driver.contexts
        assert 'NATIVE_APP' == contexts[0]
        assert contexts[1].startswith('WEBVIEW_')
        self.driver.switch_to.context(contexts[1])
        assert 'WEBVIEW_' in self.driver.current_context

    def test_get(self) -> None:
        ok = False
        contexts = self.driver.contexts
        for context in contexts:
            if context.startswith('WEBVIEW_'):
                self.driver.switch_to.context(context)
                ok = True
                break

        if ok is False:
            assert False, 'Could not set WEBVIEW context'


        self.driver.get('http://google.com')
        for _ in range(5):
            time.sleep(0.5)
            if 'Google' == self.driver.title:
                return

        assert False, 'The title was wrong'
