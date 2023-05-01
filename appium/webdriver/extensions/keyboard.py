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

from typing import TYPE_CHECKING, Dict, Optional, cast

from selenium.common.exceptions import UnknownMethodException

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.protocols.webdriver.can_remember_extension_presence import CanRememberExtensionPresence

from ..mobilecommand import MobileCommand as Command

if TYPE_CHECKING:
    from appium.webdriver.webdriver import WebDriver


class Keyboard(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    def hide_keyboard(
        self, key_name: Optional[str] = None, key: Optional[str] = None, strategy: Optional[str] = None
    ) -> 'WebDriver':
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
        ext_name = 'mobile: hideKeyboard'
        try:
            self.assert_extension_exists(ext_name).execute_script(
                ext_name, {**({'keys': [key or key_name]} if key or key_name else {})}
            )
        except UnknownMethodException:
            # TODO: Remove the fallback
            data: Dict[str, Optional[str]] = {}
            if key_name is not None:
                data['keyName'] = key_name
            elif key is not None:
                data['key'] = key
            elif strategy is None:
                strategy = 'tapOutside'
            data['strategy'] = strategy
            self.mark_extension_absence(ext_name).execute(Command.HIDE_KEYBOARD, data)
        return cast('WebDriver', self)

    def is_keyboard_shown(self) -> bool:
        """Attempts to detect whether a software keyboard is present

        Returns:
            `True` if keyboard is shown
        """
        ext_name = 'mobile: isKeyboardShown'
        try:
            return self.assert_extension_exists(ext_name).execute_script(ext_name)
        except UnknownMethodException:
            return self.mark_extension_absence(ext_name).execute(Command.IS_KEYBOARD_SHOWN)['value']

    def keyevent(self, keycode: int, metastate: Optional[int] = None) -> 'WebDriver':
        """Sends a keycode to the device.

        Android only.
        Possible keycodes can be found in http://developer.android.com/reference/android/view/KeyEvent.html.

        Args:
            keycode: the keycode to be sent to the device
            metastate: meta information about the keycode being sent

        Returns:
            Union['WebDriver', 'Keyboard']: Self instance
        """
        return self.press_keycode(keycode=keycode, metastate=metastate)

    def press_keycode(self, keycode: int, metastate: Optional[int] = None, flags: Optional[int] = None) -> 'WebDriver':
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
        ext_name = 'mobile: pressKey'
        args = {'keycode': keycode}
        if metastate is not None:
            args['metastate'] = metastate
        if flags is not None:
            args['flags'] = flags
        try:
            self.assert_extension_exists(ext_name).execute_script(ext_name, args)
        except UnknownMethodException:
            # TODO: Remove the fallback
            self.mark_extension_absence(ext_name).execute(Command.PRESS_KEYCODE, args)
        return cast('WebDriver', self)

    def long_press_keycode(
        self, keycode: int, metastate: Optional[int] = None, flags: Optional[int] = None
    ) -> 'WebDriver':
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
        ext_name = 'mobile: pressKey'
        args = {'keycode': keycode}
        if metastate is not None:
            args['metastate'] = metastate
        if flags is not None:
            args['flags'] = flags
        try:
            self.assert_extension_exists(ext_name).execute_script(
                ext_name,
                {
                    **args,
                    'isLongPress': True,
                },
            )
        except UnknownMethodException:
            # TODO: Remove the fallback
            self.mark_extension_absence(ext_name).execute(Command.LONG_PRESS_KEYCODE, args)
        return cast('WebDriver', self)

    def _add_commands(self) -> None:
        # noinspection PyProtectedMember,PyUnresolvedReferences
        commands = self.command_executor._commands
        commands[Command.HIDE_KEYBOARD] = (
            'POST',
            '/session/$sessionId/appium/device/hide_keyboard',
        )
        commands[Command.IS_KEYBOARD_SHOWN] = (
            'GET',
            '/session/$sessionId/appium/device/is_keyboard_shown',
        )
        commands[Command.KEY_EVENT] = ('POST', '/session/$sessionId/appium/device/keyevent')
        commands[Command.PRESS_KEYCODE] = (
            'POST',
            '/session/$sessionId/appium/device/press_keycode',
        )
        commands[Command.LONG_PRESS_KEYCODE] = (
            'POST',
            '/session/$sessionId/appium/device/long_press_keycode',
        )
