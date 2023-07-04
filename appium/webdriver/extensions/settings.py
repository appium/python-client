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

from typing import TYPE_CHECKING, Any, Dict, cast

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands

from ..mobilecommand import MobileCommand as Command

if TYPE_CHECKING:
    from appium.webdriver.webdriver import WebDriver


class Settings(CanExecuteCommands):
    def get_settings(self) -> Dict[str, Any]:
        """Returns the appium server Settings for the current session.

        Do not get Settings confused with Desired Capabilities, they are
        separate concepts. See https://github.com/appium/appium/blob/master/docs/en/advanced-concepts/settings.md

        Returns:
            Current settings
        """
        return self.execute(Command.GET_SETTINGS, {})['value']

    def update_settings(self, settings: Dict[str, Any]) -> 'WebDriver':
        """Set settings for the current session.

        For more on settings, see: https://github.com/appium/appium/blob/master/docs/en/advanced-concepts/settings.md

        Args:
            settings: dictionary of settings to apply to the current test session
        """
        self.execute(Command.UPDATE_SETTINGS, {'settings': settings})
        return cast('WebDriver', self)

    def _add_commands(self) -> None:
        # noinspection PyProtectedMember,PyUnresolvedReferences
        commands = self.command_executor._commands
        commands[Command.GET_SETTINGS] = ('GET', '/session/$sessionId/appium/settings')
        commands[Command.UPDATE_SETTINGS] = ('POST', '/session/$sessionId/appium/settings')
