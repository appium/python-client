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

from appium.webdriver.common.mobileby import MobileBy
from test.functional.android.helper.test_helper import (
    BaseTestCase,
    is_ci,
    wait_for_element
)


class TestFindByAccessibilityID(BaseTestCase):
    def test_find_single_element(self) -> None:
        wait_for_element(self.driver, MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Accessibility")').click()
        wait_for_element(self.driver, MobileBy.ANDROID_UIAUTOMATOR,
                         'new UiSelector().text("Accessibility Node Querying")').click()
        el = wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Task Take out Trash')
        assert el is not None

    def test_find_multiple_elements(self) -> None:
        els = self.driver.find_elements_by_accessibility_id('Accessibility')
        assert isinstance(els, list)

    @pytest.mark.skipif(condition=is_ci(), reason='Need to fix flaky test during running on CI')
    def test_element_find_single_element(self) -> None:
        wait_for_element(self.driver, MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Accessibility")').click()
        wait_for_element(self.driver, MobileBy.ANDROID_UIAUTOMATOR,
                         'new UiSelector().text("Accessibility Node Querying")').click()
        el = wait_for_element(self.driver, MobileBy.CLASS_NAME, 'android.widget.ListView')

        sub_el = el.find_element_by_accessibility_id('Task Take out Trash')
        assert sub_el is not None

    def test_element_find_multiple_elements(self) -> None:
        wait_for_element(self.driver, MobileBy.CLASS_NAME, 'android.widget.ListView')
        el = self.driver.find_element_by_class_name('android.widget.ListView')

        sub_els = el.find_elements_by_accessibility_id('Animation')
        assert isinstance(sub_els, list)
