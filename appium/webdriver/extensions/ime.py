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

import warnings
from typing import TYPE_CHECKING, List, cast

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands

from ..mobilecommand import MobileCommand as Command

if TYPE_CHECKING:
    from appium.webdriver.webdriver import WebDriver


class IME(CanExecuteCommands):
    @property
    def available_ime_engines(self) -> List[str]:
        """Get the available input methods for an Android device.

        Package and activity are returned (e.g., ['com.android.inputmethod.latin/.LatinIME'])
        Android only.

        deprecated:: 2.0.0

        Returns:
            :obj:`list` of :obj:`str`: The available input methods for an Android device
        """
        warnings.warn(
            'The "available_ime_engines" API is deprecated and will be removed in future versions. '
            'Use "mobile: shell" extension instead',
            DeprecationWarning,
        )

        return self.execute(Command.GET_AVAILABLE_IME_ENGINES, {})['value']  # pylint: disable=unsubscriptable-object

    def is_ime_active(self) -> bool:
        """Checks whether the device has IME service active.
        Android only.

        deprecated:: 2.0.0

        Returns:
            `True` if IME service is active
        """
        warnings.warn(
            'The "is_ime_active" API is deprecated and will be removed in future versions. '
            'Use "mobile: shell" extension instead',
            DeprecationWarning,
        )

        return self.execute(Command.IS_IME_ACTIVE, {})['value']  # pylint: disable=unsubscriptable-object

    def activate_ime_engine(self, engine: str) -> 'WebDriver':
        """Activates the given IME engine on the device.

        Android only.

        deprecated:: 2.0.0

        Args:
           engine: the package and activity of the IME engine to activate
               (e.g., 'com.android.inputmethod.latin/.LatinIME')

        Returns:
            Union['WebDriver', 'IME']: Self instance
        """
        warnings.warn(
            'The "activate_ime_engine" API is deprecated and will be removed in future versions. '
            'Use "mobile: shell" extension instead',
            DeprecationWarning,
        )

        data = {'engine': engine}
        self.execute(Command.ACTIVATE_IME_ENGINE, data)
        return cast('WebDriver', self)

    def deactivate_ime_engine(self) -> 'WebDriver':
        """Deactivates the currently active IME engine on the device.

        Android only.

        deprecated:: 2.0.0

        Returns:
            Union['WebDriver', 'IME']: Self instance
        """
        warnings.warn(
            'The "deactivate_ime_engine" API is deprecated and will be removed in future versions. '
            'Use "mobile: shell" extension instead',
            DeprecationWarning,
        )

        self.execute(Command.DEACTIVATE_IME_ENGINE, {})
        return cast('WebDriver', self)

    @property
    def active_ime_engine(self) -> str:
        """Returns the activity and package of the currently active IME engine
        (e.g., 'com.android.inputmethod.latin/.LatinIME').

        Android only.

        deprecated:: 2.0.0

        Returns:
            str: The activity and package of the currently active IME engine
        """
        warnings.warn(
            'The "active_ime_engine" API is deprecated and will be removed in future versions. '
            'Use "mobile: shell" extension instead',
            DeprecationWarning,
        )

        return self.execute(Command.GET_ACTIVE_IME_ENGINE, {})['value']  # pylint: disable=unsubscriptable-object

    def _add_commands(self) -> None:
        """Add IME commands. They are not in W3C spec."""
        # noinspection PyProtectedMember,PyUnresolvedReferences
        commands = self.command_executor._commands
        commands[Command.GET_AVAILABLE_IME_ENGINES] = (
            'GET',
            '/session/$sessionId/ime/available_engines',
        )
        commands[Command.IS_IME_ACTIVE] = ('GET', '/session/$sessionId/ime/activated')
        commands[Command.ACTIVATE_IME_ENGINE] = ('POST', '/session/$sessionId/ime/activate')
        commands[Command.DEACTIVATE_IME_ENGINE] = ('POST', '/session/$sessionId/ime/deactivate')
        commands[Command.GET_ACTIVE_IME_ENGINE] = (
            'GET',
            '/session/$sessionId/ime/active_engine',
        )
