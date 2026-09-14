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

from typing import List, Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

CHROMEDRIVER_PORTS = 'chromedriverPorts'


class ChromedriverPortsOption(SupportsCapabilities):
    @property
    def chromedriver_ports(self) -> Optional[List[int]]:
        """
        Local port numbers to use for Chromedriver communication.
        """
        return self.get_capability(CHROMEDRIVER_PORTS)

    @chromedriver_ports.setter
    def chromedriver_ports(self, value: List[int]) -> None:
        """
        Array of possible port numbers to assign for Chromedriver communication.
        If none of the port in this array is free then a server error is thrown.
        """
        self.set_capability(CHROMEDRIVER_PORTS, value)
