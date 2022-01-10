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


class iOSSearchContext(CanFindElements):
    """Define search context for iOS"""

    def find_element_by_ios_uiautomation(self, uia_string: str) -> 'WebElement':
        """
        deprecated:: 2.1.0
            Please use 'find_element' with 'AppiumBy.IOS_UIAUTOMATION' instead.

        Finds an element by uiautomation in iOS.

        Args:
            uia_string: The element name in the iOS UIAutomation library

        Usage:
            driver.find_element_by_ios_uiautomation('.elements()[1].cells()[2]')

        Returns:
            `appium.webdriver.webelement.WebElement`: The found element

        """

        logger.warning("[Deprecated] Please use 'find_element' with 'AppiumBy.IOS_UIAUTOMATION' instead.")

        return self.find_element(by=AppiumBy.IOS_UIAUTOMATION, value=uia_string)

    def find_elements_by_ios_uiautomation(self, uia_string: str) -> List['WebElement']:
        """
        deprecated:: 2.1.0
            Please use 'find_elements' with 'AppiumBy.IOS_UIAUTOMATION' instead.

        Finds elements by uiautomation in iOS.

        Args:
            uia_string: The element name in the iOS UIAutomation library

        Usage:
            driver.find_elements_by_ios_uiautomation('.elements()[1].cells()[2]')

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`: The found elements

        """

        logger.warning("[Deprecated] Please use 'find_elements' with 'AppiumBy.IOS_UIAUTOMATION' instead.")

        return self.find_elements(by=AppiumBy.IOS_UIAUTOMATION, value=uia_string)

    def find_element_by_ios_predicate(self, predicate_string: str) -> 'WebElement':
        """
        deprecated:: 2.1.0
            Please use 'find_element' with 'AppiumBy.IOS_PREDICATE' instead.

        Find an element by ios predicate string.

        Args:
            predicate_string: The predicate string

        Usage:
            driver.find_element_by_ios_predicate('label == "myLabel"')

        Returns:
            `appium.webdriver.webelement.WebElement`: The found element

        """

        logger.warning("[Deprecated] Please use 'find_element' with 'AppiumBy.IOS_PREDICATE' instead.")

        return self.find_element(by=AppiumBy.IOS_PREDICATE, value=predicate_string)

    def find_elements_by_ios_predicate(self, predicate_string: str) -> List['WebElement']:
        """
        deprecated:: 2.1.0
            Please use 'find_elements' with 'AppiumBy.IOS_PREDICATE' instead.

        Finds elements by ios predicate string.

        Args:
            predicate_string: The predicate string

        Usage:
            driver.find_elements_by_ios_predicate('label == "myLabel"')

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`: The found elements
        """

        logger.warning("[Deprecated] Please use 'find_elements' with 'AppiumBy.IOS_PREDICATE' instead.")

        return self.find_elements(by=AppiumBy.IOS_PREDICATE, value=predicate_string)

    def find_element_by_ios_class_chain(self, class_chain_string: str) -> 'WebElement':
        """
        deprecated:: 2.1.0
            Please use 'find_element' with 'AppiumBy.IOS_CLASS_CHAIN' instead.

        Find an element by ios class chain string.

        Args:
            class_chain_string: The class chain string

        Usage:
            driver.find_element_by_ios_class_chain('XCUIElementTypeWindow/XCUIElementTypeButton[3]')

        Returns:
            `appium.webdriver.webelement.WebElement`: The found element
        """

        logger.warning("[Deprecated] Please use 'find_element' with 'AppiumBy.IOS_CLASS_CHAIN' instead.")

        return self.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value=class_chain_string)

    def find_elements_by_ios_class_chain(self, class_chain_string: str) -> List['WebElement']:
        """
        deprecated:: 2.1.0
            Please use 'find_elements' with 'AppiumBy.IOS_CLASS_CHAIN' instead.

        Finds elements by ios class chain string.

        Args:
            class_chain_string: The class chain string

        Usage:
            driver.find_elements_by_ios_class_chain('XCUIElementTypeWindow[2]/XCUIElementTypeAny[-2]')

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`: The found elements
        """

        logger.warning("[Deprecated] Please use 'find_elements' with 'AppiumBy.IOS_CLASS_CHAIN' instead.")

        return self.find_elements(by=AppiumBy.IOS_CLASS_CHAIN, value=class_chain_string)
