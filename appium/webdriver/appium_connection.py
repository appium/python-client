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
from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from selenium.webdriver.remote.client_config import ClientConfig
from selenium.webdriver.remote.remote_connection import RemoteConnection

from appium.common.helper import library_version

if TYPE_CHECKING:
    from urllib.parse import ParseResult


PREFIX_HEADER = 'appium/'


class AppiumConnection(RemoteConnection):
    _proxy_url: Optional[str]

    RemoteConnection.user_agent = f'{PREFIX_HEADER}{library_version()} ({RemoteConnection.user_agent})'

    def __init__(
        self,
        remote_server_addr: str,
        keep_alive: bool = True,
        ignore_proxy: Optional[bool] = False,
        init_args_for_pool_manager: Union[Dict[str, Any], None] = None,
        client_config: Optional[ClientConfig] = None,
    ):
        if client_config is None:
            client_config = ClientConfig(remote_server_addr=remote_server_addr)
        client_config.keep_alive = keep_alive
        if ignore_proxy is not None:
            client_config.ignore_proxy = ignore_proxy
        if init_args_for_pool_manager is not None:
            client_config.init_args_for_pool_manager = init_args_for_pool_manager

        super().__init__(client_config=client_config)

    @classmethod
    def get_remote_connection_headers(cls, parsed_url: 'ParseResult', keep_alive: bool = True) -> Dict[str, Any]:
        """Override get_remote_connection_headers in RemoteConnection"""
        headers = RemoteConnection.get_remote_connection_headers(parsed_url, keep_alive=keep_alive)
        if parsed_url.path.endswith('/session'):
            # https://github.com/appium/appium-base-driver/pull/400
            RemoteConnection.extra_headers = {'X-Idempotency-Key': str(uuid.uuid4())}
        else:
            RemoteConnection.extra_headers = {}

        return headers
