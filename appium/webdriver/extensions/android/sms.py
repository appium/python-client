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


class Sms(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    def send_sms(self, phone_number: str, message: str) -> Self:
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
        ext_name = 'mobile: sendSms'
        args = {'phoneNumber': phone_number, 'message': message}
        try:
            self.assert_extension_exists(ext_name).execute_script(ext_name, args)
        except UnknownMethodException:
            # TODO: Remove the fallback
            self.mark_extension_absence(ext_name).execute(Command.SEND_SMS, args)
        return self

    def _add_commands(self) -> None:
        self.command_executor.add_command(Command.SEND_SMS, 'POST', '/session/$sessionId/appium/device/send_sms')
