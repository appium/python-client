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
import platform

from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium import __version__

from appium.common.helper import library_version


HEADER_ACCEPT = 'application/json'
HEADER_CONTENT_TYPE = 'application/json;charset=UTF-8'


class AppiumConnection(RemoteConnection):

    @classmethod
    def get_remote_connection_headers(cls, parsed_url, keep_alive=False):
        """Override"""
        system = platform.system().lower()
        if system == "darwin":
            system = "mac"

        selenium_ua = 'selenium/{} (python {})'.format(__version__, system)

        headers = {
            'Accept': HEADER_ACCEPT,
            'Content-Type': HEADER_CONTENT_TYPE,
            'User-Agent': 'appium/python {} ({})'.format(library_version(), selenium_ua)
        }

        if parsed_url.username:
            base64string = base64.b64encode('{0.username}:{0.password}'.format(parsed_url).encode())
            headers.update({
                'Authorization': 'Basic {}'.format(base64string.decode())
            })

        if keep_alive:
            headers.update({
                'Connection': 'keep-alive'
            })

        return headers
