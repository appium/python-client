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

from typing_extensions import Self

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts


class HardwareActions(CanExecuteCommands, CanExecuteScripts):
    def lock(self, seconds: Optional[int] = None) -> Self:
        """Lock the device. No changes are made if the device is already locked.

        Requires the Appium driver to support the `mobile: lock` execute method.

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
        self.execute_script(ext_name, args)
        return self

    def unlock(self) -> Self:
        """Unlock the device. No changes are made if the device is already unlocked.

        Requires the Appium driver to support the `mobile: isLocked` and `mobile: unlock` execute methods.

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        ext_name = 'mobile: unlock'
        if not self.execute_script('mobile: isLocked'):
            return self
        self.execute_script(ext_name)
        return self

    def is_locked(self) -> bool:
        """Checks whether the device is locked.

        Requires the Appium driver to support the `mobile: isLocked` execute method.

        Returns:
            `True` if the device is locked
        """
        ext_name = 'mobile: isLocked'
        return self.execute_script(ext_name)

    def shake(self) -> Self:
        """Shake the device.

        Requires the Appium driver to support the `mobile: shake` execute method.

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        ext_name = 'mobile: shake'
        self.execute_script(ext_name)
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
        """Authenticate users using a fingerprint scan on supported Android emulators.

        Requires the Appium driver to support the `mobile: fingerprint` execute method.

        Args:
            finger_id: Fingerprint identifier stored in the Android Keystore system (from 1 to 10)

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        ext_name = 'mobile: fingerprint'
        args = {'fingerprintId': finger_id}
        self.execute_script(ext_name, args)
        return self
