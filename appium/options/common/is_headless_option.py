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

IS_HEADLESS = 'isHeadless'


class IsHeadlessOption(SupportsCapabilities):
    @property
    def is_headless(self) -> Optional[bool]:
        """
        Whether the driver should start emulator/simulator in headless mode.
        """
        return self.get_capability(IS_HEADLESS)

    @is_headless.setter
    def is_headless(self, value: bool) -> None:
        """
        Set emulator/simulator to start in headless mode (e.g. no UI is shown).
        It is only applied if the emulator is not running before the test starts.
        """
        self.set_capability(IS_HEADLESS, value)
