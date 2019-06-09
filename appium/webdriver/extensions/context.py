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


class Context(webdriver.Remote):
    @property
    def contexts(self):
        """Returns the contexts within the current session.

        Usage:
            driver.contexts

        Return:
            :obj:`list` of :obj:`str`: The contexts within the current session

        """
        return self.execute(Command.CONTEXTS)['value']

    @property
    def current_context(self):
        """Returns the current context of the current session.

        Usage:
            driver.current_context

        Return:
            str: The context of the current session
        """
        return self.execute(Command.GET_CURRENT_CONTEXT)['value']

    @property
    def context(self):
        """Returns the current context of the current session.

        Usage:
            driver.context

        Return:
            str: The context of the current session
        """
        return self.current_context

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.CONTEXTS] = \
            ('GET', '/session/$sessionId/contexts')
        self.command_executor._commands[Command.GET_CURRENT_CONTEXT] = \
            ('GET', '/session/$sessionId/context')
        self.command_executor._commands[Command.SWITCH_TO_CONTEXT] = \
            ('POST', '/session/$sessionId/context')
