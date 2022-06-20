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

APP_TOP_LEVEL_WINDOW = 'appTopLevelWindow'


class AppTopLevelWindowOption(SupportsCapabilities):
    @property
    def app_top_level_window(self) -> Optional[str]:
        """
        Hexadecimal handle of an existing application top level window to attach to.
        """
        return self.get_capability(APP_TOP_LEVEL_WINDOW)

    @app_top_level_window.setter
    def app_top_level_window(self, value: str) -> None:
        """
        Set the hexadecimal handle of an existing application top level
        window to attach to, for example 0x12345 (should be of string type).
        Either this capability or app one must be provided on session startup.
        """
        self.set_capability(APP_TOP_LEVEL_WINDOW, value)
