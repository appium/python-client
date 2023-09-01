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

from appium.webdriver.applicationstate import ApplicationState
from appium.webdriver.common.appiumby import AppiumBy
from test.functional.ios.helper.test_helper import BaseTestCase
from test.functional.test_helper import wait_for_condition

from .helper import desired_capabilities


class TestWebDriver(BaseTestCase):
    def test_app_management(self) -> None:
        # this only works in Xcode9+
        if float(desired_capabilities.get_desired_capabilities(desired_capabilities.BUNDLE_ID)['platformVersion']) < 11:
            return
        assert self.driver.query_app_state(desired_capabilities.BUNDLE_ID) == ApplicationState.RUNNING_IN_FOREGROUND
        self.driver.background_app(-1)
        print(self.driver.query_app_state(desired_capabilities.BUNDLE_ID) < ApplicationState.RUNNING_IN_FOREGROUND)
        assert wait_for_condition(
            lambda: self.driver.query_app_state(desired_capabilities.BUNDLE_ID)
            < ApplicationState.RUNNING_IN_FOREGROUND,
        ), 'The app didn\'t go to background.'
        self.driver.activate_app(desired_capabilities.BUNDLE_ID)
        assert self.driver.query_app_state(desired_capabilities.BUNDLE_ID) == ApplicationState.RUNNING_IN_FOREGROUND

    def test_clear(self) -> None:
        self._move_to_textbox()

        el = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='XCUIElementTypeTextField')[0]

        # Verify default text
        def_text = 'Placeholder text'
        text = el.get_attribute('value')
        assert text == def_text

        # Input some text, verify
        input_text = 'blah'
        el.click()
        el.send_keys(input_text)
        self.driver.hide_keyboard()

        # TODO Needs to get the element again to update value in the element. Remove below one line when it's fixed.
        el = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='XCUIElementTypeTextField')[0]
        text = el.get_attribute('value')
        assert text == input_text

        # Clear text, verify
        el.clear()
        text = el.get_attribute('value')
        assert text == def_text

    def test_press_button(self) -> None:
        self.driver.press_button('Home')
        if float(desired_capabilities.get_desired_capabilities(desired_capabilities.BUNDLE_ID)['platformVersion']) < 11:
            return
        assert self.driver.query_app_state(desired_capabilities.BUNDLE_ID) == ApplicationState.RUNNING_IN_FOREGROUND

    def _move_to_textbox(self) -> None:
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Sliders')
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Buttons')
        self.driver.scroll(el1, el2)

        # Click text fields
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Text Fields').click()
