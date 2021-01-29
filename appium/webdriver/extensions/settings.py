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

from typing import TYPE_CHECKING, Any, Dict, TypeVar, Union

from selenium import webdriver

from ..mobilecommand import MobileCommand as Command

if TYPE_CHECKING:
    # noinspection PyUnresolvedReferences
    from appium.webdriver.webdriver import WebDriver

T = TypeVar('T', bound=Union['WebDriver', 'Settings'])


class Settings(webdriver.Remote):
    def get_settings(self: T) -> Dict[str, Any]:
        """Returns the appium server Settings for the current session.

        Do not get Settings confused with Desired Capabilities, they are
        separate concepts. See https://github.com/appium/appium/blob/master/docs/en/advanced-concepts/settings.md

        Returns:
            Current settings
        """
        return self.execute(Command.GET_SETTINGS, {})['value']

    def update_settings(self: T, settings: Dict[str, Any]) -> T:
        """Set settings for the current session.

        For more on settings, see: https://github.com/appium/appium/blob/master/docs/en/advanced-concepts/settings.md

        Args:
            settings: dictionary of settings to apply to the current test session
        """
        data = {"settings": settings}

        self.execute(Command.UPDATE_SETTINGS, data)
        return self

    # pylint: disable=protected-access
    # noinspection PyProtectedMember
    def _addCommands(self) -> None:
        self.command_executor._commands[Command.GET_SETTINGS] = ('GET', '/session/$sessionId/appium/settings')
        self.command_executor._commands[Command.UPDATE_SETTINGS] = ('POST', '/session/$sessionId/appium/settings')
