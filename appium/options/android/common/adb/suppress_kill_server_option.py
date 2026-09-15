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

SUPPRESS_KILL_SERVER = 'suppressKillServer'


class SuppressKillServerOption(SupportsCapabilities):
    @property
    def suppress_kill_server(self) -> Optional[bool]:
        """
        Prevents the driver from ever killing the ADB server explicitly.
        """
        return self.get_capability(SUPPRESS_KILL_SERVER)

    @suppress_kill_server.setter
    def suppress_kill_server(self, value: bool) -> None:
        """
        Being set to true prevents the driver from ever killing the ADB server explicitly.
        Could be useful if ADB is connected wirelessly. false by default.
        """
        self.set_capability(SUPPRESS_KILL_SERVER, value)
