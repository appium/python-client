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

import warnings
from typing import Callable, Dict, List, Optional, Union

from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.remote.command import Command as RemoteCommand
from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement

from appium.webdriver.common.appiumby import AppiumBy

from .mobilecommand import MobileCommand as Command


class WebElement(SeleniumWebElement):
    _execute: Callable
    _id: str

    def get_attribute(self, name: str) -> Optional[Union[str, Dict]]:
        """Gets the given attribute or property of the element.

        Override for Appium

        This method will first try to return the value of a property with the
        given name. If a property with that name doesn't exist, it returns the
        value of the attribute with the same name. If there's no attribute with
        that name, ``None`` is returned.

        Values which are considered truthy, that is equals "true" or "false",
        are returned as booleans.  All other non-``None`` values are returned
        as strings.  For attributes or properties which do not exist, ``None``
        is returned.

        Args:
            name: Name of the attribute/property to retrieve.

        Usage:
            # Check if the "active" CSS class is applied to an element.

            is_active = "active" in target_element.get_attribute("class")

        Returns:
            The given attribute or property of the element
        """

        resp = self._execute(RemoteCommand.GET_ELEMENT_ATTRIBUTE, {'name': name})
        attribute_value = resp.get('value')

        if attribute_value is None:
            return None

        if isinstance(attribute_value, dict):
            return attribute_value

        # Convert to str along to the spec
        if not isinstance(attribute_value, str):
            attribute_value = str(attribute_value)

        if name != 'value' and attribute_value.lower() in ('true', 'false'):
            return attribute_value.lower()

        return attribute_value

    def is_displayed(self) -> bool:
        """Whether the element is visible to a user.

        Override for Appium
        """
        return self._execute(Command.IS_ELEMENT_DISPLAYED)['value']

    def find_element(self, by: str = AppiumBy.ID, value: Union[str, Dict, None] = None) -> 'WebElement':
        """Find an element given a AppiumBy strategy and locator

        Override for Appium

        Prefer the find_element_by_* methods when possible.

        Args:
            by: The strategy
            value: The locator

        Usage:
            element = element.find_element(AppiumBy.ID, 'foo')

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        # We prefer to patch locators in the client code
        # Checking current context every time a locator is accessed could significantly slow down tests
        # Check https://github.com/appium/python-client/pull/724 before submitting any issue
        # if by == By.ID:
        #     by = By.CSS_SELECTOR
        #     value = '[id="%s"]' % value
        # elif by == By.TAG_NAME:
        #     by = By.CSS_SELECTOR
        # elif by == By.CLASS_NAME:
        #     by = By.CSS_SELECTOR
        #     value = ".%s" % value
        # elif by == By.NAME:
        #     by = By.CSS_SELECTOR
        #     value = '[name="%s"]' % value

        return self._execute(RemoteCommand.FIND_CHILD_ELEMENT, {"using": by, "value": value})['value']

    def find_elements(self, by: str = AppiumBy.ID, value: Union[str, Dict, None] = None) -> List['WebElement']:
        """Find elements given a AppiumBy strategy and locator

        Args:
            by: The strategy
            value: The locator

        Usage:
            element = element.find_elements(AppiumBy.CLASS_NAME, 'foo')

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`
        """
        # We prefer to patch locators in the client code
        # Checking current context every time a locator is accessed could significantly slow down tests
        # Check https://github.com/appium/python-client/pull/724 before submitting any issue
        # if by == By.ID:
        #     by = By.CSS_SELECTOR
        #     value = '[id="%s"]' % value
        # elif by == By.TAG_NAME:
        #     by = By.CSS_SELECTOR
        # elif by == By.CLASS_NAME:
        #     by = By.CSS_SELECTOR
        #     value = ".%s" % value
        # elif by == By.NAME:
        #     by = By.CSS_SELECTOR
        #     value = '[name="%s"]' % value

        return self._execute(RemoteCommand.FIND_CHILD_ELEMENTS, {"using": by, "value": value})['value']

    def clear(self) -> 'WebElement':
        """Clears text.

        Override for Appium

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        data = {'id': self.id}
        self._execute(Command.CLEAR, data)
        return self

    def set_text(self, keys: str = '') -> 'WebElement':
        """Sends text to the element.
        deprecated:: 2.8.1

        Previous text is removed.
        Android only.

        Args:
            keys: the text to be sent to the element.

        Usage:
            element.set_text('some text')

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        warnings.warn(
            'The "setText" API is deprecated and will be removed in future versions. '
            'Instead the "send_keys" API or W3C Actions can be used. '
            'See https://github.com/appium/python-client/pull/831',
            DeprecationWarning,
        )

        data = {'text': keys}
        self._execute(Command.REPLACE_KEYS, data)
        return self

    @property
    def location_in_view(self) -> Dict[str, int]:
        """Gets the location of an element relative to the view.

        Usage:
            | location = element.location_in_view
            | x = location['x']
            | y = location['y']

        Returns:
            dict: The location of an element relative to the view
        """
        return self._execute(Command.LOCATION_IN_VIEW)['value']

    def set_value(self, value: str) -> 'WebElement':
        """Set the value on this element in the application
        deprecated:: 2.8.1

        Args:
            value: The value to be set

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        warnings.warn(
            'The "setValue" API is deprecated and will be removed in future versions. '
            'Instead the "send_keys" API or W3C Actions can be used. '
            'See https://github.com/appium/python-client/pull/831',
            DeprecationWarning,
        )

        data = {'text': value}
        self._execute(Command.SET_IMMEDIATE_VALUE, data)
        return self

    # Override
    def send_keys(self, *value: str) -> 'WebElement':
        """Simulates typing into the element.

        Args:
            value: A string for typing.

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        keys = keys_to_typing(value)
        self._execute(RemoteCommand.SEND_KEYS_TO_ELEMENT, {'text': ''.join(keys), 'value': keys})
        return self
