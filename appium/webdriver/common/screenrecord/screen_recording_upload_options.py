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

from webdriver.common.screenrecord.utils import attributes_to_dict


class ScreenRecordingUploadOptions(object):

    def __init__(self):
        self._remotePath = None
        self._user = None
        self._pass = None
        self._method = None

    def with_remote_path(self, remote_path):
        """
        The path to a remote location, where the resulting video should be uploaded.

        :param remote_path: The path to a writable remote location.
        :return: self instance for chaining.
        """
        self._remotePath = remote_path
        return self

    def with_auth_credentials(self, user, password):
        """
        Sets the credentials for remote ftp/http authentication (if needed).
        This option only has an effect if remotePath is provided.

        :param user: The name of the user for the remote authentication.
        :param password: The password for the remote authentication.
        :return: self instance for chaining.
        """
        self._user = user
        self._pass = password
        return self

    def with_http_method(self, method):
        """
        Sets the method name for http(s) upload. PUT is used by default.
        This option only has an effect if remotePath is provided.

        :param method:The HTTP method name ('PUT'/'POST').
        :return: self instance for chaining.
        """
        self._method = method
        return self

    def build(self):
        return attributes_to_dict(self, ('_remotePath', '_user', '_pass', '_method'))
