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


class IME(webdriver.Remote):

    @property
    def available_ime_engines(self):
        """Get the available input methods for an Android device. Package and
        activity are returned (e.g., ['com.android.inputmethod.latin/.LatinIME'])
        Android only.
        """
        return self.execute(Command.GET_AVAILABLE_IME_ENGINES, {})['value']

    def is_ime_active(self):
        """Checks whether the device has IME service active. Returns True/False.
        Android only.
        """
        return self.execute(Command.IS_IME_ACTIVE, {})['value']

    def activate_ime_engine(self, engine):
        """Activates the given IME engine on the device.
        Android only.

        :Args:
         - engine - the package and activity of the IME engine to activate (e.g.,
            'com.android.inputmethod.latin/.LatinIME')
        """
        data = {
            'engine': engine
        }
        self.execute(Command.ACTIVATE_IME_ENGINE, data)
        return self

    def deactivate_ime_engine(self):
        """Deactivates the currently active IME engine on the device.
        Android only.
        """
        self.execute(Command.DEACTIVATE_IME_ENGINE, {})
        return self

    @property
    def active_ime_engine(self):
        """Returns the activity and package of the currently active IME engine (e.g.,
        'com.android.inputmethod.latin/.LatinIME').
        Android only.
        """
        return self.execute(Command.GET_ACTIVE_IME_ENGINE, {})['value']

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.GET_AVAILABLE_IME_ENGINES] = \
            ('GET', '/session/$sessionId/ime/available_engines')
        self.command_executor._commands[Command.IS_IME_ACTIVE] = \
            ('GET', '/session/$sessionId/ime/activated')
        self.command_executor._commands[Command.ACTIVATE_IME_ENGINE] = \
            ('POST', '/session/$sessionId/ime/activate')
        self.command_executor._commands[Command.DEACTIVATE_IME_ENGINE] = \
            ('POST', '/session/$sessionId/ime/deactivate')
        self.command_executor._commands[Command.GET_ACTIVE_IME_ENGINE] = \
            ('GET', '/session/$sessionId/ime/active_engine')
