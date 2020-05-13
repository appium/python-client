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
from typing import TYPE_CHECKING, Any, List, Optional, TypeVar, Union

from appium.webdriver.common.mobileby import MobileBy

from .base_search_context import BaseSearchContext

if TYPE_CHECKING:
    from appium.webdriver.webelement import WebElement

T = TypeVar('T', bound=Union[BaseSearchContext, 'AndroidSearchContext'])


class AndroidSearchContext(BaseSearchContext):
    """Define search context for Android"""

    def find_element_by_android_view_matcher(self: T, name: Optional[str] = None, args: Optional[Any] = None,
                                             className: Optional[str] = None) -> 'WebElement':
        """Finds element by [onView](https://developer.android.com/training/testing/espresso/basics) in Android

        It works with [Espresso Driver](https://github.com/appium/appium-espresso-driver).

        Args:
            name: The name of a method to invoke.
                The method must return a Hamcrest
                [Matcher](http://hamcrest.org/JavaHamcrest/javadoc/1.3/org/hamcrest/Matcher.html)
            args: The args provided to the method
            className: The class name that the method is part of (defaults to `org.hamcrest.Matchers`).
                Can be fully qualified by having the androidx.test.espresso.matcher. prefix.
                If the prefix is not provided then it is going to be added implicitly.
                (e.g.: `class=CursorMatchers` fully qualified is `class=androidx.test.espresso.matcher.CursorMatchers`

        Returns:
            `appium.webdriver.webelement.WebElement`: The found element

        Raises:
            TypeError - Raises a TypeError if the arguments are not validated for JSON format

        Usage:
            driver.find_element_by_android_view_matcher(name='withText', args=['Accessibility'], className='ViewMatchers')
        """

        return self.find_element(
            by=MobileBy.ANDROID_VIEW_MATCHER,
            value=self._build_data_matcher(name=name, args=args, className=className)
        )

    def find_element_by_android_data_matcher(self: T, name: Optional[str] = None, args: Optional[Any] = None,
                                             className: Optional[str] = None) -> 'WebElement':
        """Finds element by
        [onData](https://medium.com/androiddevelopers/adapterviews-and-espresso-f4172aa853cf) in Android

        It works with [Espresso Driver](https://github.com/appium/appium-espresso-driver).

        Args:
            name: The name of a method to invoke.
                The method must return a Hamcrest
                [Matcher](http://hamcrest.org/JavaHamcrest/javadoc/1.3/org/hamcrest/Matcher.html)
            args: The args provided to the method
            className: The class name that the method is part of
                (defaults to `org.hamcrest.Matchers`).
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

    def find_elements_by_android_data_matcher(self: T, name: Optional[str] = None, args: Optional[Any] = None,
                                              className: Optional[str] = None) -> List['WebElement']:
        """Finds elements by
        [onData](https://medium.com/androiddevelopers/adapterviews-and-espresso-f4172aa853cf) in Android
        It works with [Espresso Driver](https://github.com/appium/appium-espresso-driver).

        Args:
            name: The name of a method to invoke.
                The method must return a Hamcrest
                [Matcher](http://hamcrest.org/JavaHamcrest/javadoc/1.3/org/hamcrest/Matcher.html)
            args: The args provided to the method
            className: The class name that the method is part of
                (defaults to `org.hamcrest.Matchers`).
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

    def _build_data_matcher(self: T, name: Optional[str] = None, args: Optional[Any] = None,
                            className: Optional[str] = None) -> str:
        result = {}

        for key, value in {'name': name, 'args': args, 'class': className}.items():
            if value is not None:
                result[key] = value

        return json.dumps(result)

    def find_element_by_android_uiautomator(self: T, uia_string: str) -> 'WebElement':
        """Finds element by uiautomator in Android.

        Args:
            uia_string: The element name in the Android UIAutomator library

        Usage:
            driver.find_element_by_android_uiautomator('.elements()[1].cells()[2]')

        Returns:
            `appium.webdriver.webelement.WebElement`: The found element
        """
        return self.find_element(by=MobileBy.ANDROID_UIAUTOMATOR, value=uia_string)

    def find_elements_by_android_uiautomator(self: T, uia_string: str) -> List['WebElement']:
        """Finds elements by uiautomator in Android.

        Args:
            uia_string: The element name in the Android UIAutomator library

        Usage:
            driver.find_elements_by_android_uiautomator('.elements()[1].cells()[2]')

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`: The found elements
        """
        return self.find_elements(by=MobileBy.ANDROID_UIAUTOMATOR, value=uia_string)

    def find_element_by_android_viewtag(self: T, tag: str) -> 'WebElement':
        """Finds element by [View#tags](https://developer.android.com/reference/android/view/View#tags) in Android.

        It works with [Espresso Driver](https://github.com/appium/appium-espresso-driver).

        Args:
            tag: The tag name of the view to look for

        Usage:
            driver.find_element_by_android_viewtag('a tag name')

        Returns:
            `appium.webdriver.webelement.WebElement`: The found element
        """
        return self.find_element(by=MobileBy.ANDROID_VIEWTAG, value=tag)

    def find_elements_by_android_viewtag(self: T, tag: str) -> List['WebElement']:
        """Finds element by [View#tags](https://developer.android.com/reference/android/view/View#tags) in Android.

        It works with [Espresso Driver](https://github.com/appium/appium-espresso-driver).

        Args:
            tag: The tag name of the view to look for

        Usage:
            driver.find_elements_by_android_viewtag('a tag name')

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`: The found elements
        """
        return self.find_elements(by=MobileBy.ANDROID_VIEWTAG, value=tag)
