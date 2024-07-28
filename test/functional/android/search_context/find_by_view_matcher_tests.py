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

import json

import pytest
from selenium.common.exceptions import WebDriverException

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from test.functional.android.helper.test_helper import BaseTestCase, desired_capabilities, is_ci
from test.helpers.constants import SERVER_URL_BASE


class TestFindByViewMatcher(BaseTestCase):
    # Override
    def setup_method(self, method) -> None:  # type: ignore
        caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk.zip')
        caps['automationName'] = 'Espresso'
        self.driver = webdriver.Remote(SERVER_URL_BASE, options=AppiumOptions().load_capabilities(caps))
        if is_ci():
            self.driver.start_recording_screen()

    def test_find_single_element(self) -> None:
        el = self.driver.find_element(
            by=AppiumBy.ANDROID_VIEW_MATCHER,
            value=json.dumps({'name': 'withText', 'args': ['Accessibility'], 'class': 'ViewMatchers'}),
        )
        assert el.text == 'Accessibility'

    def test_find_single_element_ful_class_name(self) -> None:
        el = self.driver.find_element(
            by=AppiumBy.ANDROID_VIEW_MATCHER,
            value=json.dumps(
                {'name': 'withText', 'args': ['Accessibility'], 'class': 'androidx.test.espresso.matcher.ViewMatchers'}
            ),
        )
        assert el.text == 'Accessibility'

    def test_find_single_element_using_hamcrest_matcher(self) -> None:
        el = self.driver.find_element(
            by=AppiumBy.ANDROID_VIEW_MATCHER,
            value=json.dumps(
                {
                    'name': 'withText',
                    'args': {'name': 'containsString', 'args': 'Animati', 'class': 'org.hamcrest.Matchers'},
                    'class': 'ViewMatchers',
                }
            ),
        )
        assert el.text == 'Animation'

    # androidx.test.espresso.AmbiguousViewMatcherException:
    # 'with text: a string containing "Access"' matches multiple views in the hierarchy.
    def test_find_multiple_elements(self) -> None:
        el = self.driver.find_element(
            by=AppiumBy.ANDROID_VIEW_MATCHER,
            value=json.dumps({'name': 'withSubstring', 'args': ['Access'], 'class': 'ViewMatchers'}),
        )
        self.assertEqual(el.text, "Access'ibility")
