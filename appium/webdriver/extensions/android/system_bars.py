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

from typing import Dict, Union

from selenium.common.exceptions import UnknownMethodException

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.protocols.webdriver.can_remember_extension_presence import CanRememberExtensionPresence
from appium.webdriver.mobilecommand import MobileCommand as Command


class SystemBars(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    def get_system_bars(self) -> Dict[str, Dict[str, Union[int, bool]]]:
        """Retrieve visibility and bounds information of the status and navigation bars.

        Android only.

        Returns:
            A dictionary whose keys are
               - statusBar
                   - visible
                   - x
                   - y
                   - width
                   - height
               - navigationBar
                   - visible
                   - x
                   - y
                   - width
                   - height
        """
        ext_name = 'mobile: getSystemBars'
        try:
            return self.assert_extension_exists(ext_name).execute_script(ext_name)
        except UnknownMethodException:
            # TODO: Remove the fallback
            return self.mark_extension_absence(ext_name).execute(Command.GET_SYSTEM_BARS)['value']

    def _add_commands(self) -> None:
        # noinspection PyProtectedMember,PyUnresolvedReferences
        commands = self.command_executor._commands
        commands[Command.GET_SYSTEM_BARS] = (
            'GET',
            '/session/$sessionId/appium/device/system_bars',
        )
