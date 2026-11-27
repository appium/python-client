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

FORCE_QUIT = 'ms:forcequit'


class ForceQuitOption(SupportsCapabilities):
    @property
    def force_quit(self) -> bool | None:
        """
        Whether to kill the application process instead of closing its window on session end.
        """
        return self.get_capability(FORCE_QUIT)

    @force_quit.setter
    def force_quit(self, value: bool) -> None:
        """
        Set whether to terminate the application process instead of closing its window
        when the application is closed at the end of the session.
        """
        self.set_capability(FORCE_QUIT, value)
