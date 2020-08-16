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

import pytest
from selenium.common.exceptions import NoSuchElementException

from appium.webdriver.common.mobileby import MobileBy

from .helper.test_helper import BaseTestCase, wait_for_element


class TestUia2(BaseTestCase):

    def test_flick_uia2_with_element(self) -> None:
        self.driver.find_element_by_accessibility_id('Views').click()
        wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Grid')

        with pytest.raises(NoSuchElementException):
            self.driver.find_element_by_accessibility_id('WebView3')

        el = self.driver.find_element_by_accessibility_id('Grid')
        self.driver.flick_uia2(el, xoffset=0, yoffset=-3000, speed=1000)

        # Exception occurs if not found
        self.driver.find_element_by_accessibility_id('WebView3')

    def test_flick_uia2_without_element(self) -> None:
        self.driver.find_element_by_accessibility_id('Views').click()
        wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Grid')

        with pytest.raises(NoSuchElementException):
            self.driver.find_element_by_accessibility_id('WebView3')

        self.driver.flick_uia2(xspeed=0, yspeed=-3000)

        # Exception occurs if not found
        self.driver.find_element_by_accessibility_id('WebView3')
