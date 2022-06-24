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

INCLUDE_DEVICE_CAPS_TO_SESSION_INFO = 'includeDeviceCapsToSessionInfo'


class IncludeDeviceCapsToSessionInfoOption(SupportsCapabilities):
    @property
    def include_device_caps_to_session_info(self) -> Optional[bool]:
        """
        Whether to include screen information as the result of Get Session Capabilities.
        """
        return self.get_capability(INCLUDE_DEVICE_CAPS_TO_SESSION_INFO)

    @include_device_caps_to_session_info.setter
    def include_device_caps_to_session_info(self, value: bool) -> None:
        """
        Whether to include screen information as the result of Get Session Capabilities.
        It includes pixelRatio, statBarHeight and viewportRect, but
        it causes an extra API call to WDA which may increase the response time.
        Defaults to true.
        """
        self.set_capability(INCLUDE_DEVICE_CAPS_TO_SESSION_INFO, value)
