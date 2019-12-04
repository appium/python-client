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

from appium.common.logger import logger

from ..mobilecommand import MobileCommand as Command


class Session(webdriver.Remote):
    @property
    def session(self):
        """ Retrieves session information from the current session

        Usage:
            session = driver.session

        Returns:
            `dict`: containing information from the current session
        """
        return self.execute(Command.GET_SESSION)['value']

    @property
    def all_sessions(self):
        """ Retrieves all sessions that are open

        Usage:
            sessions = driver.all_sessions

        Returns:
            `dict`: containing all open sessions
        """
        return self.execute(Command.GET_ALL_SESSIONS)['value']

    @property
    def events(self):
        """ Retrieves events information from the current session

        Usage:
            events = driver.events

        Returns:
            `dict`:  containing events timing information from the current session
        """
        try:
            session = self.session
            return session['events']
        except Exception as e:
            logger.warning('Could not find events information in the session. Error:', e)
            return {}

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.GET_SESSION] = \
            ('GET', '/session/$sessionId')
        self.command_executor._commands[Command.GET_ALL_SESSIONS] = \
            ('GET', '/sessions')
