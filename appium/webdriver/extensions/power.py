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


class Power(webdriver.Remote):

    AC_OFF, AC_ON = 'off', 'on'

    def set_power_capacity(self, percent):
        """Emulate power capacity change on the connected emulator.

        :Args:
         - percent: The power capacity to be set. Can be set int from 0 to 100

        :Usage:
            self.driver.set_power_capacity(50)
        """
        if percent not in range(101):  # 0-100(int)
            raise TypeError('{} is out of range. Needs to be 0-100(int).'.format(percent))
        self.execute(Command.SET_POWER_CAPACITY, {'percent': percent})
        return self

    def set_power_ac(self, ac_state):
        """Emulate power state change on the connected emulator.

        :Args:
         - ac_state: The power ac state to be set

        :Usage:
            self.driver.set_power_ac(Power.AC_OFF)
            self.driver.set_power_ac(Power.AC_ON)
        """
        if ac_state not in [self.AC_OFF, self.AC_ON]:
            raise TypeError('{} is unexpected. Use Power.AC_OFF, Power.AC_ON'.format(ac_state))
        self.execute(Command.SET_POWER_AC, {'state': ac_state})
        return self

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.SET_POWER_CAPACITY] = \
            ('POST', '/session/$sessionId/appium/device/power_capacity')
        self.command_executor._commands[Command.SET_POWER_AC] = \
            ('POST', '/session/$sessionId/appium/device/power_ac')
