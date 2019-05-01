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

from appium.common.logger import logger
from ..gsm_signal_strength import GsmSignalStrength
from ..gsm_call_actions import GsmCallActions


class Gsm(webdriver.Remote):

    def make_gsm_call(self, phone_number, action):
        """Make GSM call (Emulator only)

        :Args:
         - phone_number (str): The phone number to call to.
         - action (str): The action - GsmCallActions.CALL/ACCEPT/CANCEL/HOLD

        :Usage:
            self.driver.make_gsm_call('5551234567', GsmCallActions.CALL)
        """
        if action not in self._dict_const(GsmCallActions).values():
            logger.warning('{} is invalid. Use the value in {}. (e.g. GsmCallActions.CALL)'.format(
                action, list(self._dict_const(GsmCallActions).keys())))
        self.execute(Command.MAKE_GSM_CALL, {'phoneNumber': phone_number, 'action': action})
        return self

    def set_gsm_signal(self, strength):
        """Set GSM signal strength (Emulator only)

        :Args:
         - strength: Signal strength. Can be set GsmSignalStrength.NONE_OR_UNKNOWN/POOR/MODERATE/GOOD/GREAT

        :Usage:
            self.driver.set_gsm_signal(GsmSignalStrength.GOOD)
        """
        if strength not in self._dict_const(GsmSignalStrength).values():
            logger.warning('{} is out of range. Use the value in {}. (e.g. GsmSignalStrength.GOOD)'.format(
                strength, list(self._dict_const(GsmSignalStrength).keys())))
        self.execute(Command.SET_GSM_SIGNAL, {'signalStrength': strength, 'signalStrengh': strength})
        return self

    def _dict_const(self, cls):
        return {attr: value for attr, value in vars(cls).items() if not callable(getattr(cls, attr)) and attr.isupper()}

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.MAKE_GSM_CALL] = \
            ('POST', '/session/$sessionId/appium/device/gsm_call')
        self.command_executor._commands[Command.SET_GSM_SIGNAL] = \
            ('POST', '/session/$sessionId/appium/device/gsm_signal')
