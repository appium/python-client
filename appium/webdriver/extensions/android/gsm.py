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

from typing import TYPE_CHECKING, TypeVar

from selenium import webdriver

from appium.common.helper import extract_const_attributes
from appium.common.logger import logger
from appium.webdriver.mobilecommand import MobileCommand as Command

if TYPE_CHECKING:
    from appium.webdriver.webdriver import WebDriver


class GsmCallActions:
    CALL = 'call'
    ACCEPT = 'accept'
    CANCEL = 'cancel'
    HOLD = 'hold'


class GsmSignalStrength:
    NONE_OR_UNKNOWN = 0
    POOR = 1
    MODERATE = 2
    GOOD = 3
    GREAT = 4


class GsmVoiceState:
    UNREGISTERED = 'unregistered'
    HOME = 'home'
    ROAMING = 'roaming'
    SEARCHING = 'searching'
    DENIED = 'denied'
    OFF = 'off'
    ON = 'on'


T = TypeVar('T', bound='WebDriver')


class Gsm(webdriver.Remote):

    def make_gsm_call(self, phone_number: str, action: str) -> T:
        """Make GSM call (Emulator only)

        Android only.

        Args:
            phone_number (str): The phone number to call to.
            action (str): The call action.
                A member of the const `appium.webdriver.extensions.android.gsm.GsmCallActions`

        :Usage:
            self.driver.make_gsm_call('5551234567', GsmCallActions.CALL)
        """
        constants = extract_const_attributes(GsmCallActions)
        if action not in constants.values():
            logger.warning(
                f'{action} is unknown. Consider using one of {list(constants.keys())} constants. (e.g. {GsmCallActions.__name__}.CALL)')
        self.execute(Command.MAKE_GSM_CALL, {'phoneNumber': phone_number, 'action': action})
        return self

    def set_gsm_signal(self, strength: int) -> T:
        """Set GSM signal strength (Emulator only)

        Android only.

        Args:
            strength (int): Signal strength.
                A member of the enum `appium.webdriver.extensions.android.gsm.GsmSignalStrength`

        Usage:
            self.driver.set_gsm_signal(GsmSignalStrength.GOOD)
        """
        constants = extract_const_attributes(GsmSignalStrength)
        if strength not in constants.values():
            logger.warning(
                f'{strength} is out of range. Consider using one of {list(constants.keys())} constants. (e.g. {GsmSignalStrength.__name__}.GOOD)')
        self.execute(Command.SET_GSM_SIGNAL, {'signalStrength': strength, 'signalStrengh': strength})
        return self

    def set_gsm_voice(self, state: str) -> T:
        """Set GSM voice state (Emulator only)

        Android only.

        Args:
            state (str): State of GSM voice.
                A member of the const `appium.webdriver.extensions.android.gsm.GsmVoiceState`

        Usage:
            self.driver.set_gsm_voice(GsmVoiceState.HOME)
        """
        constants = extract_const_attributes(GsmVoiceState)
        if state not in constants.values():
            logger.warning(
                f'{state} is unknown. Consider using one of {list(constants.keys())} constants. (e.g. {GsmVoiceState.__name__}.HOME)')
        self.execute(Command.SET_GSM_VOICE, {'state': state})
        return self

    # pylint: disable=protected-access

    def _addCommands(self) -> None:
        self.command_executor._commands[Command.MAKE_GSM_CALL] = \
            ('POST', '/session/$sessionId/appium/device/gsm_call')
        self.command_executor._commands[Command.SET_GSM_SIGNAL] = \
            ('POST', '/session/$sessionId/appium/device/gsm_signal')
        self.command_executor._commands[Command.SET_GSM_VOICE] = \
            ('POST', '/session/$sessionId/appium/device/gsm_voice')
