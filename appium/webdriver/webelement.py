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

from typing import Dict, List, Optional, TypeVar, Union

from selenium.webdriver.common.by import By
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.remote.command import Command as RemoteCommand

from .extensions.search_context import AppiumWebElementSearchContext
from .mobilecommand import MobileCommand as Command

T = TypeVar('T', bound='WebElement')


class WebElement(AppiumWebElementSearchContext):
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
        attributeValue = resp.get('value')

        if attributeValue is None:
            return None

        if isinstance(attributeValue, dict):
            return attributeValue

        # Convert to str along to the spec
        if not isinstance(attributeValue, str):
            attributeValue = str(attributeValue)

        if name != 'value' and attributeValue.lower() in ('true', 'false'):
            return attributeValue.lower()

        return attributeValue

    def is_displayed(self) -> bool:
        """Whether the element is visible to a user.

        Override for Appium
        """
        return self._execute(RemoteCommand.IS_ELEMENT_DISPLAYED)['value']

    def find_element(self, by: str = By.ID, value: Union[str, Dict] = None) -> T:
        """Find an element given a By strategy and locator

        Override for Appium

        Prefer the find_element_by_* methods when possible.

        Args:
            by: The strategy
            value: The locator

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

        return self._execute(RemoteCommand.FIND_CHILD_ELEMENT, {"using": by, "value": value})['value']

    def find_elements(self, by: str = By.ID, value: Union[str, Dict] = None) -> List[T]:
        """Find elements given a By strategy and locator

        Override for Appium

        Prefer the find_elements_by_* methods when possible.

        Args:
            by: The strategy
            value: The locator

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

        return self._execute(RemoteCommand.FIND_CHILD_ELEMENTS, {"using": by, "value": value})['value']

    def clear(self) -> T:
        """Clears text.

        Override for Appium

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        data = {'id': self.id}
        self._execute(Command.CLEAR, data)
        return self

    def set_text(self, keys: str = '') -> T:
        """Sends text to the element.

        Previous text is removed.
        Android only.

        Args:
            keys: the text to be sent to the element.

        Usage:
            element.set_text('some text')

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        data = {'id': self._id, 'value': [keys]}
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

    def set_value(self, value: str) -> T:
        """Set the value on this element in the application

        Args:
            value: The value to be set

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        data = {
            'id': self.id,
            'value': [value],
        }
        self._execute(Command.SET_IMMEDIATE_VALUE, data)
        return self

    # Override
    def send_keys(self, *value: str) -> T:
        """Simulates typing into the element.

        Args:
            value: A string for typing.

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        keys = keys_to_typing(value)
        self._execute(RemoteCommand.SEND_KEYS_TO_ELEMENT, {'text': ''.join(keys), 'value': keys})
        return self
