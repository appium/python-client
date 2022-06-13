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

import pytest

from appium import webdriver
from appium.common.exceptions import NoSuchContextException
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from test.helpers.constants import SERVER_URL_BASE

from .helper import desired_capabilities


@pytest.mark.skip(reason="Need to fix broken test")
class TestContextSwitching(object):
    def setup_method(self) -> None:
        caps = desired_capabilities.get_desired_capabilities('selendroid-test-app.apk')
        self.driver = webdriver.Remote(SERVER_URL_BASE, options=AppiumOptions().load_capabilities(caps))

    def teardown_method(self) -> None:
        self.driver.quit()

    def test_contexts_list(self) -> None:
        self._enter_webview()
        contexts = self.driver.contexts
        assert 2 == len(contexts)

    def test_move_to_correct_context(self) -> None:
        self._enter_webview()
        assert 'WEBVIEW_io.selendroid.testapp' == self.driver.current_context

    def test_actually_in_webview(self) -> None:
        self._enter_webview()
        self.driver.find_element(by=AppiumBy.CSS_SELECTOR, value='input[type=submit]').click()
        el = self.driver.find_element(by=AppiumBy.XPATH, value="//h1[contains(., 'This is my way')]")
        assert el is not None

    def test_move_back_to_native_context(self) -> None:
        self._enter_webview()
        self.driver.switch_to.context(None)
        assert 'NATIVE_APP' == self.driver.current_context

    def test_set_invalid_context(self) -> None:
        with pytest.raises(NoSuchContextException):
            self.driver.switch_to.context('invalid name')

    def _enter_webview(self) -> None:
        btn = self.driver.find_element(by=AppiumBy.NAME, value='buttonStartWebviewCD')
        btn.click()
        self.driver.switch_to.context('WEBVIEW')
