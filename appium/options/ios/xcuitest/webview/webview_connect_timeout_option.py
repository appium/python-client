# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from datetime import timedelta
from typing import Optional, Union

from appium.options.common.supports_capabilities import SupportsCapabilities

WEBVIEW_CONNECT_TIMEOUT = 'webviewConnectTimeout'


class WebviewConnectTimeoutOption(SupportsCapabilities):
    @property
    def webview_connect_timeout(self) -> Optional[timedelta]:
        """
        Timeout to wait for the initial presence of webviews.
        """
        value = self.get_capability(WEBVIEW_CONNECT_TIMEOUT)
        return None if value is None else timedelta(milliseconds=value)

    @webview_connect_timeout.setter
    def webview_connect_timeout(self, value: Union[timedelta, int]) -> None:
        """
        The time to wait for the initial presence of webviews in
        MobileSafari or hybrid apps. Defaults to 0ms.
        """
        self.set_capability(
            WEBVIEW_CONNECT_TIMEOUT, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value
        )
