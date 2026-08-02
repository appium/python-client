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

from typing_extensions import Self

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts


class Sms(CanExecuteCommands, CanExecuteScripts):
    def send_sms(self, phone_number: str, message: str) -> Self:
        """Emulate send SMS event on the connected emulator.

        Android only.

        Requires the Appium driver to support the `mobile: sendSms` execute method.

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
        self.execute_script(ext_name, args)
        return self
