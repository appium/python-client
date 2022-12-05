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

from typing import TYPE_CHECKING

import pytest
from selenium.webdriver.support.ui import WebDriverWait

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.applicationstate import ApplicationState
from appium.webdriver.common.appiumby import AppiumBy
from test.functional.ios.helper.test_helper import BaseTestCase
from test.functional.test_helper import (
    get_available_from_port_range,
    wait_for_condition,
)
from test.helpers.constants import SERVER_URL_BASE

from ..test_helper import is_ci
from .helper import desired_capabilities

if TYPE_CHECKING:
    from appium.webdriver.webdriver import WebDriver


class TestWebDriver(BaseTestCase):

    # TODO Due to not created 2nd session somehow
    @pytest.mark.skipif(
        condition=is_ci(), reason="Need to fix flaky test during running on CI."
    )
    def test_all_sessions(self) -> None:
        port = get_available_from_port_range(8200, 8300)
        caps = desired_capabilities.get_desired_capabilities("UICatalog.app.zip")
        caps["deviceName"] = "iPhone Xs Max"
        caps["wdaLocalPort"] = port

        class session_counts_is_two:
            TIMEOUT = 10

            def __call__(self, driver: "WebDriver") -> bool:
                return len(driver.all_sessions) == 2

        driver2 = None
        try:
            driver2 = webdriver.Remote(
                SERVER_URL_BASE, options=AppiumOptions().load_capabilities(caps)
            )
            WebDriverWait(driver2, session_counts_is_two.TIMEOUT).until(
                session_counts_is_two()
            )
            assert len(self.driver.all_sessions) == 2
        finally:
            if driver2 is not None:
                driver2.quit()

    def test_app_management(self) -> None:
        # this only works in Xcode9+
        if (
            float(
                desired_capabilities.get_desired_capabilities(
                    desired_capabilities.BUNDLE_ID
                )["platformVersion"]
            )
            < 11
        ):
            return
        assert (
            self.driver.query_app_state(desired_capabilities.BUNDLE_ID)
            == ApplicationState.RUNNING_IN_FOREGROUND
        )
        self.driver.background_app(-1)
        print(
            self.driver.query_app_state(desired_capabilities.BUNDLE_ID)
            < ApplicationState.RUNNING_IN_FOREGROUND
        )
        assert wait_for_condition(
            lambda: self.driver.query_app_state(desired_capabilities.BUNDLE_ID)
            < ApplicationState.RUNNING_IN_FOREGROUND,
        ), "The app didn't go to background."
        self.driver.activate_app(desired_capabilities.BUNDLE_ID)
        assert (
            self.driver.query_app_state(desired_capabilities.BUNDLE_ID)
            == ApplicationState.RUNNING_IN_FOREGROUND
        )

    def test_clear(self) -> None:
        self._move_to_textbox()

        el = self.driver.find_elements(
            by=AppiumBy.CLASS_NAME, value="XCUIElementTypeTextField"
        )[0]

        # Verify default text
        def_text = "Placeholder text"
        text = el.get_attribute("value")
        assert text == def_text

        # Input some text, verify
        input_text = "blah"
        el.click()
        el.send_keys(input_text)
        self.driver.hide_keyboard()

        # TODO Needs to get the element again to update value in the element. Remove below one line when it's fixed.
        el = self.driver.find_elements(
            by=AppiumBy.CLASS_NAME, value="XCUIElementTypeTextField"
        )[0]
        text = el.get_attribute("value")
        assert text == input_text

        # Clear text, verify
        el.clear()
        text = el.get_attribute("value")
        assert text == def_text

    def test_press_button(self) -> None:
        self.driver.press_button("Home")
        if (
            float(
                desired_capabilities.get_desired_capabilities(
                    desired_capabilities.BUNDLE_ID
                )["platformVersion"]
            )
            < 11
        ):
            return
        assert (
            self.driver.query_app_state(desired_capabilities.BUNDLE_ID)
            == ApplicationState.RUNNING_IN_FOREGROUND
        )

    def _move_to_textbox(self) -> None:
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Sliders")
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Buttons")
        self.driver.scroll(el1, el2)

        # Click text fields
        self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="Text Fields"
        ).click()
