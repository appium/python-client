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


class ExecuteDriver(webdriver.Remote):

    def execute_driver(self, script='', type='webdriverio', timeout=None):
        """Returns the date and time from the device.

        Args:

        Usage:
            self.driver.get_device_time()
            self.driver.get_device_time("YYYY-MM-DD")

        Return:
            [Dir[str, any]]: The result of the script
        """

        option = {'script': script, 'type': type}
        if timeout is not None:
            option['timeout'] = timeout

        return self.execute(Command.EXECUTE_DRIVER, option)['value']

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.EXECUTE_DRIVER] = \
            ('POST', '/session/$sessionId/appium/execute_driver')
