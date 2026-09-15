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

from selenium.common.exceptions import UnknownMethodException
from typing_extensions import Self

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.protocols.webdriver.can_remember_extension_presence import CanRememberExtensionPresence
from appium.webdriver.mobilecommand import MobileCommand as Command


class Power(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    AC_OFF, AC_ON = 'off', 'on'

    def set_power_capacity(self, percent: int) -> Self:
        """Emulate power capacity change on the connected emulator.

        Android only.

        Args:
            percent: The power capacity to be set. Can be set from 0 to 100

        Usage:
            self.driver.set_power_capacity(50)

        Returns:
            Union['WebDriver', 'Power']: Self instance
        """
        ext_name = 'mobile: powerCapacity'
        args = {'percent': percent}
        try:
            self.assert_extension_exists(ext_name).execute_script(ext_name, args)
        except UnknownMethodException:
            # TODO: Remove the fallback
            self.mark_extension_absence(ext_name).execute(Command.SET_POWER_CAPACITY, args)
        return self

    def set_power_ac(self, ac_state: str) -> Self:
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
        ext_name = 'mobile: powerAC'
        args = {'state': ac_state}
        try:
            self.assert_extension_exists(ext_name).execute_script(ext_name, args)
        except UnknownMethodException:
            # TODO: Remove the fallback
            self.mark_extension_absence(ext_name).execute(Command.SET_POWER_AC, args)
        return self

    def _add_commands(self) -> None:
        self.command_executor.add_command(
            Command.SET_POWER_CAPACITY,
            'POST',
            '/session/$sessionId/appium/device/power_capacity',
        )
        self.command_executor.add_command(Command.SET_POWER_AC, 'POST', '/session/$sessionId/appium/device/power_ac')
