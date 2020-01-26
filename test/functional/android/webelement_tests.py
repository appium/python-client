#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

from appium.webdriver.common.mobileby import MobileBy

from .helper.test_helper import (
    APIDEMO_PKG_NAME,
    BaseTestCase,
    wait_for_element
)


class TestWebelement(BaseTestCase):
    def test_element_location_in_view(self) -> None:
        el = self.driver.find_element_by_accessibility_id('Content')
        loc = el.location_in_view
        assert loc['x'] is not None
        assert loc['y'] is not None

    def test_set_text(self) -> None:
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Views").instance(0));').click()

        wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Controls').click()
        wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, '1. Light Theme').click()

        el = wait_for_element(self.driver, MobileBy.CLASS_NAME, 'android.widget.EditText')
        el.send_keys('original text')
        el.set_text('new text')

        assert 'new text' == el.text

    def test_send_keys(self) -> None:
        for text in ['App', 'Activity', 'Custom Title']:
            wait_for_element(self.driver, MobileBy.XPATH,
                             f"//android.widget.TextView[@text='{text}']").click()

        el = wait_for_element(self.driver, MobileBy.ID, '{}:id/left_text_edit'.format(APIDEMO_PKG_NAME))
        el.send_keys(' text')

        assert 'Left is best text' == el.text
