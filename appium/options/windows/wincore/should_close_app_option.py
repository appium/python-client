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

SHOULD_CLOSE_APP = 'shouldCloseApp'


class ShouldCloseAppOption(SupportsCapabilities):
    @property
    def should_close_app(self) -> bool | None:
        """
        Whether to close the application window when the session ends.
        """
        return self.get_capability(SHOULD_CLOSE_APP)

    @should_close_app.setter
    def should_close_app(self, value: bool) -> None:
        """
        Set whether to close the application window when the session ends.
        Defaults to True on the driver side; has no effect in Root sessions.
        """
        self.set_capability(SHOULD_CLOSE_APP, value)
