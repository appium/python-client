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

SAFARI_WEB_INSPECTOR_MAX_FRAME_LENGTH = 'safariWebInspectorMaxFrameLength'


class SafariWebInspectorMaxFrameLengthOption(SupportsCapabilities):
    @property
    def safari_web_inspector_max_frame_length(self) -> Optional[int]:
        """
        Maximum size in bytes of a single data frame for the Web Inspector.
        """
        return self.get_capability(SAFARI_WEB_INSPECTOR_MAX_FRAME_LENGTH)

    @safari_web_inspector_max_frame_length.setter
    def safari_web_inspector_max_frame_length(self, value: int) -> None:
        """
        The maximum size in bytes of a single data frame for the Web Inspector.
        Too high values could introduce slowness and/or memory leaks.
        Too low values could introduce possible buffer overflow exceptions.
        Defaults to 20MiB (20*1024*1024).
        """
        self.set_capability(SAFARI_WEB_INSPECTOR_MAX_FRAME_LENGTH, value)
