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


class LogEvents(webdriver.Remote):

    @property
    def events(self):
        """ Retrieves events information from the current session
        (Since Appium 1.16.0)

        Usage:
            events = driver.events

        Returns:
            `dict`: A dictionary of events timing information containing the following entries
                commands: (`list` of `dict`) List of dictionaries containing the following entries
                    cmd: (str) Sent command to appium server
                    startTime: (int) Received time
                    endTime: (init)Response time
        """
        return self.execute(Command.GET_EVENTS)['value']

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.GET_EVENTS] = \
            ('POST', '/session/$sessionId/appium/events')
