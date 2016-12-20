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

from .mobilecommand import MobileCommand as Command

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement


class WebElement(SeleniumWebElement):
    def find_element_by_ios_uiautomation(self, uia_string):
        """Finds an element by uiautomation in iOS.

        :Args:
         - uia_string - The element name in the iOS UIAutomation library

        :Usage:
            driver.find_element_by_ios_uiautomation('.elements()[1].cells()[2]')
        """
        return self.find_element(by=By.IOS_UIAUTOMATION, value=uia_string)

    def find_elements_by_ios_uiautomation(self, uia_string):
        """Finds elements by uiautomation in iOS.

        :Args:
         - uia_string - The element name in the iOS UIAutomation library

        :Usage:
            driver.find_elements_by_ios_uiautomation('.elements()[1].cells()[2]')
        """
        return self.find_elements(by=By.IOS_UIAUTOMATION, value=uia_string)

    def find_element_by_ios_predicate(self, predicate_string):
        """Find an element by ios predicate string.

        :Args:
         - predicate_string - The predicate string

        :Usage:
            driver.find_element_by_ios_predicate('label == "myLabel"')
        """
        return self.find_element(by=By.IOS_PREDICATE, value=predicate_string)

    def find_elements_by_ios_predicate(self, predicate_string):
        """Finds elements by ios predicate string.

        :Args:
         - predicate_string - The predicate string

        :Usage:
            driver.find_elements_by_ios_predicate('label == "myLabel"')
        """
        return self.find_elements(by=By.IOS_PREDICATE, value=predicate_string)

    def find_element_by_android_uiautomator(self, uia_string):
        """Finds element by uiautomator in Android.

        :Args:
         - uia_string - The element name in the Android UIAutomator library

        :Usage:
            driver.find_element_by_android_uiautomator('.elements()[1].cells()[2]')
        """
        return self.find_element(by=By.ANDROID_UIAUTOMATOR, value=uia_string)

    def find_elements_by_android_uiautomator(self, uia_string):
        """Finds elements by uiautomator in Android.

        :Args:
         - uia_string - The element name in the Android UIAutomator library

        :Usage:
            driver.find_elements_by_android_uiautomator('.elements()[1].cells()[2]')
        """
        return self.find_elements(by=By.ANDROID_UIAUTOMATOR, value=uia_string)

    def find_element_by_accessibility_id(self, id):
        """Finds an element by accessibility id.

        :Args:
         - id - a string corresponding to a recursive element search using the
         Id/Name that the native Accessibility options utilize

        :Usage:
            driver.find_element_by_accessibility_id()
        """
        return self.find_element(by=By.ACCESSIBILITY_ID, value=id)

    def find_elements_by_accessibility_id(self, id):
        """Finds elements by accessibility id.

        :Args:
         - id - a string corresponding to a recursive element search using the
         Id/Name that the native Accessibility options utilize

        :Usage:
            driver.find_elements_by_accessibility_id()
        """
        return self.find_elements(by=By.ACCESSIBILITY_ID, value=id)

    def set_text(self, keys=''):
        """Sends text to the element. Previous text is removed.
        Android only.

        :Args:
         - keys - the text to be sent to the element.

        :Usage:
            element.set_text('some text')
        """
        data = {
            'id': self._id,
            'value': [keys]
        }
        self._execute(Command.REPLACE_KEYS, data)
        return self

    @property
    def location_in_view(self):
        """Gets the location of an element relative to the view.

        :Usage:
            location = element.location_in_view
        """
        return self._execute(Command.LOCATION_IN_VIEW)['value']

    def set_value(self, value):
        """Set the value on this element in the application
        """
        data = {
            'id': self.id,
            'value': [value],
        }
        self._execute(Command.SET_IMMEDIATE_VALUE, data)
        return self

    def clear(self):
        """Clears text.
        """
        data = {'id': self.id}
        self._execute(Command.CLEAR, data)
        return self
