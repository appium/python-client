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

NATIVE_WEB_TAP = 'nativeWebTap'


class NativeWebTapOption(SupportsCapabilities):
    @property
    def native_web_tap(self) -> Optional[bool]:
        """
        Whether to enable native taps in web view mode.
        """
        return self.get_capability(NATIVE_WEB_TAP)

    @native_web_tap.setter
    def native_web_tap(self, value: bool) -> None:
        """
        Enable native, non-javascript-based taps being in web context mode. Defaults
        to false. Warning: sometimes the preciseness of native taps could be broken,
        because there is no reliable way to map web element coordinates to native ones.
        """
        self.set_capability(NATIVE_WEB_TAP, value)
