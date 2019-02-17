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

from selenium import webdriver

from appium.webdriver.common.mobileby import MobileBy


class SearchContext(webdriver.Remote):
    """Define search context"""

    def find_element_by_android_data_matcher(self, name=None, args=None, className=None):
        """Finds element by [onData](https://medium.com/androiddevelopers/adapterviews-and-espresso-f4172aa853cf) in Android
        It works with [Espresso Driver](https://github.com/appium/appium-espresso-driver).

        :Args:
         - name - The name of a method to invoke. The method must return a Hamcrest [Matcher](http://hamcrest.org/JavaHamcrest/javadoc/1.3/org/hamcrest/Matcher.html)
         - args - The args provided to the method
         - className - The class name that the method is part of (defaults to `org.hamcrest.Matchers`).
                       Can be fully qualified, or simple, and simple defaults to `androidx.test.espresso.matcher` package
                       (e.g.: `class=CursorMatchers` fully qualified is `class=androidx.test.espresso.matcher.CursorMatchers`

        :Returns:
          An Element object

        :Raises:
        - TypeError - Raises a TypeError if the arguments are not validate for JSON format

        :Usage:
            driver.find_element_by_android_data_matcher(name='hasEntry', args=['title', 'Animation'])
        """

        return self.find_element(by=MobileBy.ANDROID_DATA_MATCHER, value=self._build_data_matcher(name=name, args=args, className=className))

    def find_elements_by_android_data_matcher(self, name=None, args=None, className=None):
        """Finds elements by [onData](https://medium.com/androiddevelopers/adapterviews-and-espresso-f4172aa853cf) in Android
        It works with [Espresso Driver](https://github.com/appium/appium-espresso-driver).

        :Args:
         - name - The name of a method to invoke. The method must return a Hamcrest [Matcher](http://hamcrest.org/JavaHamcrest/javadoc/1.3/org/hamcrest/Matcher.html)
         - args - The args provided to the method
         - className - The class name that the method is part of (defaults to `org.hamcrest.Matchers`).
                       Can be fully qualified, or simple, and simple defaults to `androidx.test.espresso.matcher` package
                       (e.g.: `class=CursorMatchers` fully qualified is `class=androidx.test.espresso.matcher.CursorMatchers`

        :Usage:
            driver.find_elements_by_android_data_matcher(name='hasEntry', args=['title', 'Animation'])
        """

        return self.find_elements(by=MobileBy.ANDROID_DATA_MATCHER, value=self._build_data_matcher(name=name, args=args, className=className))

    def _build_data_matcher(self, name=None, args=None, className=None):
        value = {}
        if name is not None:
            value['name'] = name
        if args is not None:
            value['args'] = args
        if className is not None:
            value['class'] = className

        return json.dumps(value)
