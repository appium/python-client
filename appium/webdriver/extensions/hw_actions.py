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

from typing import Optional

from selenium.common.exceptions import UnknownMethodException
from typing_extensions import Self

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.protocols.webdriver.can_remember_extension_presence import CanRememberExtensionPresence

from ..mobilecommand import MobileCommand as Command


class HardwareActions(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    def lock(self, seconds: Optional[int] = None) -> Self:
        """Lock the device. No changes are made if the device is already unlocked.

        Args:
            seconds: The duration to lock the device, in seconds.
                The device is going to be locked forever until `unlock` is called
                if it equals or is less than zero, otherwise this call blocks until
                the timeout expires and unlocks the screen automatically.

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        ext_name = 'mobile: lock'
        args = {'seconds': seconds or 0}
        try:
            self.assert_extension_exists(ext_name).execute_script(ext_name, args)
        except UnknownMethodException:
            # TODO: Remove the fallback
            self.mark_extension_absence(ext_name).execute(Command.LOCK, args)
        return self

    def unlock(self) -> Self:
        """Unlock the device. No changes are made if the device is already locked.

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        ext_name = 'mobile: unlock'
        try:
            if not self.assert_extension_exists(ext_name).execute_script('mobile: isLocked'):
                return self
            self.execute_script(ext_name)
        except UnknownMethodException:
            # TODO: Remove the fallback
            self.mark_extension_absence(ext_name).execute(Command.UNLOCK)
        return self

    def is_locked(self) -> bool:
        """Checks whether the device is locked.

        Returns:
            `True` if the device is locked
        """
        ext_name = 'mobile: isLocked'
        try:
            return self.assert_extension_exists(ext_name).execute_script('mobile: isLocked')
        except UnknownMethodException:
            # TODO: Remove the fallback
            return self.mark_extension_absence(ext_name).execute(Command.IS_LOCKED)['value']

    def shake(self) -> Self:
        """Shake the device.

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        ext_name = 'mobile: shake'
        try:
            self.assert_extension_exists(ext_name).execute_script(ext_name)
        except UnknownMethodException:
            # TODO: Remove the fallback
            self.mark_extension_absence(ext_name).execute(Command.SHAKE)
        return self

    def touch_id(self, match: bool) -> Self:
        """Simulate touchId on iOS Simulator

        Args:
            match: Simulates a successful touch (`True`) or a failed touch (`False`)

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        self.execute_script(
            'mobile: sendBiometricMatch',
            {
                'type': 'touchId',
                'match': match,
            },
        )
        return self

    def toggle_touch_id_enrollment(self) -> Self:
        """Toggle enroll touchId on iOS Simulator

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        is_enrolled = self.execute_script('mobile: isBiometricEnrolled')
        self.execute_script('mobile: enrollBiometric', {'isEnabled': not is_enrolled})
        return self

    def finger_print(self, finger_id: int) -> Self:
        """Authenticate users by using their finger print scans on supported Android emulators.

        Args:
            finger_id: Finger prints stored in Android Keystore system (from 1 to 10)
        """
        ext_name = 'mobile: fingerprint'
        args = {'fingerprintId': finger_id}
        try:
            self.assert_extension_exists(ext_name).execute_script(ext_name, args)
        except UnknownMethodException:
            self.mark_extension_absence(ext_name).execute(Command.FINGER_PRINT, args)
        return self

    def _add_commands(self) -> None:
        self.command_executor.add_command(Command.LOCK, 'POST', '/session/$sessionId/appium/device/lock')
        self.command_executor.add_command(Command.UNLOCK, 'POST', '/session/$sessionId/appium/device/unlock')
        self.command_executor.add_command(Command.IS_LOCKED, 'POST', '/session/$sessionId/appium/device/is_locked')
        self.command_executor.add_command(Command.SHAKE, 'POST', '/session/$sessionId/appium/device/shake')
        self.command_executor.add_command(Command.TOUCH_ID, 'POST', '/session/$sessionId/appium/simulator/touch_id')
        self.command_executor.add_command(
            Command.TOGGLE_TOUCH_ID_ENROLLMENT,
            'POST',
            '/session/$sessionId/appium/simulator/toggle_touch_id_enrollment',
        )
        self.command_executor.add_command(
            Command.FINGER_PRINT,
            'POST',
            '/session/$sessionId/appium/device/finger_print',
        )
