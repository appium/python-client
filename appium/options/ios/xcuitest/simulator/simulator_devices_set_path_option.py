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

SIMULATOR_DEVICES_SET_PATH = 'simulatorDevicesSetPath'


class SimulatorDevicesSetPathOption(SupportsCapabilities):
    @property
    def simulator_devices_set_path(self) -> Optional[str]:
        """
        Alternative path to the simulator devices set.
        """
        return self.get_capability(SIMULATOR_DEVICES_SET_PATH)

    @simulator_devices_set_path.setter
    def simulator_devices_set_path(self, value: str) -> None:
        """
        This capability allows to set an alternative path to the simulator devices
        set in case you have multiple sets deployed on your local system. Such
        feature could be useful if you, for example, would like to save disk space
        on the main system volume.
        """
        self.set_capability(SIMULATOR_DEVICES_SET_PATH, value)
