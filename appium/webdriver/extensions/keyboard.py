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


from typing_extensions import Self

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts


class Keyboard(CanExecuteCommands, CanExecuteScripts):
    def hide_keyboard(self, key_name: str | None = None, key: str | None = None, strategy: str | None = None) -> Self:
        """Hides the software keyboard on the device.

        On iOS, use `key_name` or `key` to provide a keyboard key name.
        On Android, no parameters are used. `strategy` is retained for compatibility and ignored.

        Requires the Appium driver to support the `mobile: hideKeyboard` execute method.

        Args:
            key_name: Keyboard key name to use on iOS
            key: Alias for `key_name`
            strategy: Legacy argument retained for compatibility; ignored by `mobile: hideKeyboard`

        Returns:
            Union['WebDriver', 'Keyboard']: Self instance
        """
        ext_name = 'mobile: hideKeyboard'
        self.execute_script(ext_name, {**({'keys': [key or key_name]} if key or key_name else {})})
        return self

    def is_keyboard_shown(self) -> bool:
        """Attempts to detect whether a software keyboard is present

        Requires the Appium driver to support the `mobile: isKeyboardShown` execute method.

        Returns:
            `True` if keyboard is shown
        """
        ext_name = 'mobile: isKeyboardShown'
        return self.execute_script(ext_name)

    def keyevent(self, keycode: int, metastate: int | None = None) -> Self:
        """Sends a keycode to the device.

        Android only.
        Possible keycodes can be found in http://developer.android.com/reference/android/view/KeyEvent.html.

        Requires the Appium driver to support the `mobile: pressKey` execute method.

        Args:
            keycode: the keycode to be sent to the device
            metastate: meta information about the keycode being sent

        Returns:
            Union['WebDriver', 'Keyboard']: Self instance
        """
        return self.press_keycode(keycode=keycode, metastate=metastate)

    def press_keycode(self, keycode: int, metastate: int | None = None, flags: int | None = None) -> Self:
        """Sends a keycode to the device.

        Android only. Possible keycodes can be found
        in http://developer.android.com/reference/android/view/KeyEvent.html.

        Requires the Appium driver to support the `mobile: pressKey` execute method.

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
        self.execute_script(ext_name, args)
        return self

    def long_press_keycode(self, keycode: int, metastate: int | None = None, flags: int | None = None) -> Self:
        """Sends a long press of keycode to the device.

        Android only. Possible keycodes can be found in
        http://developer.android.com/reference/android/view/KeyEvent.html.

        Requires the Appium driver to support the `mobile: pressKey` execute method.

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
        self.execute_script(
            ext_name,
            {
                **args,
                'isLongPress': True,
            },
        )
        return self
