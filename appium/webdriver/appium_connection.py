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

import urllib3

from selenium.webdriver.remote.remote_connection import RemoteConnection

from appium.common.helper import library_version


READ_RETRIES = 3


class AppiumConnection(RemoteConnection):

    @classmethod
    def get_remote_connection_headers(cls, parsed_url, keep_alive=True):
        """Override get_remote_connection_headers in RemoteConnection"""
        headers = RemoteConnection.get_remote_connection_headers(parsed_url, keep_alive=keep_alive)
        headers['User-Agent'] = 'appium/python {} ({})'.format(library_version(), headers['User-Agent'])
        return headers

    def __init__(self, remote_server_addr, keep_alive=True, resolve_ip=True):
        super(AppiumConnection, self).__init__(remote_server_addr, keep_alive=keep_alive,
                                               resolve_ip=resolve_ip)
        # TODO: Remove this workaround after https://github.com/SeleniumHQ/selenium/pull/7746 is merged to master
        if keep_alive:
            self._conn = urllib3.PoolManager(timeout=self._timeout, retries=urllib3.Retry(read=3))
