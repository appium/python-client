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


class HardwareActions(webdriver.Remote):

    def lock(self, seconds=None):
        """Lock the device. No changes are made if the device is already unlocked.

        Args:
            seconds (optional): The duration to lock the device, in seconds.
                The device is going to be locked forever until `unlock` is called
                if it equals or is less than zero, otherwise this call blocks until
                the timeout expires and unlocks the screen automatically.

        Returns:
            `appium.webdriver.webdriver.WebDriver`
        """
        if seconds is None:
            self.execute(Command.LOCK)
        else:
            self.execute(Command.LOCK, {'seconds': seconds})

        return self

    def unlock(self):
        """Unlock the device. No changes are made if the device is already locked.

        Returns:
            `appium.webdriver.webdriver.WebDriver`
        """
        self.execute(Command.UNLOCK)
        return self

    def is_locked(self):
        """Checks whether the device is locked.

        Returns:
            bool: `True` if the device is locked
        """
        return self.execute(Command.IS_LOCKED)['value']

    def shake(self):
        """Shake the device.

        Returns:
            `appium.webdriver.webdriver.WebDriver`
        """
        self.execute(Command.SHAKE)
        return self

    def touch_id(self, match):
        """Simulate touchId on iOS Simulator

        Args:
            match (bool): Simulates a successful touch (`True`) or a failed touch (`False`)

        Returns:
            `appium.webdriver.webdriver.WebDriver`
        """
        data = {
            'match': match
        }
        self.execute(Command.TOUCH_ID, data)
        return self

    def toggle_touch_id_enrollment(self):
        """Toggle enroll touchId on iOS Simulator

        Returns:
            `appium.webdriver.webdriver.WebDriver`
        """
        self.execute(Command.TOGGLE_TOUCH_ID_ENROLLMENT)
        return self

    def finger_print(self, finger_id):
        """Authenticate users by using their finger print scans on supported Android emulators.

        Args:
            finger_id (int): Finger prints stored in Android Keystore system (from 1 to 10)

        Returns:
            TODO
        """
        return self.execute(Command.FINGER_PRINT, {'fingerprintId': finger_id})['value']

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.LOCK] = \
            ('POST', '/session/$sessionId/appium/device/lock')
        self.command_executor._commands[Command.UNLOCK] = \
            ('POST', '/session/$sessionId/appium/device/unlock')
        self.command_executor._commands[Command.IS_LOCKED] = \
            ('POST', '/session/$sessionId/appium/device/is_locked')
        self.command_executor._commands[Command.SHAKE] = \
            ('POST', '/session/$sessionId/appium/device/shake')
        self.command_executor._commands[Command.TOUCH_ID] = \
            ('POST', '/session/$sessionId/appium/simulator/touch_id')
        self.command_executor._commands[Command.TOGGLE_TOUCH_ID_ENROLLMENT] = \
            ('POST', '/session/$sessionId/appium/simulator/toggle_touch_id_enrollment')
        self.command_executor._commands[Command.FINGER_PRINT] = \
            ('POST', '/session/$sessionId/appium/device/finger_print')
