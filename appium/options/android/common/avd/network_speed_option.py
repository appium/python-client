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

NETWORK_SPEED = 'networkSpeed'


class NetworkSpeedOption(SupportsCapabilities):
    @property
    def network_speed(self) -> Optional[str]:
        """
        Desired network speed limit for the emulator.
        """
        return self.get_capability(NETWORK_SPEED)

    @network_speed.setter
    def network_speed(self, value: str) -> None:
        """
        Sets the desired network speed limit for the emulator.
        It is only applied if the emulator is not running before
        the test starts. See emulator command line arguments description
        for more details.
        """
        self.set_capability(NETWORK_SPEED, value)
