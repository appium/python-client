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

from selenium import webdriver
from ..mobilecommand import MobileCommand as Command


class Sms(webdriver.Remote):

    def send_sms(self, phone_number, message):
        """Emulate send SMS event on the connected emulator.

        :Args:
         - phone_number: The phone number of message sender
         - message: message: The message to send

        :Usage:
            self.driver.send_sms('555-123-4567', 'Hey lol')
        """
        self.execute(Command.SEND_SMS, {'phoneNumber': phone_number, 'message': message})

    def _addCommands(self):
        self.command_executor._commands[Command.SEND_SMS] = \
            ('POST', '/session/$sessionId/appium/device/send_sms')
