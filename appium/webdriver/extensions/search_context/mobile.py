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

import base64
from typing import TYPE_CHECKING, List

from appium.common.logger import logger
from appium.protocols.webdriver.can_find_elements import CanFindElements
from appium.webdriver.common.appiumby import AppiumBy

if TYPE_CHECKING:
    from appium.webdriver.webelement import WebElement


class MobileSearchContext(CanFindElements):
    """Define search context for Mobile(Android, iOS)"""

    def find_element_by_accessibility_id(self, accessibility_id: str) -> 'WebElement':
        """
        deprecated:: 2.1.0
            Please use 'find_element' with 'AppiumBy.ACCESSIBILITY_ID' instead.

        Finds an element by accessibility id.

        Args:
            accessibility_id: A string corresponding to a recursive element search using the
                Id/Name that the native Accessibility options utilize

        Usage:
            driver.find_element_by_accessibility_id()

        Returns:
            `appium.webdriver.webelement.WebElement`: The found element

        """

        logger.warning("[Deprecated] Please use 'find_element' with 'AppiumBy.ACCESSIBILITY_ID' instead.")

        return self.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=accessibility_id)

    def find_elements_by_accessibility_id(self, accessibility_id: str) -> List['WebElement']:
        """
        deprecated:: 2.1.0
            Please use 'find_elements' with 'AppiumBy.ACCESSIBILITY_ID' instead.

        Finds elements by accessibility id.

        Args:
            accessibility_id: a string corresponding to a recursive element search using the
                Id/Name that the native Accessibility options utilize

        Usage:
            driver.find_elements_by_accessibility_id()

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`: The found elements

        """

        logger.warning("[Deprecated] Please use 'find_elements' with 'AppiumBy.ACCESSIBILITY_ID' instead.")

        return self.find_elements(by=AppiumBy.ACCESSIBILITY_ID, value=accessibility_id)

    def find_element_by_image(self, img_path: str) -> 'WebElement':
        """Finds a portion of a screenshot by an image.

        Uses driver.find_image_occurrence under the hood.

        Args:
            img_path: a string corresponding to the path of a image

        Returns:
            `appium.webdriver.webelement.WebElement`: The found element
        """

        with open(img_path, 'rb') as i_file:
            b64_data = base64.b64encode(i_file.read()).decode('UTF-8')

        return self.find_element(by=AppiumBy.IMAGE, value=b64_data)

    def find_elements_by_image(self, img_path: str) -> List['WebElement']:
        """Finds a portion of a screenshot by an image.

        Uses driver.find_image_occurrence under the hood. Note that this will
        only ever return at most one element

        Args:
            img_path: a string corresponding to the path of a image

        Return:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`: The found elements
        """
        with open(img_path, 'rb') as i_file:
            b64_data = base64.b64encode(i_file.read()).decode('UTF-8')

        return self.find_elements(by=AppiumBy.IMAGE, value=b64_data)
