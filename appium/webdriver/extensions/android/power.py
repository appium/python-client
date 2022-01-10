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

from typing import TYPE_CHECKING

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.webdriver.mobilecommand import MobileCommand as Command

if TYPE_CHECKING:
    from appium.webdriver.webdriver import WebDriver


class Power(CanExecuteCommands):

    AC_OFF, AC_ON = 'off', 'on'

    def set_power_capacity(self, percent: int) -> 'WebDriver':
        """Emulate power capacity change on the connected emulator.

        Android only.

        Args:
            percent: The power capacity to be set. Can be set from 0 to 100

        Usage:
            self.driver.set_power_capacity(50)

        Returns:
            Union['WebDriver', 'Power']: Self instance
        """
        self.execute(Command.SET_POWER_CAPACITY, {'percent': percent})
        return self  # type: ignore

    def set_power_ac(self, ac_state: str) -> 'WebDriver':
        """Emulate power state change on the connected emulator.

        Android only.

        Args:
            ac_state: The power ac state to be set. Use `Power.AC_OFF`, `Power.AC_ON`

        Usage:
            | self.driver.set_power_ac(Power.AC_OFF)
            | self.driver.set_power_ac(Power.AC_ON)

        Returns:
            Union['WebDriver', 'Power']: Self instance
        """
        self.execute(Command.SET_POWER_AC, {'state': ac_state})
        return self  # type: ignore

    def _add_commands(self) -> None:
        # noinspection PyProtectedMember,PyUnresolvedReferences
        commands = self.command_executor._commands
        commands[Command.SET_POWER_CAPACITY] = (
            'POST',
            '/session/$sessionId/appium/device/power_capacity',
        )
        commands[Command.SET_POWER_AC] = ('POST', '/session/$sessionId/appium/device/power_ac')
