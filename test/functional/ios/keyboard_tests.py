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

from time import sleep

from test.functional.ios.helper.test_helper import BaseTestCase


class TestKeyboard(BaseTestCase):
    def test_hide_keyboard(self) -> None:
        self._move_to_textbox()

        el = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]
        el.click()
        el.set_value('Testing')

        el = self.driver.find_element_by_class_name('UIAKeyboard')
        assert el.is_displayed()

        self.driver.hide_keyboard(key_name='Done')

        assert not el.is_displayed()

    def test_hide_keyboard_presskey_strategy(self) -> None:
        self._move_to_textbox()

        el = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]
        el.click()
        el.set_value('Testing')

        el = self.driver.find_element_by_class_name('UIAKeyboard')
        assert el.is_displayed()

        self.driver.hide_keyboard(strategy='pressKey', key='Done')

        assert not el.is_displayed()

    def test_hide_keyboard_no_key_name(self) -> None:
        self._move_to_textbox()

        el = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]
        el.click()
        el.set_value('Testing')

        el = self.driver.find_element_by_class_name('UIAKeyboard')
        assert el.is_displayed()

        self.driver.hide_keyboard()
        sleep(10)

        # currently fails.
        assert not el.is_displayed()

    def test_is_keyboard_shown(self) -> None:
        self._move_to_textbox()

        el = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]
        el.click()
        el.set_value('Testing')
        assert self.driver.is_keyboard_shown()

    def _move_to_textbox(self) -> None:
        el1 = self.driver.find_element_by_accessibility_id('Sliders')
        el2 = self.driver.find_element_by_accessibility_id('Buttons')
        self.driver.scroll(el1, el2)

        # Click text fields
        self.driver.find_element_by_accessibility_id('Text Fields').click()
