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

import base64

from appium.webdriver.common.mobileby import MobileBy

from .base_search_context import BaseSearchContext


class MobileSearchContext(BaseSearchContext):
    """Define search context for Mobile(Android, iOS)"""

    def find_element_by_accessibility_id(self, accessibility_id):
        """Finds an element by accessibility id.

        Args:
            accessibility_id (str): A string corresponding to a recursive element search using the
                Id/Name that the native Accessibility options utilize

        Usage:
            driver.find_element_by_accessibility_id()

        Returns:
            `appium.webdriver.webelement.WebElement`

        # To enable auto completion in PyCharm(IDE)
        :rtype: `appium.webdriver.webelement.WebElement`
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

        :rtype: list of `appium.webdriver.webelement.WebElement`
        """
        return self.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=accessibility_id)

    def find_element_by_image(self, img_path):
        """Finds a portion of a screenshot by an image.

        Uses driver.find_image_occurrence under the hood.

        Args:
            img_path (str): a string corresponding to the path of a image

        Returns:
            `appium.webdriver.webelement.WebElement`

        :rtype: `appium.webdriver.webelement.WebElement`
        """
        with open(img_path, 'rb') as i_file:
            b64_data = base64.b64encode(i_file.read()).decode('UTF-8')

        return self.find_element(by=MobileBy.IMAGE, value=b64_data)

    def find_elements_by_image(self, img_path):
        """Finds a portion of a screenshot by an image.

        Uses driver.find_image_occurrence under the hood. Note that this will
        only ever return at most one element

        Args:
            img_path (str): a string corresponding to the path of a image

        Return:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`

        :rtype: list of `appium.webdriver.webelement.WebElement`
        """
        with open(img_path, 'rb') as i_file:
            b64_data = base64.b64encode(i_file.read()).decode('UTF-8')

        return self.find_elements(by=MobileBy.IMAGE, value=b64_data)
