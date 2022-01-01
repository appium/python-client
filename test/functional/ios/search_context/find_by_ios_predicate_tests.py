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

from appium.webdriver.common.appiumby import AppiumBy
from test.functional.ios.helper.test_helper import BaseTestCase


class TestFindByIOSPredicate(BaseTestCase):
    def test_find_element_by_name(self) -> None:
        # Will throw exception if element is not found
        self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value='wdName == "Buttons"')

    def test_find_multiple_element_by_type(self) -> None:
        e = self.driver.find_elements(by=AppiumBy.IOS_PREDICATE, value='wdType == "XCUIElementTypeStaticText"')
        assert len(e) != 0

    def test_find_element_by_label(self) -> None:
        # Will throw exception if element is not found
        self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value='label == "Buttons"')

    def test_find_element_by_value(self) -> None:
        # Will throw exception if element is not found
        self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value='wdValue == "Buttons"')

    def test_find_element_by_isvisible(self) -> None:
        # Will throw exception if element is not found
        self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value='wdValue == "Buttons" AND visible == 1')

        # Should not find any elements
        e = self.driver.find_elements(by=AppiumBy.IOS_PREDICATE, value='wdValue == "Buttons" AND visible == 0')
        assert len(e) == 0

    def test_find_element_by_isenabled(self) -> None:
        # Will throw exception if element is not found
        self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value='wdValue == "Buttons" AND enabled == 1')

        # Should not find any elements
        e = self.driver.find_elements(by=AppiumBy.IOS_PREDICATE, value='wdValue == "Buttons" AND enabled == 0')
        assert len(e) == 0
