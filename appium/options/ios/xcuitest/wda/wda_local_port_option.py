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

WDA_LOCAL_PORT = 'wdaLocalPort'


class WdaLocalPortOption(SupportsCapabilities):
    @property
    def wda_local_port(self) -> Optional[int]:
        """
        Local port number where the WDA traffic is being forwarded.
        """
        return self.get_capability(WDA_LOCAL_PORT)

    @wda_local_port.setter
    def wda_local_port(self, value: int) -> None:
        """
        This value, if specified, will be used to forward traffic from
        Mac host to real ios devices over USB.
        Default value is the same as the port number used by WDA on
        the device under test (8100).
        """
        self.set_capability(WDA_LOCAL_PORT, value)
