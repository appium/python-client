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

from .helper.desired_capabilities import get_desired_capabilities


class TestSafari:
    def setup_method(self) -> None:
        caps = get_desired_capabilities()
        caps.update({'browserName': 'safari', 'nativeWebTap': True, 'safariIgnoreFraudWarning': True})
        self.driver = webdriver.Remote('http://127.0.0.1:4723/', options=AppiumOptions().load_capabilities(caps))

    def teardown_method(self) -> None:
        self.driver.quit()

    def test_context(self) -> None:
        assert 'NATIVE_APP' == self.driver.contexts[0]
        assert self.driver.contexts[1].startswith('WEBVIEW_')
        assert 'WEBVIEW_' in self.driver.current_context

    def test_get(self) -> None:
        self.driver.get("http://google.com")
        for _ in range(5):
            time.sleep(0.5)
            if 'Google' == self.driver.title:
                return

        assert False, 'The title was wrong'
