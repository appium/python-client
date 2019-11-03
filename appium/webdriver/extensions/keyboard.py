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


class Keyboard(webdriver.Remote):

    def hide_keyboard(self, key_name=None, key=None, strategy=None):
        """Hides the software keyboard on the device.

        In iOS, use `key_name` to press
        a particular key, or `strategy`. In Android, no parameters are used.

        Args:
            key_name (:obj:`str`, optional): key to press
            key (:obj:`str`, optional):
            strategy (:obj:`str`, optional): strategy for closing the keyboard (e.g., `tapOutside`)
        """
        data = {}
        if key_name is not None:
            data['keyName'] = key_name
        elif key is not None:
            data['key'] = key
        elif strategy is None:
            strategy = 'tapOutside'
        data['strategy'] = strategy
        self.execute(Command.HIDE_KEYBOARD, data)
        return self

    def is_keyboard_shown(self):
        """Attempts to detect whether a software keyboard is present

        Returns:
            bool: `True` if keyboard is shown
        """
        return self.execute(Command.IS_KEYBOARD_SHOWN)['value']

    def keyevent(self, keycode, metastate=None):
        """Sends a keycode to the device.

        Android only.
        Possible keycodes can be found in http://developer.android.com/reference/android/view/KeyEvent.html.

        Args:
            keycode (int): the keycode to be sent to the device
            metastate (:obj:`int`, optional): meta information about the keycode being sent

        Returns:
            `appium.webdriver.webdriver.WebDriver`
        """
        data = {
            'keycode': keycode,
        }
        if metastate is not None:
            data['metastate'] = metastate
        self.execute(Command.KEY_EVENT, data)
        return self

    def press_keycode(self, keycode, metastate=None, flags=None):
        """Sends a keycode to the device.

        Android only. Possible keycodes can be found in http://developer.android.com/reference/android/view/KeyEvent.html.

        Args:
            keycode (int): the keycode to be sent to the device
            metastate (:obj:`int`, optional): meta information about the keycode being sent
            flags (:obj:`int`, optional): the set of key event flags

        Returns:
            `appium.webdriver.webdriver.WebDriver`
        """
        data = {
            'keycode': keycode,
        }
        if metastate is not None:
            data['metastate'] = metastate
        if flags is not None:
            data['flags'] = flags
        self.execute(Command.PRESS_KEYCODE, data)
        return self

    def long_press_keycode(self, keycode, metastate=None, flags=None):
        """Sends a long press of keycode to the device.

        Android only. Possible keycodes can be found in http://developer.android.com/reference/android/view/KeyEvent.html.

        Args:
            keycode (int): the keycode to be sent to the device
            metastate (:obj:`int`, optional): meta information about the keycode being sent
            flags (:obj:`int`, optional): the set of key event flags

        Returns:
            `appium.webdriver.webdriver.WebDriver`
        """
        data = {
            'keycode': keycode
        }
        if metastate is not None:
            data['metastate'] = metastate
        if flags is not None:
            data['flags'] = flags
        self.execute(Command.LONG_PRESS_KEYCODE, data)
        return self

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.HIDE_KEYBOARD] = \
            ('POST', '/session/$sessionId/appium/device/hide_keyboard')
        self.command_executor._commands[Command.IS_KEYBOARD_SHOWN] = \
            ('GET', '/session/$sessionId/appium/device/is_keyboard_shown')
        self.command_executor._commands[Command.KEY_EVENT] = \
            ('POST', '/session/$sessionId/appium/device/keyevent')
        self.command_executor._commands[Command.PRESS_KEYCODE] = \
            ('POST', '/session/$sessionId/appium/device/press_keycode')
        self.command_executor._commands[Command.LONG_PRESS_KEYCODE] = \
            ('POST', '/session/$sessionId/appium/device/long_press_keycode')
