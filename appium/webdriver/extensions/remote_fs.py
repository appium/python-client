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

import base64
from typing import Optional

from selenium.common.exceptions import InvalidArgumentException, UnknownMethodException
from typing_extensions import Self

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.protocols.webdriver.can_remember_extension_presence import CanRememberExtensionPresence

from ..mobilecommand import MobileCommand as Command


class RemoteFS(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    def pull_file(self, path: str) -> str:
        """Retrieves the file at `path`.

        Args:
            path: the path to the file on the device

        Returns:
            The file's contents encoded as Base64.
        """
        ext_name = 'mobile: pullFile'
        try:
            return self.assert_extension_exists(ext_name).execute_script(ext_name, {'remotePath': path})
        except UnknownMethodException:
            # TODO: Remove the fallback
            return self.mark_extension_absence(ext_name).execute(Command.PULL_FILE, {'path': path})['value']

    def pull_folder(self, path: str) -> str:
        """Retrieves a folder at `path`.

        Args:
            path: the path to the folder on the device

        Returns:
            The folder's contents zipped and encoded as Base64.
        """
        ext_name = 'mobile: pullFolder'
        try:
            return self.assert_extension_exists(ext_name).execute_script(ext_name, {'remotePath': path})
        except UnknownMethodException:
            # TODO: Remove the fallback
            return self.mark_extension_absence(ext_name).execute(Command.PULL_FOLDER, {'path': path})['value']

    def push_file(self, destination_path: str, base64data: Optional[str] = None, source_path: Optional[str] = None) -> Self:
        """Puts the data from the file at `source_path`, encoded as Base64, in the file specified as `path`.

        Specify either `base64data` or `source_path`, if both specified default to `source_path`

        Args:
            destination_path: the location on the device/simulator where the local file contents should be saved
            base64data: file contents, encoded as Base64, to be written
            to the file on the device/simulator
            source_path: local file path for the file to be loaded on device

        Returns:
            Union['WebDriver', 'RemoteFS']: Self instance
        """
        if source_path is None and base64data is None:
            raise InvalidArgumentException('Must either pass base64 data or a local file path')

        if source_path is not None:
            try:
                with open(source_path, 'rb') as f:
                    file_data = f.read()
            except IOError as e:
                message = f'source_path "{source_path}" could not be found. Are you sure the file exists?'
                raise InvalidArgumentException(message) from e
            base64data = base64.b64encode(file_data).decode('utf-8')

        ext_name = 'mobile: pushFile'
        try:
            self.assert_extension_exists(ext_name).execute_script(
                ext_name,
                {
                    'remotePath': destination_path,
                    'payload': base64data,
                },
            )
        except UnknownMethodException:
            # TODO: Remove the fallback
            self.mark_extension_absence(ext_name).execute(
                Command.PUSH_FILE,
                {
                    'path': destination_path,
                    'data': base64data,
                },
            )
        return self

    def _add_commands(self) -> None:
        self.command_executor.add_command(Command.PULL_FILE, 'POST', '/session/$sessionId/appium/device/pull_file')
        self.command_executor.add_command(Command.PULL_FOLDER, 'POST', '/session/$sessionId/appium/device/pull_folder')
        self.command_executor.add_command(Command.PUSH_FILE, 'POST', '/session/$sessionId/appium/device/push_file')
