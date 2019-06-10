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
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from appium.webdriver.mobilecommand import MobileCommand as Command


class Activities(webdriver.Remote):
    def start_activity(self, app_package, app_activity, **opts):
        """Opens an arbitrary activity during a test. If the activity belongs to
        another application, that application is started and the activity is opened.

        This is an Android-only method.

        Args:
            app_package (str): The package containing the activity to start.
            app_activity (str): The activity to start.

        Keyword Args:
            app_wait_package (str): Begin automation after this package starts.
            app_wait_activity (str): Begin automation after this activity starts.
            intent_action (str): Intent to start.
            intent_category (str): Intent category to start.
            intent_flags (str): Flags to send to the intent.
            optional_intent_arguments (str): Optional arguments to the intent.
            dont_stop_app_on_reset (str): Should the app be stopped on reset?
        """
        data = {
            'appPackage': app_package,
            'appActivity': app_activity
        }
        arguments = {
            'app_wait_package': 'appWaitPackage',
            'app_wait_activity': 'appWaitActivity',
            'intent_action': 'intentAction',
            'intent_category': 'intentCategory',
            'intent_flags': 'intentFlags',
            'optional_intent_arguments': 'optionalIntentArguments',
            'dont_stop_app_on_reset': 'dontStopAppOnReset'
        }
        for key, value in arguments.items():
            if key in opts:
                data[value] = opts[key]
        self.execute(Command.START_ACTIVITY, data)
        return self

    @property
    def current_activity(self):
        """Retrieves the current activity running on the device.

        Returns:
            str: The current activity name running on the device
        """
        return self.execute(Command.GET_CURRENT_ACTIVITY)['value']

    def wait_activity(self, activity, timeout, interval=1):
        """Wait for an activity: block until target activity presents or time out.

        This is an Android-only method.

        Args:
            activity (str): target activity
            timeout (int): max wait time, in seconds
            interval (int): sleep interval between retries, in seconds
        """
        try:
            WebDriverWait(self, timeout, interval).until(
                lambda d: d.current_activity == activity)
            return True
        except TimeoutException:
            return False

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.GET_CURRENT_ACTIVITY] = \
            ('GET', '/session/$sessionId/appium/device/current_activity')
        self.command_executor._commands[Command.START_ACTIVITY] = \
            ('POST', '/session/$sessionId/appium/device/start_activity')
