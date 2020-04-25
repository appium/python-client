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
    desired_capabilities,
    is_ci
)


class FindByViewMatcherTests(unittest.TestCase):

    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk.zip')
        desired_caps['automationName'] = 'Espresso'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        if is_ci():
            # Take the screenshot to investigate when tests failed only on CI
            img_path = os.path.join(os.getcwd(), self._testMethodName + '.png')
            self.driver.get_screenshot_as_file(img_path)
        self.driver.quit()

    def test_find_single_element(self):
        el = self.driver.find_element_by_android_view_matcher(
            name='withText', args=['Accessibility'], className='ViewMatchers')
        assert el.text == 'Accessibility'

    def test_find_single_element_ful_class_name(self):
        el = self.driver.find_element_by_android_view_matcher(
            name='withText', args=['Accessibility'], className='androidx.test.espresso.matcher.ViewMatchers')
        assert el.text == 'Accessibility'

    def test_find_single_element_using_hamcrest_matcher(self):
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
    def test_find_multiple_elements(self):
        value = AndroidSearchContext()._build_data_matcher(
            name='withSubstring', args=['Access'], className='ViewMatchers')
        with pytest.raises(WebDriverException):
            self.driver.find_elements(by=MobileBy.ANDROID_VIEW_MATCHER, value=value)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FindByViewMatcherTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
