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

from typing import TYPE_CHECKING, Dict, TypeVar, Union

from selenium import webdriver

from appium.webdriver.mobilecommand import MobileCommand as Command

if TYPE_CHECKING:
    # noinspection PyUnresolvedReferences
    from appium.webdriver.webdriver import WebDriver

T = TypeVar('T', bound=Union['WebDriver', 'SystemBars'])


class SystemBars(webdriver.Remote):
    def get_system_bars(self: T) -> Dict[str, Dict[str, Union[int, bool]]]:
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
        return self.execute(Command.GET_SYSTEM_BARS)['value']

    # pylint: disable=protected-access
    # noinspection PyProtectedMember
    def _addCommands(self) -> None:
        self.command_executor._commands[Command.GET_SYSTEM_BARS] = (
            'GET',
            '/session/$sessionId/appium/device/system_bars',
        )
