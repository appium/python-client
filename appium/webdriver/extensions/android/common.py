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

from selenium.common.exceptions import UnknownMethodException
from typing_extensions import Self

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.protocols.webdriver.can_remember_extension_presence import CanRememberExtensionPresence
from appium.webdriver.mobilecommand import MobileCommand as Command


class Common(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    def open_notifications(self) -> Self:
        """Open notification shade in Android (API Level 18 and above)

        Returns:
            Union['WebDriver', 'Common']: Self instance
        """
        ext_name = 'mobile: openNotifications'
        try:
            self.assert_extension_exists(ext_name).execute_script(ext_name)
        except UnknownMethodException:
            # TODO: Remove the fallback
            self.mark_extension_absence(ext_name).execute(Command.OPEN_NOTIFICATIONS, {})
        return self

    @property
    def current_package(self) -> str:
        """Retrieves the current package running on the device."""
        ext_name = 'mobile: getCurrentPackage'
        try:
            return self.assert_extension_exists(ext_name).execute_script(ext_name)
        except UnknownMethodException:
            # TODO: Remove the fallback
            return self.mark_extension_absence(ext_name).execute(Command.GET_CURRENT_PACKAGE)['value']

    def _add_commands(self) -> None:
        self.command_executor.add_command(
            Command.GET_CURRENT_PACKAGE,
            'GET',
            '/session/$sessionId/appium/device/current_package',
        )
        self.command_executor.add_command(
            Command.OPEN_NOTIFICATIONS,
            'POST',
            '/session/$sessionId/appium/device/open_notifications',
        )
