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

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.webdriver.mobilecommand import MobileCommand as Command


class Display(CanExecuteCommands):
    def get_display_density(self) -> int:
        """Get the display density, Android only

        Returns:
            The display density of the Android device(dpi)

        Usage:
            self.driver.get_display_density()

        Return:
            int: The display density
        """
        return self.execute(Command.GET_DISPLAY_DENSITY)['value']

    def _add_commands(self) -> None:
        # noinspection PyProtectedMember,PyUnresolvedReferences
        commands = self.command_executor._commands
        commands[Command.GET_DISPLAY_DENSITY] = (
            'GET',
            '/session/$sessionId/appium/device/display_density',
        )
