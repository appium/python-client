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


class Gsm(webdriver.Remote):

    (
        NONE_OR_UNKNOWN,
        POOR,
        MODERATE,
        GOOD,
        GREAT
    ) = range(5)

    def set_gsm_signal(self, strength):
        """Set GSM signal strength (Emulator only)

        :Args:
         - strength: Signal strength. Can be set Gsm.NONE_OR_UNKNOWN/POOR/MODERATE/GOOD/GREAT

        :Usage:
            self.driver.set_gsm_signal(Gsm.GOOD)
        """
        if strength not in self._dict_signal_strength().values():
            logger.warning('{} is out of range. Use the value in {}.'.format(
                strength, list(self._dict_signal_strength().keys())))
        self.execute(Command.SET_GSM_SIGNAL, {'signalStrength': strength, 'signalStrengh': strength})
        return self

    def _dict_signal_strength(self):
        return {'{}.{}'.format(Gsm.__name__, attr): value for attr, value in vars(Gsm).items()
                if not callable(getattr(Gsm, attr)) and attr.isupper()}

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.SET_GSM_SIGNAL] = \
            ('POST', '/session/$sessionId/appium/device/gsm_signal')
