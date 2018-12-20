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


class Applications(webdriver.Remote):
    def background_app(self, seconds):
        """Puts the application in the background on the device for a certain
        duration.

        :Args:
         - seconds - the duration for the application to remain in the background
        """
        data = {
            'seconds': seconds,
        }
        self.execute(Command.BACKGROUND, data)
        return self

    def is_app_installed(self, bundle_id):
        """Checks whether the application specified by `bundle_id` is installed
        on the device.

        :Args:
         - bundle_id - the id of the application to query
        """
        data = {
            'bundleId': bundle_id,
        }
        return self.execute(Command.IS_APP_INSTALLED, data)['value']

    def install_app(self, app_path, **options):
        """Install the application found at `app_path` on the device.

        :Args:
         - app_path - the local or remote path to the application to install
         - options - the possible installation options.
         The following options are available for Android:
         `replace`: whether to reinstall/upgrade the package if it is
         already present on the device under test. True by default
         `timeout`: how much time to wait for the installation to complete.
         60000ms by default.
         `allowTestPackages`: whether to allow installation of packages marked
         as test in the manifest. False by default
         `useSdcard`: whether to use the SD card to install the app. False
         by default
         `grantPermissions`: whether to automatically grant application permissions
         on Android 6+ after the installation completes. False by default
        """
        data = {
            'appPath': app_path,
        }
        if options:
            data.update({'options': options})
        self.execute(Command.INSTALL_APP, data)
        return self

    def remove_app(self, app_id, **options):
        """Remove the specified application from the device.

        :Args:
         - app_id - the application id to be removed
         - options - the possible removal options.
         The following options are available for Android:
         `keepData`: whether to keep application data and caches after it is uninstalled.
         False by default
         `timeout`: how much time to wait for the uninstall to complete.
         20000ms by default.
        """
        data = {
            'appId': app_id,
        }
        if options:
            data.update({'options': options})
        self.execute(Command.REMOVE_APP, data)
        return self

    def launch_app(self):
        """Start on the device the application specified in the desired capabilities.
        """
        self.execute(Command.LAUNCH_APP)
        return self

    def close_app(self):
        """Stop the running application, specified in the desired capabilities, on
        the device.
        """
        self.execute(Command.CLOSE_APP)
        return self

    def terminate_app(self, app_id, **options):
        """Terminates the application if it is running.

        :Args:
         - app_id - the application id to be terminates
         - options - the possible termination options.
         The following options are available for Android:
         `timeout`: how much time to wait for the uninstall to complete.
         500ms by default.

        :return: True if the app has been successfully terminated
        """
        data = {
            'appId': app_id,
        }
        if options:
            data.update({'options': options})
        return self.execute(Command.TERMINATE_APP, data)['value']

    def activate_app(self, app_id):
        """Activates the application if it is not running
        or is running in the background.

        :Args:
         - app_id - the application id to be activated

        :return: self instance for chaining
        """
        data = {
            'appId': app_id,
        }
        self.execute(Command.ACTIVATE_APP, data)
        return self

    def query_app_state(self, app_id):
        """Queries the state of the application.

        :Args:
         - app_id - the application id to be queried

        :return: One of possible application state constants. See ApplicationState
        class for more details.
        """
        data = {
            'appId': app_id,
        }
        return self.execute(Command.QUERY_APP_STATE, data)['value']

    def app_strings(self, language=None, string_file=None):
        """Returns the application strings from the device for the specified
        language.

        :Args:
         - language - strings language code
         - string_file - the name of the string file to query
        """
        data = {}
        if language != None:
            data['language'] = language
        if string_file != None:
            data['stringFile'] = string_file
        return self.execute(Command.GET_APP_STRINGS, data)['value']

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.BACKGROUND] = \
            ('POST', '/session/$sessionId/appium/app/background')
        self.command_executor._commands[Command.IS_APP_INSTALLED] = \
            ('POST', '/session/$sessionId/appium/device/app_installed')
        self.command_executor._commands[Command.INSTALL_APP] = \
            ('POST', '/session/$sessionId/appium/device/install_app')
        self.command_executor._commands[Command.REMOVE_APP] = \
            ('POST', '/session/$sessionId/appium/device/remove_app')
        self.command_executor._commands[Command.TERMINATE_APP] = \
            ('POST', '/session/$sessionId/appium/device/terminate_app')
        self.command_executor._commands[Command.ACTIVATE_APP] = \
            ('POST', '/session/$sessionId/appium/device/activate_app')
        self.command_executor._commands[Command.QUERY_APP_STATE] = \
            ('POST', '/session/$sessionId/appium/device/app_state')
        self.command_executor._commands[Command.GET_APP_STRINGS] = \
            ('POST', '/session/$sessionId/appium/app/strings')
