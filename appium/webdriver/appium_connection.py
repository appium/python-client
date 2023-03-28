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
from typing import TYPE_CHECKING, Any, Dict, Union, Optional

import urllib3
from selenium.webdriver.remote.remote_connection import RemoteConnection

from appium.common.helper import library_version

if TYPE_CHECKING:
    from urllib.parse import ParseResult


class AppiumConnection(RemoteConnection):
    def __init__(self, remote_server_addr, keep_alive=False, ignore_proxy: Optional[bool] = False):
        self._pool_manager_init_args = {}

        super().__init__(remote_server_addr, keep_alive=keep_alive, ignore_proxy=ignore_proxy)

    def set_init_args_for_pool_manager(self, **kwargs):
        """Set keyword arguments for the pool manager.

        Appium Python client manages http requests with urllib3.PoolManager or urllib3.ProxyManager.
        This method allows to set keyword arguments for the pool manager.

        For example, "urllib3.util.retry.Retry" provides flexible retry strategy for http requests.
        """
        self._pool_manager_init_args = {'timeout': self._timeout}
        # pylint: disable=E1101
        if self._ca_certs:
            self._pool_manager_init_args['cert_reqs'] = 'CERT_REQUIRED'
            self._pool_manager_init_args['ca_certs'] = self._ca_certs
        else:
            # This line is necessary to disable certificate verification
            self._pool_manager_init_args['cert_reqs'] = 'CERT_NONE'

        self._pool_manager_init_args.update(**kwargs)

    def _get_connection_manager(self) -> Union[urllib3.PoolManager, urllib3.ProxyManager]:
        # https://github.com/SeleniumHQ/selenium/blob/0e0194b0e52a34e7df4b841f1ed74506beea5c3e/py/selenium/webdriver/remote/remote_connection.py#L134
        return (
            urllib3.PoolManager(**self._pool_manager_init_args)
            if self._proxy_url is None
            else urllib3.ProxyManager(self._proxy_url, **self._pool_manager_init_args)
        )

    @classmethod
    def get_remote_connection_headers(cls, parsed_url: 'ParseResult', keep_alive: bool = True) -> Dict[str, Any]:
        """Override get_remote_connection_headers in RemoteConnection"""
        headers = RemoteConnection.get_remote_connection_headers(parsed_url, keep_alive=keep_alive)
        headers['User-Agent'] = f'appium/python {library_version()} ({headers["User-Agent"]})'
        if parsed_url.path.endswith('/session'):
            # https://github.com/appium/appium-base-driver/pull/400
            headers['X-Idempotency-Key'] = str(uuid.uuid4())

        return headers
