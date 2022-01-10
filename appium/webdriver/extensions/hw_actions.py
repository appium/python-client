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

from typing import TYPE_CHECKING, Any, Optional

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands

from ..mobilecommand import MobileCommand as Command

if TYPE_CHECKING:
    from appium.webdriver.webdriver import WebDriver


class HardwareActions(CanExecuteCommands):
    def lock(self, seconds: Optional[int] = None) -> 'WebDriver':
        """Lock the device. No changes are made if the device is already unlocked.

        Args:
            seconds: The duration to lock the device, in seconds.
                The device is going to be locked forever until `unlock` is called
                if it equals or is less than zero, otherwise this call blocks until
                the timeout expires and unlocks the screen automatically.

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        if seconds is None:
            self.execute(Command.LOCK)
        else:
            self.execute(Command.LOCK, {'seconds': seconds})
        return self  # type: ignore

    def unlock(self) -> 'WebDriver':
        """Unlock the device. No changes are made if the device is already locked.

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        self.execute(Command.UNLOCK)
        return self  # type: ignore

    def is_locked(self) -> bool:
        """Checks whether the device is locked.

        Returns:
            `True` if the device is locked
        """
        return self.execute(Command.IS_LOCKED)['value']

    def shake(self) -> 'WebDriver':
        """Shake the device.

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        self.execute(Command.SHAKE)
        return self  # type: ignore

    def touch_id(self, match: bool) -> 'WebDriver':
        """Simulate touchId on iOS Simulator

        Args:
            match: Simulates a successful touch (`True`) or a failed touch (`False`)

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        data = {'match': match}
        self.execute(Command.TOUCH_ID, data)
        return self  # type: ignore

    def toggle_touch_id_enrollment(self) -> 'WebDriver':
        """Toggle enroll touchId on iOS Simulator

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        self.execute(Command.TOGGLE_TOUCH_ID_ENROLLMENT)
        return self  # type: ignore

    def finger_print(self, finger_id: int) -> Any:
        """Authenticate users by using their finger print scans on supported Android emulators.

        Args:
            finger_id: Finger prints stored in Android Keystore system (from 1 to 10)

        Returns:
            TODO
        """
        return self.execute(Command.FINGER_PRINT, {'fingerprintId': finger_id})['value']

    def _add_commands(self) -> None:
        # noinspection PyProtectedMember,PyUnresolvedReferences
        commands = self.command_executor._commands
        commands[Command.LOCK] = ('POST', '/session/$sessionId/appium/device/lock')
        commands[Command.UNLOCK] = ('POST', '/session/$sessionId/appium/device/unlock')
        commands[Command.IS_LOCKED] = ('POST', '/session/$sessionId/appium/device/is_locked')
        commands[Command.SHAKE] = ('POST', '/session/$sessionId/appium/device/shake')
        commands[Command.TOUCH_ID] = ('POST', '/session/$sessionId/appium/simulator/touch_id')
        commands[Command.TOGGLE_TOUCH_ID_ENROLLMENT] = (
            'POST',
            '/session/$sessionId/appium/simulator/toggle_touch_id_enrollment',
        )
        commands[Command.FINGER_PRINT] = (
            'POST',
            '/session/$sessionId/appium/device/finger_print',
        )
