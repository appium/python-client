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

from typing import Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

WEBVIEW_CONNECT_RETRIES = 'webviewConnectRetries'


class WebviewConnectRetriesOption(SupportsCapabilities):
    @property
    def webview_connect_retries(self) -> Optional[int]:
        """
        Number of retries to send connection message to remote debugger,
        to get a webview.
        """
        return self.get_capability(WEBVIEW_CONNECT_RETRIES)

    @webview_connect_retries.setter
    def webview_connect_retries(self, value: int) -> None:
        """
        Number of times to send connection message to remote debugger,
        to get a webview. Default: 8.
        """
        self.set_capability(WEBVIEW_CONNECT_RETRIES, value)
