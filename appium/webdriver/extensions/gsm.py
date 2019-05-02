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
from appium.common.helper import extract_const_attributes


class GsmCallActions(object):
    CALL = 'call'
    ACCEPT = 'accept'
    CANCEL = 'cancel'
    HOLD = 'hold'


class GsmSignalStrength(object):
    NONE_OR_UNKNOWN = 0
    POOR = 1
    MODERATE = 2
    GOOD = 3
    GREAT = 4


class Gsm(webdriver.Remote):

    def make_gsm_call(self, phone_number, action):
        """Make GSM call (Emulator only)

        :Args:
         - phone_number (str): The phone number to call to.
         - action (str): The call action - GsmCallActions.CALL/ACCEPT/CANCEL/HOLD

        :Usage:
            self.driver.make_gsm_call('5551234567', GsmCallActions.CALL)
        """
        constants = extract_const_attributes(GsmCallActions)
        if action not in constants.values():
            logger.warning('{} is unknown. Consider using one of {} constants. (e.g. {}.CALL)'.format(
                action, list(constants.keys()), GsmCallActions.__name__))
        self.execute(Command.MAKE_GSM_CALL, {'phoneNumber': phone_number, 'action': action})
        return self

    def set_gsm_signal(self, strength):
        """Set GSM signal strength (Emulator only)

        :Args:
         - strength (int): Signal strength - GsmSignalStrength.NONE_OR_UNKNOWN/POOR/MODERATE/GOOD/GREAT

        :Usage:
            self.driver.set_gsm_signal(GsmSignalStrength.GOOD)
        """
        constants = extract_const_attributes(GsmSignalStrength)
        if strength not in constants.values():
            logger.warning('{} is out of range. Consider using one of {} constants. (e.g. {}.GOOD)'.format(
                strength, list(constants.keys()), GsmSignalStrength.__name__))
        self.execute(Command.SET_GSM_SIGNAL, {'signalStrength': strength, 'signalStrengh': strength})
        return self

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.MAKE_GSM_CALL] = \
            ('POST', '/session/$sessionId/appium/device/gsm_call')
        self.command_executor._commands[Command.SET_GSM_SIGNAL] = \
            ('POST', '/session/$sessionId/appium/device/gsm_signal')
