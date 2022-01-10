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

from typing import Optional

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands

from ..mobilecommand import MobileCommand as Command


class DeviceTime(CanExecuteCommands):
    @property
    def device_time(self) -> str:
        """Returns the date and time from the device.

        Return:
            str: The date and time
        """
        return self.execute(Command.GET_DEVICE_TIME_GET, {})['value']

    def get_device_time(self, format: Optional[str] = None) -> str:
        """Returns the date and time from the device.

        Args:
            format:  The set of format specifiers. Read https://momentjs.com/docs/
                to get the full list of supported datetime format specifiers.
                If unset, return :func:`.device_time` as default format is `YYYY-MM-DDTHH:mm:ssZ`,
                which complies to ISO-8601

        Usage:
            | self.driver.get_device_time()
            | self.driver.get_device_time("YYYY-MM-DD")

        Return:
            str: The date and time
        """
        if format is None:
            return self.device_time
        return self.execute(Command.GET_DEVICE_TIME_POST, {'format': format})['value']

    def _add_commands(self) -> None:
        # noinspection PyProtectedMember,PyUnresolvedReferences
        commands = self.command_executor._commands
        commands[Command.GET_DEVICE_TIME_GET] = (
            'GET',
            '/session/$sessionId/appium/device/system_time',
        )
        commands[Command.GET_DEVICE_TIME_POST] = (
            'POST',
            '/session/$sessionId/appium/device/system_time',
        )
