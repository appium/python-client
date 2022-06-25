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

SIMULATOR_WINDOW_CENTER = 'simulatorWindowCenter'


class SimulatorWindowCenterOption(SupportsCapabilities):
    @property
    def simulator_window_center(self) -> Optional[str]:
        """
        Simulator window center coordinates.
        """
        return self.get_capability(SIMULATOR_WINDOW_CENTER)

    @simulator_window_center.setter
    def simulator_window_center(self, value: str) -> None:
        """
        Allows to explicitly set the coordinates of Simulator window center
        for Xcode9+ SDK. This capability only has an effect if Simulator
        window has not been opened yet for the current session before it started.
        e.g. "{-100.0,100.0}" or "{500,500}", spaces are not allowed
        """
        self.set_capability(SIMULATOR_WINDOW_CENTER, value)
