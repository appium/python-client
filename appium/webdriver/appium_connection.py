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

import uuid
from typing import TYPE_CHECKING, Any, Dict

from selenium.webdriver.remote.remote_connection import RemoteConnection

from appium.common.helper import library_version

if TYPE_CHECKING:
    from urllib.parse import ParseResult


PREFIX_HEADER = 'appium/'

_HEADER_IDEMOTENCY_KEY = 'X-Idempotency-Key'


class AppiumConnection(RemoteConnection):
    """
    A subclass of selenium.webdriver.remote.remote_connection.Remoteconnection.

    The changes are:
        - The default user agent
        - Adds 'X-Idempotency-Key' header in a new session request to avoid proceeding
          the same request multiple times in the Appium server side.
            - https://github.com/appium/appium-base-driver/pull/400
    """

    user_agent = f'{PREFIX_HEADER}{library_version()} ({RemoteConnection.user_agent})'
    extra_headers = {}

    @classmethod
    def get_remote_connection_headers(cls, parsed_url: 'ParseResult', keep_alive: bool = True) -> Dict[str, Any]:
        """Override get_remote_connection_headers in RemoteConnection to control the extra headers.
        This method will be used in sending a request method in this class.
        """

        if parsed_url.path.endswith('/session'):
            # https://github.com/appium/appium-base-driver/pull/400
            cls.extra_headers[_HEADER_IDEMOTENCY_KEY] = str(uuid.uuid4())
        elif _HEADER_IDEMOTENCY_KEY in cls.extra_headers:
            del cls.extra_headers[_HEADER_IDEMOTENCY_KEY]

        return {**super().get_remote_connection_headers(parsed_url, keep_alive=keep_alive), **cls.extra_headers}
