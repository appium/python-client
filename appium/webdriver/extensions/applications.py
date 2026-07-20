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
from typing import Any, Dict, Union

from typing_extensions import Self

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts


class Applications(CanExecuteCommands, CanExecuteScripts):
    def background_app(self, seconds: int) -> Self:
        """Puts the application in the background on the device for a certain duration.

        Args:
            seconds: the duration for the application to remain in the background.
            Providing a negative value will continue immediately after putting the app
            under test to the background.

        Returns:
            Union['WebDriver', 'Applications']: Self instance
        """
        ext_name = 'mobile: backgroundApp'
        args = {'seconds': seconds}
        self.execute_script(ext_name, args)
        return self

    def is_app_installed(self, bundle_id: str) -> bool:
        """Checks whether the application specified by `bundle_id` is installed on the device.

        Args:
            bundle_id: the id of the application to query

        Returns:
            `True` if app is installed
        """
        ext_name = 'mobile: isAppInstalled'
        return self.execute_script(
            ext_name,
            {
                'bundleId': bundle_id,
                'appId': bundle_id,
            },
        )

    def install_app(self, app_path: str, **options: Any) -> Self:
        """Install the application found at `app_path` on the device.

        Args:
            app_path: the local or remote path to the application to install

        Keyword Args:
            replace (bool): [Android only] whether to reinstall/upgrade the package if it is
                already present on the device under test. True by default
            timeout (int): [Android only] how much time to wait for the installation to complete.
                60000ms by default.
            allowTestPackages (bool): [Android only] whether to allow installation of packages marked
                as test in the manifest. False by default
            useSdcard (bool): [Android only] whether to use the SD card to install the app. False by default
            grantPermissions (bool): [Android only] whether to automatically grant application permissions
                on Android 6+ after the installation completes. False by default

        Returns:
            Union['WebDriver', 'Applications']: Self instance
        """
        ext_name = 'mobile: installApp'
        self.execute_script(
            ext_name,
            {
                'app': app_path,
                'appPath': app_path,
                **(options or {}),
            },
        )
        return self

    def remove_app(self, app_id: str, **options: Any) -> Self:
        """Remove the specified application from the device.

        Args:
            app_id: the application id to be removed

        Keyword Args:
            keepData (bool): [Android only] whether to keep application data and caches after it is uninstalled.
                False by default
            timeout (int): [Android only] how much time to wait for the uninstall to complete.
                20000ms by default.

        Returns:
            Union['WebDriver', 'Applications']: Self instance
        """
        ext_name = 'mobile: removeApp'
        self.execute_script(
            ext_name,
            {
                'appId': app_id,
                'bundleId': app_id,
                **(options or {}),
            },
        )
        return self

    def terminate_app(self, app_id: str, **options: Any) -> bool:
        """Terminates the application if it is running.

        Args:
            app_id: the application id to be terminates

        Keyword Args:
            `timeout` (int): [Android only] how much time to wait for the uninstall to complete.
                500ms by default.

        Returns:
            True if the app has been successfully terminated
        """
        ext_name = 'mobile: terminateApp'
        return self.execute_script(
            ext_name,
            {
                'appId': app_id,
                'bundleId': app_id,
                **(options or {}),
            },
        )

    def activate_app(self, app_id: str) -> Self:
        """Activates the application if it is not running
        or is running in the background.

        Args:
            app_id: the application id to be activated

        Returns:
            Union['WebDriver', 'Applications']: Self instance
        """
        ext_name = 'mobile: activateApp'
        self.execute_script(
            ext_name,
            {
                'appId': app_id,
                'bundleId': app_id,
            },
        )
        return self

    def query_app_state(self, app_id: str) -> int:
        """Queries the state of the application.

        Args:
            app_id: the application id to be queried

        Returns:
            One of possible application state constants. See ApplicationState
            class for more details.
        """
        ext_name = 'mobile: queryAppState'
        return self.execute_script(
            ext_name,
            {
                'appId': app_id,
                'bundleId': app_id,
            },
        )

    def app_strings(self, language: Union[str, None] = None, string_file: Union[str, None] = None) -> Dict[str, str]:
        """Returns the application strings from the device for the specified
        language.

        Args:
            language: strings language code
            string_file: the name of the string file to query. Only relevant for XCUITest driver

        Returns:
            The key is string id and the value is the content.
        """
        ext_name = 'mobile: getAppStrings'
        data = {}
        if language is not None:
            data['language'] = language
        if string_file is not None:
            data['stringFile'] = string_file
        return self.execute_script(ext_name, data)

    def _add_commands(self) -> None:
        pass
