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

import os
import unittest

import pytest
from selenium.common.exceptions import WebDriverException

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.extensions.search_context.android import (
    AndroidSearchContext
)
from test.functional.android.helper.test_helper import (
    BaseTestCase,
    desired_capabilities,
    is_ci
)


class TestFindByViewMatcher(BaseTestCase):

    # Override
    def setup_method(self, method) -> None:  # type: ignore
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk.zip')
        desired_caps['automationName'] = 'Espresso'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        if is_ci():
            self.driver.start_recording_screen()

    def test_find_single_element(self) -> None:
        el = self.driver.find_element_by_android_view_matcher(
            name='withText', args=['Accessibility'], className='ViewMatchers')
        assert el.text == 'Accessibility'

    def test_find_single_element_ful_class_name(self) -> None:
        el = self.driver.find_element_by_android_view_matcher(
            name='withText', args=['Accessibility'], className='androidx.test.espresso.matcher.ViewMatchers')
        assert el.text == 'Accessibility'

    def test_find_single_element_using_hamcrest_matcher(self) -> None:
        el = self.driver.find_element_by_android_view_matcher(
            name='withText',
            args={
                'name': 'containsString',
                'args': 'Animati',
                'class': 'org.hamcrest.Matchers'},
            className='ViewMatchers')
        assert el.text == 'Animation'

    # androidx.test.espresso.AmbiguousViewMatcherException:
    # 'with text: a string containing "Access"' matches multiple views in the hierarchy.
    def test_find_multiple_elements(self) -> None:
        value = AndroidSearchContext()._build_data_matcher(
            name='withSubstring', args=['Access'], className='ViewMatchers')
        with pytest.raises(WebDriverException):
            self.driver.find_elements(by=MobileBy.ANDROID_VIEW_MATCHER, value=value)
