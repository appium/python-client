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

from selenium.common.exceptions import NoSuchElementException
from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from selenium.webdriver.remote.command import Command as W3C_Command
from ..webelement import WebElement


class ActiveElement(CanExecuteCommands):

    @property
    def active_element(self) -> WebElement:
        """Retrieves session information from the current session

        Usage:
            session = driver.session

        Returns:
            `dict`: containing information from the current session
        """
        try:
            return self.execute(W3C_Command.W3C_GET_ACTIVE_ELEMENT)['value']
        except NoSuchElementException:
            return None

    def send_keys_to_active_element(self, value: str):
        return self.active_element.send_keys(value)

    def click_active_element(self):
        return self.active_element.click()
