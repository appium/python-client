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


class TestFindByElementWebelement(BaseTestCase):
    def test_find_element_by_path(self) -> None:
        el = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value='wdName == "UICatalog"')
        assert 'UICatalog' == el.get_attribute('name')

        c_el = el.find_elements(by=AppiumBy.IOS_PREDICATE, value='label == "Action Sheets"')  # type: list
        assert 'Action Sheets' == c_el[0].get_attribute('name')

        c_el = el.find_elements(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeStaticText')
        assert 'UICatalog' == c_el[0].get_attribute('name')

        c_el = el.find_elements(by=AppiumBy.ACCESSIBILITY_ID, value='UICatalog')
        assert 'UICatalog' == c_el[0].get_attribute('name')
