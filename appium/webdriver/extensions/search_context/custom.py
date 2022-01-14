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

from typing import TYPE_CHECKING, List

from appium.common.logger import logger
from appium.protocols.webdriver.can_find_elements import CanFindElements
from appium.webdriver.common.appiumby import AppiumBy

if TYPE_CHECKING:
    from appium.webdriver.webelement import WebElement


class CustomSearchContext(CanFindElements):
    """Define search context for custom plugin"""

    def find_element_by_custom(self, selector: str) -> 'WebElement':
        """
        deprecated:: 2.1.0
            Please use 'find_element' with 'AppiumBy.CUSTOM' instead.

        Finds an element in conjunction with a custom element finding plugin

        Args:
            selector: a string of the form "module:selector", where "module" is
                the shortcut name given in the customFindModules capability, and
                "selector" is the string that will be passed to the custom element
                finding plugin itself

        Usage:
            driver.find_element_by_custom("foo:bar")

        Returns:
            `appium.webdriver.webelement.WebElement`: The found element

        """

        logger.warning("[Deprecated] Please use 'find_element' with 'AppiumBy.CUSTOM' instead.")

        return self.find_element(by=AppiumBy.CUSTOM, value=selector)

    def find_elements_by_custom(self, selector: str) -> List['WebElement']:
        """
        deprecated:: 2.1.0
            Please use 'find_elements' with 'AppiumBy.CUSTOM' instead.

        Finds elements in conjunction with a custom element finding plugin

        Args:
            selector: a string of the form "module:selector", where "module" is
                the shortcut name given in the customFindModules capability, and
                "selector" is the string that will be passed to the custom element
                finding plugin itself

        Usage:
            driver.find_elements_by_custom("foo:bar")

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`: The found elements
        """

        logger.warning("[Deprecated] Please use 'find_elements' with 'AppiumBy.CUSTOM' instead.")

        return self.find_elements(by=AppiumBy.CUSTOM, value=selector)
