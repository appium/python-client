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

from typing import Callable, Dict, Optional, Union

from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.remote.command import Command as RemoteCommand
from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement
from typing_extensions import Self

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

    def clear(self) -> Self:
        """Clears text.

        Override for Appium

        Returns:
            `appium.webdriver.webelement.WebElement`
        """

        # NOTE: this method is overridden because the selenium client returned None instead of self.
        # Appium python cleint would like to allow users to chain methods.
        data = {'id': self.id}
        self._execute(Command.CLEAR, data)
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

    # Override
    def send_keys(self, *value: str) -> Self:
        """Simulates typing into the element.

        Args:
            value: A string for typing.

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        keys = keys_to_typing(value)
        self._execute(RemoteCommand.SEND_KEYS_TO_ELEMENT, {'text': ''.join(keys), 'value': keys})
        return self
