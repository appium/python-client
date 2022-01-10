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

from typing import TYPE_CHECKING

from appium.common.helper import extract_const_attributes
from appium.common.logger import logger
from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
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


class Gsm(CanExecuteCommands):
    def make_gsm_call(self, phone_number: str, action: str) -> 'WebDriver':
        """Make GSM call (Emulator only)

        Android only.

        Args:
            phone_number: The phone number to call to.
            action: The call action.
                A member of the const `appium.webdriver.extensions.android.gsm.GsmCallActions`

        Usage:
            self.driver.make_gsm_call('5551234567', GsmCallActions.CALL)

        Returns:
            Union['WebDriver', 'Gsm']: Self instance
        """
        constants = extract_const_attributes(GsmCallActions)
        if action not in constants.values():
            logger.warning(
                f'{action} is unknown. Consider using one of {list(constants.keys())} constants. '
                f'(e.g. {GsmCallActions.__name__}.CALL)'
            )
        self.execute(Command.MAKE_GSM_CALL, {'phoneNumber': phone_number, 'action': action})
        # noinspection PyTypeChecker
        return self

    def set_gsm_signal(self, strength: int) -> 'WebDriver':
        """Set GSM signal strength (Emulator only)

        Android only.

        Args:
            strength: Signal strength.
                A member of the enum :obj:`appium.webdriver.extensions.android.gsm.GsmSignalStrength`

        Usage:
            self.driver.set_gsm_signal(GsmSignalStrength.GOOD)

        Returns:
            Union['WebDriver', 'Gsm']: Self instance
        """
        constants = extract_const_attributes(GsmSignalStrength)
        if strength not in constants.values():
            logger.warning(
                f'{strength} is out of range. Consider using one of {list(constants.keys())} constants. '
                f'(e.g. {GsmSignalStrength.__name__}.GOOD)'
            )
        self.execute(Command.SET_GSM_SIGNAL, {'signalStrength': strength, 'signalStrengh': strength})
        # noinspection PyTypeChecker
        return self

    def set_gsm_voice(self, state: str) -> 'WebDriver':
        """Set GSM voice state (Emulator only)

        Android only.

        Args:
            state: State of GSM voice.
                A member of the const `appium.webdriver.extensions.android.gsm.GsmVoiceState`

        Usage:
            self.driver.set_gsm_voice(GsmVoiceState.HOME)

        Returns:
            Union['WebDriver', 'Gsm']: Self instance
        """
        constants = extract_const_attributes(GsmVoiceState)
        if state not in constants.values():
            logger.warning(
                f'{state} is unknown. Consider using one of {list(constants.keys())} constants. '
                f'(e.g. {GsmVoiceState.__name__}.HOME)'
            )
        self.execute(Command.SET_GSM_VOICE, {'state': state})
        # noinspection PyTypeChecker
        return self

    def _add_commands(self) -> None:
        # noinspection PyProtectedMember,PyUnresolvedReferences
        commands = self.command_executor._commands
        commands[Command.MAKE_GSM_CALL] = ('POST', '/session/$sessionId/appium/device/gsm_call')
        commands[Command.SET_GSM_SIGNAL] = (
            'POST',
            '/session/$sessionId/appium/device/gsm_signal',
        )
        commands[Command.SET_GSM_VOICE] = ('POST', '/session/$sessionId/appium/device/gsm_voice')
