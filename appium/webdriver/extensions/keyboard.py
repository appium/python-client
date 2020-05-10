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

from typing import TYPE_CHECKING, Dict, Optional, TypeVar, Union

from selenium import webdriver

from ..mobilecommand import MobileCommand as Command

if TYPE_CHECKING:
    # noinspection PyUnresolvedReferences
    from appium.webdriver.webdriver import WebDriver

T = TypeVar('T', bound=Union['WebDriver', 'Keyboard'])


class Keyboard(webdriver.Remote):

    def hide_keyboard(self: T, key_name: Optional[str] = None, key: Optional[str]
                      = None, strategy: Optional[str] = None) -> T:
        """Hides the software keyboard on the device.

        In iOS, use `key_name` to press
        a particular key, or `strategy`. In Android, no parameters are used.

        Args:
            key_name: key to press
            key:
            strategy: strategy for closing the keyboard (e.g., `tapOutside`)

        Returns:
            Union['WebDriver', 'Keyboard']: Self instance
        """
        data: Dict[str, Optional[str]] = {}
        if key_name is not None:
            data['keyName'] = key_name
        elif key is not None:
            data['key'] = key
        elif strategy is None:
            strategy = 'tapOutside'
        data['strategy'] = strategy
        self.execute(Command.HIDE_KEYBOARD, data)
        return self

    def is_keyboard_shown(self: T) -> bool:
        """Attempts to detect whether a software keyboard is present

        Returns:
            `True` if keyboard is shown
        """
        return self.execute(Command.IS_KEYBOARD_SHOWN)['value']

    def keyevent(self: T, keycode: int, metastate: Optional[int] = None) -> T:
        """Sends a keycode to the device.

        Android only.
        Possible keycodes can be found in http://developer.android.com/reference/android/view/KeyEvent.html.

        Args:
            keycode: the keycode to be sent to the device
            metastate: meta information about the keycode being sent

        Returns:
            Union['WebDriver', 'Keyboard']: Self instance
        """
        data = {
            'keycode': keycode,
        }
        if metastate is not None:
            data['metastate'] = metastate
        self.execute(Command.KEY_EVENT, data)
        return self

    def press_keycode(self: T, keycode: int, metastate: Optional[int] = None, flags: Optional[int] = None) -> T:
        """Sends a keycode to the device.

        Android only. Possible keycodes can be found
        in http://developer.android.com/reference/android/view/KeyEvent.html.

        Args:
            keycode: the keycode to be sent to the device
            metastate: meta information about the keycode being sent
            flags: the set of key event flags

        Returns:
            Union['WebDriver', 'Keyboard']: Self instance
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

    def long_press_keycode(self: T, keycode: int, metastate: Optional[int] = None, flags: Optional[int] = None) -> T:
        """Sends a long press of keycode to the device.

        Android only. Possible keycodes can be found in
        http://developer.android.com/reference/android/view/KeyEvent.html.

        Args:
            keycode: the keycode to be sent to the device
            metastate: meta information about the keycode being sent
            flags: the set of key event flags

        Returns:
            Union['WebDriver', 'Keyboard']: Self instance
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
    # noinspection PyProtectedMember
    def _addCommands(self) -> None:
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
