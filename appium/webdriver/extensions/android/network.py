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

from typing import TYPE_CHECKING, cast

from selenium.common.exceptions import UnknownMethodException

from appium.common.helper import extract_const_attributes
from appium.common.logger import logger
from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.protocols.webdriver.can_remember_extension_presence import CanRememberExtensionPresence
from appium.webdriver.mobilecommand import MobileCommand as Command

if TYPE_CHECKING:
    from appium.webdriver.webdriver import WebDriver


class NetSpeed:
    GSM = 'gsm'  # GSM/CSD (up: 14.4(kbps), down: 14.4(kbps))
    SCSD = 'scsd'  # HSCSD (up: 14.4, down: 57.6)
    GPRS = 'gprs'  # GPRS (up: 28.8, down: 57.6)
    EDGE = 'edge'  # EDGE/EGPRS (up: 473.6, down: 473.6)
    UMTS = 'umts'  # UMTS/3G (up: 384.0, down: 384.0)
    HSDPA = 'hsdpa'  # HSDPA (up: 5760.0, down: 13,980.0)
    LTE = 'lte'  # LTE (up: 58,000, down: 173,000)
    EVDO = 'evdo'  # EVDO (up: 75,000, down: 280,000)
    FULL = 'full'  # No limit, the default (up: 0.0, down: 0.0)


class NetworkMask:
    WIFI = 0b010
    DATA = 0b100
    AIRPLANE_MODE = 0b001


class Network(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    @property
    def network_connection(self) -> int:
        """Returns an integer bitmask specifying the network connection type.

        Android only.
        Possible values are available through the enumeration `appium.webdriver.ConnectionType`

        This API only works reliably on emulators (any version) and real devices
        since API level 31.
        """
        ext_name = 'mobile: getConnectivity'
        try:
            result_map = self.assert_extension_exists(ext_name).execute_script(ext_name)
            return (
                (NetworkMask.WIFI if result_map['wifi'] else 0)
                | (NetworkMask.DATA if result_map['data'] else 0)
                | (NetworkMask.AIRPLANE_MODE if result_map['airplaneMode'] else 0)
            )
        except UnknownMethodException:
            # TODO: Remove the fallback
            return self.mark_extension_absence(ext_name).execute(Command.GET_NETWORK_CONNECTION, {})['value']

    def set_network_connection(self, connection_type: int) -> int:
        """Sets the network connection type. Android only.

        Possible values:

            +--------------------+------+------+---------------+
            | Value (Alias)      | Data | Wifi | Airplane Mode |
            +====================+======+======+===============+
            | 0 (None)           | 0    | 0    | 0             |
            +--------------------+------+------+---------------+
            | 1 (Airplane Mode)  | 0    | 0    | 1             |
            +--------------------+------+------+---------------+
            | 2 (Wifi only)      | 0    | 1    | 0             |
            +--------------------+------+------+---------------+
            | 4 (Data only)      | 1    | 0    | 0             |
            +--------------------+------+------+---------------+
            | 6 (All network on) | 1    | 1    | 0             |
            +--------------------+------+------+---------------+

        These are available through the enumeration `appium.webdriver.ConnectionType`

        This API only works reliably on emulators (any version) and real devices
        since API level 31.

        Args:
            connection_type: a member of the enum `appium.webdriver.ConnectionType`

        Return:
            int: Set network connection type
        """
        ext_name = 'mobile: setConnectivity'
        try:
            return self.assert_extension_exists(ext_name).execute_script(
                ext_name,
                {
                    'wifi': bool(connection_type & NetworkMask.WIFI),
                    'data': bool(connection_type & NetworkMask.DATA),
                    'airplaneMode': bool(connection_type & NetworkMask.AIRPLANE_MODE),
                },
            )
        except UnknownMethodException:
            # TODO: Remove the fallback
            return self.mark_extension_absence(ext_name).execute(
                Command.SET_NETWORK_CONNECTION, {'parameters': {'type': connection_type}}
            )['value']

    def toggle_wifi(self) -> 'WebDriver':
        """Toggle the wifi on the device, Android only.
        This API only works reliably on emulators (any version) and real devices
        since API level 31.

        Returns:
            Union['WebDriver', 'Network']: Self instance
        """
        ext_name = 'mobile: setConnectivity'
        try:
            self.assert_extension_exists(ext_name).execute_script(
                ext_name, {'wifi': not (self.network_connection & NetworkMask.WIFI)}
            )
        except UnknownMethodException:
            self.mark_extension_absence(ext_name).execute(Command.TOGGLE_WIFI, {})
        return cast('WebDriver', self)

    def set_network_speed(self, speed_type: str) -> 'WebDriver':
        """Set the network speed emulation.

        Android Emulator only.

        Args:
            speed_type: The network speed type.
                A member of the const appium.webdriver.extensions.android.network.NetSpeed.

        Usage:
            self.driver.set_network_speed(NetSpeed.LTE)

        Returns:
            Union['WebDriver', 'Network']: Self instance
        """
        constants = extract_const_attributes(NetSpeed)
        if speed_type not in constants.values():
            logger.warning(
                f'{speed_type} is unknown. Consider using one of {list(constants.keys())} constants. '
                f'(e.g. {NetSpeed.__name__}.LTE)'
            )
        ext_name = 'mobile: networkSpeed'
        try:
            self.assert_extension_exists(ext_name).execute_script(ext_name, {'speed': speed_type})
        except UnknownMethodException:
            # TODO: Remove the fallback
            self.mark_extension_absence(ext_name).execute(Command.SET_NETWORK_SPEED, {'netspeed': speed_type})
        return cast('WebDriver', self)

    def _add_commands(self) -> None:
        # noinspection PyProtectedMember,PyUnresolvedReferences
        commands = self.command_executor._commands
        commands[Command.TOGGLE_WIFI] = ('POST', '/session/$sessionId/appium/device/toggle_wifi')
        commands[Command.GET_NETWORK_CONNECTION] = (
            'GET',
            '/session/$sessionId/network_connection',
        )
        commands[Command.SET_NETWORK_CONNECTION] = (
            'POST',
            '/session/$sessionId/network_connection',
        )
        commands[Command.SET_NETWORK_SPEED] = (
            'POST',
            '/session/$sessionId/appium/device/network_speed',
        )
