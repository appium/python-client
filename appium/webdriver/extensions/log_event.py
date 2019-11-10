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


class LogEvent(webdriver.Remote):

    @property
    def events(self):
        """ Retrieves events information from the current session
        (Since Appium 1.16.0)

        Usage:
            events = driver.events

        Returns:
            `dict`: A dictionary of events timing information containing the following entries
                commands: (`list` of `dict`) List of dictionaries containing the following entries
                    cmd: (str) The command name that has been sent to the appium server
                    startTime: (int) Received time
                    endTime: (init) Response time
        """
        return self.execute(Command.GET_EVENTS)['value']

    def log_event(self, vendor, event):
        """Log a custom event on the Appium server.
        (Since Appium 1.16.0)

        Args:
            vendor (str): The vendor to log
            event (str): The event to log

        Usage:
            driver.log_event('appium', 'funEvent')

        Returns:
            `appium.webdriver.webdriver.WebDriver`

        Note:
            The below commands

            ```
            driver.log_event('appium', 'funEvent')
            print(driver.events)
            ```

            produce the following output

            ```
            {'commands': [{'cmd': 'getWindowRect', 'startTime': 12345, 'endTime': 12346}],
             'appium:funEvent': [12347]}
            ```

        """
        data = {
            'vendor': vendor,
            'event': event
        }
        self.execute(Command.LOG_EVENT, data)
        return self

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.GET_EVENTS] = \
            ('POST', '/session/$sessionId/appium/events')
        self.command_executor._commands[Command.LOG_EVENT] = \
            ('POST', '/session/$sessionId/appium/log_event')
