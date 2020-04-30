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

from test.functional.ios.helper.test_helper import BaseTestCase


class TestFindByIOClassChain(BaseTestCase):
    def test_find_element_by_path(self) -> None:
        els = self.driver.find_elements_by_ios_class_chain('XCUIElementTypeWindow/**/XCUIElementTypeStaticText')
        assert 35 == len(els)
        assert 'UICatalog' == els[0].get_attribute('name')

    def test_find_multiple_elements_by_path(self) -> None:
        el = self.driver.find_elements_by_ios_class_chain('XCUIElementTypeWindow/*/*/*')
        assert 2 == len(el)
        assert 'UICatalog' == el[0].get_attribute('name')
        assert el[1].get_attribute('name') is None
