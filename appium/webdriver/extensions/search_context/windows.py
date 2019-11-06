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

from appium.webdriver.common.mobileby import MobileBy

from .base_search_context import BaseSearchContext


class WindowsSearchContext(BaseSearchContext):
    """Define search context for Windows"""

    def find_element_by_windows_uiautomation(self, win_uiautomation):
        """Finds an element by windows uiautomation

        Args:
            win_uiautomation (str): The element name in the windows UIAutomation selector

        Usage:
            driver.find_element_by_windows_uiautomation()

        Returns:
            `appium.webdriver.webelement.WebElement`

        # To enable auto completion in PyCharm(IDE)
        :rtype: `appium.webdriver.webelement.WebElement`
        """
        return self.find_element(by=MobileBy.WINDOWS_UI_AUTOMATION, value=win_uiautomation)

    def find_elements_by_windows_uiautomation(self, win_uiautomation):
        """Finds elements by windows uiautomation

        Args:
            win_uiautomation (str): The element name in the windows UIAutomation selector

        Usage:
            driver.find_elements_by_windows_uiautomation()

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`

        :rtype: list of `appium.webdriver.webelement.WebElement`
        """
        return self.find_elements(by=MobileBy.WINDOWS_UI_AUTOMATION, value=win_uiautomation)
