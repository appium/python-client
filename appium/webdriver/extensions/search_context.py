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

# pylint: disable=abstract-method

import json

from selenium import webdriver
from selenium.webdriver.remote.webelement import \
    WebElement as SeleniumWebElement

from appium.webdriver.common.mobileby import MobileBy


class BaseSearchContext(object):
    """Used by each search context. Dummy find_element/s are for preventing pylint error"""

    def find_element(self, by=None, value=None):
        raise NotImplementedError

    def find_elements(self, by=None, value=None):
        raise NotImplementedError


class AndroidSearchContext(BaseSearchContext):
    """Define search context for Android"""

    def find_element_by_android_data_matcher(self, name=None, args=None, className=None):
        """Finds element by [onData](https://medium.com/androiddevelopers/adapterviews-and-espresso-f4172aa853cf) in Android

        It works with [Espresso Driver](https://github.com/appium/appium-espresso-driver).

        Args:
            name (:obj:`str`, optional): The name of a method to invoke.
                The method must return a Hamcrest
                [Matcher](http://hamcrest.org/JavaHamcrest/javadoc/1.3/org/hamcrest/Matcher.html)
            args (:obj:`str`, optional): The args provided to the method
            className (:obj:`str`, optional): The class name that the method is part of (defaults to `org.hamcrest.Matchers`).
                Can be fully qualified, or simple, and simple defaults to `androidx.test.espresso.matcher` package
                (e.g.: `class=CursorMatchers` fully qualified is `class=androidx.test.espresso.matcher.CursorMatchers`

        Returns:
            `appium.webdriver.webelement.WebElement`: The found element

        Raises:
            TypeError - Raises a TypeError if the arguments are not validated for JSON format

        Usage:
            driver.find_element_by_android_data_matcher(name='hasEntry', args=['title', 'Animation'])
        """

        return self.find_element(
            by=MobileBy.ANDROID_DATA_MATCHER,
            value=self._build_data_matcher(name=name, args=args, className=className)
        )

    def find_elements_by_android_data_matcher(self, name=None, args=None, className=None):
        """Finds elements by [onData](https://medium.com/androiddevelopers/adapterviews-and-espresso-f4172aa853cf) in Android
        It works with [Espresso Driver](https://github.com/appium/appium-espresso-driver).

        Args:
            name (:obj:`str`, optional): The name of a method to invoke.
                The method must return a Hamcrest
                [Matcher](http://hamcrest.org/JavaHamcrest/javadoc/1.3/org/hamcrest/Matcher.html)
            args (:obj:`str`, optional): The args provided to the method
            className (:obj:`str`, optional): The class name that the method is part of (defaults to `org.hamcrest.Matchers`).
                Can be fully qualified, or simple, and simple defaults to `androidx.test.espresso.matcher` package
                (e.g.: `class=CursorMatchers` fully qualified is `class=androidx.test.espresso.matcher.CursorMatchers`

        Returns:
            `appium.webdriver.webelement.WebElement`: The found elements

        Usage:
            driver.find_elements_by_android_data_matcher(name='hasEntry', args=['title', 'Animation'])
        """

        return self.find_elements(
            by=MobileBy.ANDROID_DATA_MATCHER,
            value=self._build_data_matcher(name=name, args=args, className=className)
        )

    def _build_data_matcher(self, name=None, args=None, className=None):
        result = {}

        for key, value in {'name': name, 'args': args, 'class': className}.items():
            if value is not None:
                result[key] = value

        return json.dumps(result)


class AppiumSearchContext(webdriver.Remote,
                          AndroidSearchContext):
    """Returns appium driver search conext"""


class AppiumWebElementSearchContext(SeleniumWebElement,
                                    AndroidSearchContext):
    """Returns appium web element search context"""
