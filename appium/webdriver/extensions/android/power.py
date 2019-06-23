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

from selenium import webdriver

from appium.webdriver.mobilecommand import MobileCommand as Command


class Power(webdriver.Remote):

    AC_OFF, AC_ON = 'off', 'on'

    def set_power_capacity(self, percent):
        """Emulate power capacity change on the connected emulator.

        Android only.

        Args:
            percent (int): The power capacity to be set. Can be set from 0 to 100

        Usage:
            self.driver.set_power_capacity(50)

        Returns:
            `appium.webdriver.webdriver.WebDriver`
        """
        self.execute(Command.SET_POWER_CAPACITY, {'percent': percent})
        return self

    def set_power_ac(self, ac_state):
        """Emulate power state change on the connected emulator.

        Android only.

        Args:
            ac_state (str): The power ac state to be set. Use `.AC_OFF`, `.AC_ON`

        Usage:
            self.driver.set_power_ac(Power.AC_OFF)
            self.driver.set_power_ac(Power.AC_ON)

        Returns:
            `appium.webdriver.webdriver.WebDriver`
        """
        self.execute(Command.SET_POWER_AC, {'state': ac_state})
        return self

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.SET_POWER_CAPACITY] = \
            ('POST', '/session/$sessionId/appium/device/power_capacity')
        self.command_executor._commands[Command.SET_POWER_AC] = \
            ('POST', '/session/$sessionId/appium/device/power_ac')
