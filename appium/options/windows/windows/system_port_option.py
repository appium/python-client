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

SYSTEM_PORT = 'systemPort'


class SystemPortOption(SupportsCapabilities):
    @property
    def system_port(self) -> Optional[int]:
        """
        :Returns: Port number to execute Appium Windows Driver server listener on.
        """
        return self.get_capability(SYSTEM_PORT)

    @system_port.setter
    def system_port(self, value: int) -> None:
        """
        The port number to execute Appium Windows Driver server listener on,
        for example 5556. The port must not be occupied. The default starting port
        number for a new Appium Windows Driver session is 4724. If this port is
        already busy then the next free port will be automatically selected.
        """
        self.set_capability(SYSTEM_PORT, value)
