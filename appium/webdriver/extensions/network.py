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


class Network(webdriver.Remote):

    @property
    def network_connection(self):
        """Returns an integer bitmask specifying the network connection type.
        Android only.
        Possible values are available through the enumeration `appium.webdriver.ConnectionType`
        """
        return self.execute(Command.GET_NETWORK_CONNECTION, {})['value']

    def set_network_connection(self, connection_type):
        """Sets the network connection type. Android only.
        Possible values:
            Value (Alias)      | Data | Wifi | Airplane Mode
            -------------------------------------------------
            0 (None)           | 0    | 0    | 0
            1 (Airplane Mode)  | 0    | 0    | 1
            2 (Wifi only)      | 0    | 1    | 0
            4 (Data only)      | 1    | 0    | 0
            6 (All network on) | 1    | 1    | 0
        These are available through the enumeration `appium.webdriver.ConnectionType`

        :Args:
         - connectionType - a member of the enum appium.webdriver.ConnectionType
        """
        data = {
            'parameters': {
                'type': connection_type
            }
        }
        return self.execute(Command.SET_NETWORK_CONNECTION, data)['value']

    def toggle_wifi(self):
        """Toggle the wifi on the device, Android only.
        """
        self.execute(Command.TOGGLE_WIFI, {})
        return self

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.TOGGLE_WIFI] = \
            ('POST', '/session/$sessionId/appium/device/toggle_wifi')
        self.command_executor._commands[Command.GET_NETWORK_CONNECTION] = \
            ('GET', '/session/$sessionId/network_connection')
        self.command_executor._commands[Command.SET_NETWORK_CONNECTION] = \
            ('POST', '/session/$sessionId/network_connection')
