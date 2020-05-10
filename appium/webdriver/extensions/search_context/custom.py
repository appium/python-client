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

from typing import TYPE_CHECKING, List, TypeVar, Union

from appium.webdriver.common.mobileby import MobileBy

from .base_search_context import BaseSearchContext

if TYPE_CHECKING:
    from appium.webdriver.webelement import WebElement

T = TypeVar('T', bound=Union[BaseSearchContext, 'CustomSearchContext'])


class CustomSearchContext(BaseSearchContext):
    """Define search context for custom plugin"""

    def find_element_by_custom(self: T, selector: str) -> 'WebElement':
        """Finds an element in conjunction with a custom element finding plugin

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
        return self.find_element(by=MobileBy.CUSTOM, value=selector)

    def find_elements_by_custom(self: T, selector: str) -> List['WebElement']:
        """Finds elements in conjunction with a custom element finding plugin

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
        return self.find_elements(by=MobileBy.CUSTOM, value=selector)
