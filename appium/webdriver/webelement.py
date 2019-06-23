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

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command as RemoteCommand

from appium.webdriver.common.mobileby import MobileBy

from .extensions.search_context import AppiumWebElementSearchContext
from .mobilecommand import MobileCommand as Command

# Python 3 imports
try:
    str = basestring
except NameError:
    pass


class WebElement(AppiumWebElementSearchContext):
    # Override
    def get_attribute(self, name):
        """Gets the given attribute or property of the element.

        This method will first try to return the value of a property with the
        given name. If a property with that name doesn't exist, it returns the
        value of the attribute with the same name. If there's no attribute with
        that name, ``None`` is returned.

        Values which are considered truthy, that is equals "true" or "false",
        are returned as booleans.  All other non-``None`` values are returned
        as strings.  For attributes or properties which do not exist, ``None``
        is returned.

        Args:
            name (str): Name of the attribute/property to retrieve.

        Usage:
            # Check if the "active" CSS class is applied to an element.
            is_active = "active" in target_element.get_attribute("class")

        Returns:
            str: The given attribute or property of the element
        """

        resp = self._execute(RemoteCommand.GET_ELEMENT_ATTRIBUTE, {'name': name})
        attributeValue = resp.get('value')

        if attributeValue is None:
            return None

        if not isinstance(attributeValue, str):
            attributeValue = unicode(attributeValue)

        if name != 'value' and attributeValue.lower() in ('true', 'false'):
            return attributeValue.lower()

        return attributeValue

    # Override
    def is_displayed(self):
        """Whether the element is visible to a user."""
        return self._execute(RemoteCommand.IS_ELEMENT_DISPLAYED)['value']

    def find_element_by_ios_uiautomation(self, uia_string):
        """Finds an element by uiautomation in iOS.

        Args:
            uia_string (str): The element name in the iOS UIAutomation library

        Usage:
            driver.find_element_by_ios_uiautomation('.elements()[1].cells()[2]')

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        return self.find_element(by=MobileBy.IOS_UIAUTOMATION, value=uia_string)

    def find_elements_by_ios_uiautomation(self, uia_string):
        """Finds elements by uiautomation in iOS.

        Args:
            uia_string (str): The element name in the iOS UIAutomation library

        Usage:
            driver.find_elements_by_ios_uiautomation('.elements()[1].cells()[2]')

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`
        """
        return self.find_elements(by=MobileBy.IOS_UIAUTOMATION, value=uia_string)

    def find_element_by_ios_predicate(self, predicate_string):
        """Find an element by ios predicate string.

        Args:
            predicate_string (str): The predicate string

        Usage:
            driver.find_element_by_ios_predicate('label == "myLabel"')

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        return self.find_element(by=MobileBy.IOS_PREDICATE, value=predicate_string)

    def find_elements_by_ios_predicate(self, predicate_string):
        """Finds elements by ios predicate string.

        Args:
            predicate_string (str): The predicate string

        Usage:
            driver.find_elements_by_ios_predicate('label == "myLabel"')

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`
        """
        return self.find_elements(by=MobileBy.IOS_PREDICATE, value=predicate_string)

    def find_element_by_ios_class_chain(self, class_chain_string):
        """Find an element by ios class chain string.

        Args:
            class_chain_string (str): The class chain string

        Usage:
            driver.find_element_by_ios_class_chain('XCUIElementTypeWindow/XCUIElementTypeButton[3]')

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        return self.find_element(by=MobileBy.IOS_CLASS_CHAIN, value=class_chain_string)

    def find_elements_by_ios_class_chain(self, class_chain_string):
        """Finds elements by ios class chain string.

        Args:
            class_chain_string (str): The class chain string

        Usage:
            driver.find_elements_by_ios_class_chain('XCUIElementTypeWindow[2]/XCUIElementTypeAny[-2]')

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`
        """
        return self.find_elements(by=MobileBy.IOS_CLASS_CHAIN, value=class_chain_string)

    def find_element_by_android_uiautomator(self, uia_string):
        """Finds element by uiautomator in Android.

        Args:
            uia_string (str): The element name in the Android UIAutomator library

        Usage:
            driver.find_element_by_android_uiautomator('.elements()[1].cells()[2]')

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        return self.find_element(by=MobileBy.ANDROID_UIAUTOMATOR, value=uia_string)

    def find_elements_by_android_uiautomator(self, uia_string):
        """Finds elements by uiautomator in Android.

        Args:
            uia_string (str): The element name in the Android UIAutomator library

        Usage:
            driver.find_elements_by_android_uiautomator('.elements()[1].cells()[2]')

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`
        """
        return self.find_elements(by=MobileBy.ANDROID_UIAUTOMATOR, value=uia_string)

    def find_element_by_accessibility_id(self, accessibility_id):
        """Finds an element by accessibility id.

        Args:
            accessibility_id (str): a string corresponding to a recursive element search using the
                Id/Name that the native Accessibility options utilize

        Usage:
            driver.find_element_by_accessibility_id()

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        return self.find_element(by=MobileBy.ACCESSIBILITY_ID, value=accessibility_id)

    def find_elements_by_accessibility_id(self, accessibility_id):
        """Finds elements by accessibility id.

        Args:
            accessibility_id (str): a string corresponding to a recursive element search using the
                Id/Name that the native Accessibility options utilize

        Usage:
            driver.find_elements_by_accessibility_id()

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`
        """
        return self.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=accessibility_id)

    def find_element(self, by=By.ID, value=None):
        """Find an element given a By strategy and locator

        Prefer the find_element_by_* methods when possible.

        Args:
            by (:obj:`str`, optional): The strategy
            value (:obj:`str`, optional): The locator

        Usage:
            element = element.find_element(By.ID, 'foo')

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        # TODO: If we need, we should enable below converter for Web context
        # if self._w3c:
        #     if by == By.ID:
        #         by = By.CSS_SELECTOR
        #         value = '[id="%s"]' % value
        #     elif by == By.TAG_NAME:
        #         by = By.CSS_SELECTOR
        #     elif by == By.CLASS_NAME:
        #         by = By.CSS_SELECTOR
        #         value = ".%s" % value
        #     elif by == By.NAME:
        #         by = By.CSS_SELECTOR
        #         value = '[name="%s"]' % value

        return self._execute(RemoteCommand.FIND_CHILD_ELEMENT,
                             {"using": by, "value": value})['value']

    def find_elements(self, by=By.ID, value=None):
        """Find elements given a By strategy and locator

        Prefer the find_elements_by_* methods when possible.

        Args:
            by (:obj:`str`, optional): The strategy
            value (:obj:`str`, optional): The locator

        Usage:
            element = element.find_elements(By.CLASS_NAME, 'foo')

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`
        """
        # TODO: If we need, we should enable below converter for Web context
        # if self._w3c:
        #     if by == By.ID:
        #         by = By.CSS_SELECTOR
        #         value = '[id="%s"]' % value
        #     elif by == By.TAG_NAME:
        #         by = By.CSS_SELECTOR
        #     elif by == By.CLASS_NAME:
        #         by = By.CSS_SELECTOR
        #         value = ".%s" % value
        #     elif by == By.NAME:
        #         by = By.CSS_SELECTOR
        #         value = '[name="%s"]' % value

        return self._execute(RemoteCommand.FIND_CHILD_ELEMENTS,
                             {"using": by, "value": value})['value']

    def set_text(self, keys=''):
        """Sends text to the element.

        Previous text is removed.
        Android only.

        Args:
            keys (str): the text to be sent to the element.

        Usage:
            element.set_text('some text')

        Returns:
            `appium.webdriver.webelement.WebElement`
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

        Usage:
            location = element.location_in_view
            x = location['x']
            y = location['y']

        Returns:
            dict: The location of an element relative to the view
        """
        return self._execute(Command.LOCATION_IN_VIEW)['value']

    def set_value(self, value):
        """Set the value on this element in the application

        Args:
            value (str): The value to be set

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        data = {
            'id': self.id,
            'value': [value],
        }
        self._execute(Command.SET_IMMEDIATE_VALUE, data)
        return self

    def clear(self):
        """Clears text.

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        data = {'id': self.id}
        self._execute(Command.CLEAR, data)
        return self
