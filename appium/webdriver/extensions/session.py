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

from typing import Any, Dict, List

from appium.common.logger import logger
from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands

from ..mobilecommand import MobileCommand as Command


class Session(CanExecuteCommands):
    @property
    def session(self) -> Dict[str, Any]:
        """Retrieves session information from the current session

        Usage:
            session = driver.session

        Returns:
            `dict`: containing information from the current session
        """
        return self.execute(Command.GET_SESSION)['value']

    @property
    def all_sessions(self) -> List[Dict[str, Any]]:
        """Retrieves all sessions that are open

        Usage:
            sessions = driver.all_sessions

        Returns:
            :obj:`list` of :obj:`dict`: containing all open sessions
        """
        return self.execute(Command.GET_ALL_SESSIONS)['value']

    @property
    def events(self) -> Dict:
        """Retrieves events information from the current session

        Usage:
            events = driver.events

        Returns:
            `dict`:  containing events timing information from the current session
        """
        try:
            session = self.session
            return session['events']
        except Exception as e:
            logger.warning('Could not find events information in the session. Error: %s', e)
            return {}

    def _add_commands(self) -> None:
        # noinspection PyProtectedMember,PyUnresolvedReferences
        commands = self.command_executor._commands
        commands[Command.GET_SESSION] = ('GET', '/session/$sessionId')
        commands[Command.GET_ALL_SESSIONS] = ('GET', '/sessions')
