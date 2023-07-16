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
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from appium import webdriver
from appium.common.exceptions import NoSuchContextException
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from test.helpers.constants import SERVER_URL_BASE

from .helper import desired_capabilities


class TestContextSwitching(object):
    def setup_method(self) -> None:
        caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk.zip')
        self.driver = webdriver.Remote(SERVER_URL_BASE, options=AppiumOptions().load_capabilities(caps))

    def teardown_method(self) -> None:
        self.driver.quit()

    def test_contexts_list(self) -> None:
        self._enter_webview()
        contexts = self.driver.contexts
        assert 2 == len(contexts)

    def test_move_to_correct_context(self) -> None:
        self._enter_webview()
        assert 'WEBVIEW_io.appium.android.apis' == self.driver.current_context

    def test_actually_in_webview(self) -> None:
        self._enter_webview()
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//a[@id="i am a link"]')
        assert el is not None

    def test_move_back_to_native_context(self) -> None:
        self._enter_webview()
        self.driver.switch_to.context(None)
        assert 'NATIVE_APP' == self.driver.current_context

    def test_set_invalid_context(self) -> None:
        with pytest.raises(NoSuchContextException):
            self.driver.switch_to.context('invalid name')

    def _enter_webview(self) -> None:
        btn = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views')
        btn.click()
        self._scroll_to_webview()
        self._scroll_to_webview()
        btn_web_view = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='WebView')
        btn_web_view.click()
        self.driver.switch_to.context('WEBVIEW')

    def _scroll_to_webview(self) -> None:
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(393, 1915)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(462, 355)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
