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

from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException
from ..mobilecommand import MobileCommand as Command


class RemoteFS(webdriver.Remote):
    def pull_file(self, path):
        """Retrieves the file at `path`. Returns the file's contents as base64.

        :Args:
         - path - the path to the file on the device
        """
        data = {
            'path': path,
        }
        return self.execute(Command.PULL_FILE, data)['value']

    def pull_folder(self, path):
        """Retrieves a folder at `path`. Returns the folder's contents zipped
        and encoded as Base64.

        :Args:
         - path - the path to the folder on the device
        """
        data = {
            'path': path,
        }
        return self.execute(Command.PULL_FOLDER, data)['value']

    def push_file(self, destination_path, base64data=None, source_path=None):
        """Puts the data from the file at `source_path`, encoded as Base64, in the file specified as `path`.

        Specify either `base64data` or `source_path`, if both specified default to `source_path`
        :param destination_path: the location on the device/simulator where the local file contents should be saved
        :param base64data: file contents, encoded as Base64, to be written to the file on the device/simulator
        :param source_path: local file path for the file to be loaded on device
        :return: WebDriver instance
        """
        if source_path is None and base64data is None:
            raise InvalidArgumentException('Must either pass base64 data or a local file path')

        if source_path is not None:
            try:
                with open(source_path, 'rb') as f:
                    data = f.read()
            except IOError:
                message = 'source_path {} could not be found. Are you sure the file exists?'.format(source_path)
                raise InvalidArgumentException(message)
            base64data = base64.b64encode(data).decode('utf-8')

        data = {
            'path': destination_path,
            'data': base64data,
        }
        self.execute(Command.PUSH_FILE, data)
        return self

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.PULL_FILE] = \
            ('POST', '/session/$sessionId/appium/device/pull_file')
        self.command_executor._commands[Command.PULL_FOLDER] = \
            ('POST', '/session/$sessionId/appium/device/pull_folder')
        self.command_executor._commands[Command.PUSH_FILE] = \
            ('POST', '/session/$sessionId/appium/device/push_file')
