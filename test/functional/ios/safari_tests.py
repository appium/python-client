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

from appium import webdriver

from .helper.desired_capabilities import get_desired_capabilities


class TestSafari(object):
    def setup_method(self) -> None:
        desired_caps = get_desired_capabilities()
        desired_caps.update({
            'browserName': 'safari',
            'nativeWebTap': True,
            'safariIgnoreFraudWarning': True
        })

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def teardown_method(self) -> None:
        self.driver.quit()

    def test_context(self) -> None:
        assert 'NATIVE_APP' == self.driver.contexts[0]
        assert self.driver.contexts[1].startswith('WEBVIEW_')
        assert 'WEBVIEW_' in self.driver.current_context

    def test_get(self) -> None:
        self.driver.get("http://google.com")
        assert 'Google' == self.driver.title
