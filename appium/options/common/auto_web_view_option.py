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

from .supports_capabilities import SupportsCapabilities

AUTO_WEB_VIEW = 'autoWebView'


class AutoWebViewOption(SupportsCapabilities):
    @property
    def auto_web_view(self) -> Optional[bool]:
        """
        Whether the driver should try to automatically switch
        to a web view context after the session is started.
        """
        return self.get_capability(AUTO_WEB_VIEW)

    @auto_web_view.setter
    def auto_web_view(self, value: bool) -> None:
        """
        Set whether the driver should try to automatically switch
        a web view context after the session is started.
        """
        self.set_capability(AUTO_WEB_VIEW, value)
