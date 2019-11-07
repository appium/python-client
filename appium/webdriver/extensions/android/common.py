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

from appium.webdriver.mobilecommand import MobileCommand as Command


class Common(webdriver.Remote):

    def end_test_coverage(self, intent, path):
        """Ends the coverage collection and pull the coverage.ec file from the device.

        Android only.
        See https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/android/android-coverage.md

        Args:
            intent (str): description of operation to be performed
            path (str): path to coverage.ec file to be pulled from the device

        Returns:
            TODO
        """
        data = {
            'intent': intent,
            'path': path,
        }
        return self.execute(Command.END_TEST_COVERAGE, data)['value']

    def open_notifications(self):
        """Open notification shade in Android (API Level 18 and above)

        Returns:
            `appium.webdriver.webdriver.WebDriver`
        """
        self.execute(Command.OPEN_NOTIFICATIONS, {})
        return self

    @property
    def current_package(self):
        """Retrieves the current package running on the device.
        """
        return self.execute(Command.GET_CURRENT_PACKAGE)['value']

    def _addCommands(self):
        self.command_executor._commands[Command.GET_CURRENT_PACKAGE] = \
            ('GET', '/session/$sessionId/appium/device/current_package')
        self.command_executor._commands[Command.END_TEST_COVERAGE] = \
            ('POST', '/session/$sessionId/appium/app/end_test_coverage')
        self.command_executor._commands[Command.OPEN_NOTIFICATIONS] = \
            ('POST', '/session/$sessionId/appium/device/open_notifications')
