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

from typing_extensions import Self

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.protocols.webdriver.can_remember_extension_presence import CanRememberExtensionPresence


class Common(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    def open_notifications(self) -> Self:
        """Open notification shade in Android (API Level 18 and above)

        Returns:
            Union['WebDriver', 'Common']: Self instance
        """
        self.execute_script('mobile: openNotifications')
        return self

    @property
    def current_package(self) -> str:
        """Retrieves the current package running on the device."""
        return self.execute_script('mobile: getCurrentPackage')

    def _add_commands(self) -> None:
        pass
