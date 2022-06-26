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

from typing import TypeVar

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.webdriver.mobilecommand import MobileCommand as Command

T = TypeVar('T', bound=CanExecuteCommands)


class Sms(CanExecuteCommands):
    def send_sms(self: T, phone_number: str, message: str) -> T:
        """Emulate send SMS event on the connected emulator.

        Android only.

        Args:
            phone_number: The phone number of message sender
            message: The message to send

        Usage:
            self.driver.send_sms('555-123-4567', 'Hey lol')

        Returns:
            Union['WebDriver', 'Sms']: Self instance
        """
        self.execute(Command.SEND_SMS, {'phoneNumber': phone_number, 'message': message})
        return self

    def _add_commands(self) -> None:
        # noinspection PyProtectedMember,PyUnresolvedReferences
        commands = self.command_executor._commands
        commands[Command.SEND_SMS] = ('POST', '/session/$sessionId/appium/device/send_sms')
