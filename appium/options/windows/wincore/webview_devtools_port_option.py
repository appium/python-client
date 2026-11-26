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

from appium.options.common.supports_capabilities import SupportsCapabilities

WEBVIEW_DEVTOOLS_PORT = 'webviewDevtoolsPort'


class WebviewDevtoolsPortOption(SupportsCapabilities):
    @property
    def webview_devtools_port(self) -> int | None:
        """
        Remote debugging port used to connect to WebView2 or browser CDP.
        """
        return self.get_capability(WEBVIEW_DEVTOOLS_PORT)

    @webview_devtools_port.setter
    def webview_devtools_port(self, value: int) -> None:
        """
        Set the remote debugging port to connect to for WebView2 or browser automation.
        """
        self.set_capability(WEBVIEW_DEVTOOLS_PORT, value)
