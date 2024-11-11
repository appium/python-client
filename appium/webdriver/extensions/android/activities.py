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

from selenium.common.exceptions import TimeoutException, UnknownMethodException
from selenium.webdriver.support.ui import WebDriverWait

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.protocols.webdriver.can_remember_extension_presence import CanRememberExtensionPresence
from appium.webdriver.mobilecommand import MobileCommand as Command


class Activities(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    @property
    def current_activity(self) -> str:
        """Retrieves the current activity running on the device.

        Returns:
            str: The current activity name running on the device
        """
        ext_name = 'mobile: getCurrentActivity'
        try:
            return self.assert_extension_exists(ext_name).execute_script(ext_name)
        except UnknownMethodException:
            # TODO: Remove the fallback
            return self.mark_extension_absence(ext_name).execute(Command.GET_CURRENT_ACTIVITY)['value']

    def wait_activity(self, activity: str, timeout: int, interval: int = 1) -> bool:
        """Wait for an activity: block until target activity presents or time out.

        This is an Android-only method.

        Args:
            activity: target activity
            timeout: max wait time, in seconds
            interval: sleep interval between retries, in seconds

        Returns:
            `True` if the target activity is shown
        """
        try:
            WebDriverWait(self, timeout, interval).until(lambda d: d.current_activity == activity)
            return True
        except TimeoutException:
            return False

    def _add_commands(self) -> None:
        self.command_executor.add_command(
            Command.GET_CURRENT_ACTIVITY,
            'GET',
            '/session/$sessionId/appium/device/current_activity',
        )
