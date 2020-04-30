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

from test.functional.android.helper.test_helper import BaseTestCase


@pytest.mark.skip(reason="Need to fix flaky test")
class TestFindByUIAutomator(BaseTestCase):
    def test_find_single_element(self) -> None:
        el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Animation")')
        assert el is not None

    def test_find_multiple_elements(self) -> None:
        els = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
        assert isinstance(els, list)

    def test_element_find_single_element(self) -> None:
        el = self.driver.find_element_by_class_name('android.widget.ListView')

        sub_el = el.find_element_by_android_uiautomator('new UiSelector().description("Animation")')
        assert sub_el is not None

    def test_element_find_multiple_elements(self) -> None:
        el = self.driver.find_element_by_class_name('android.widget.ListView')

        sub_els = el.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
        assert isinstance(sub_els, list)

    def test_scroll_into_view(self) -> None:
        el = self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Views").instance(0));')
        el.click()
        # TODO Add assert
