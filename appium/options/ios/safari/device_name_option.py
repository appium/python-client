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

DEVICE_NAME = 'safari:deviceName'


class DeviceNameOption(SupportsCapabilities):
    @property
    def device_name(self) -> Optional[str]:
        """
        String representing the name of the device.
        """
        return self.get_capability(DEVICE_NAME)

    @device_name.setter
    def device_name(self, value: str) -> None:
        """
        safaridriver will only create a session using hosts whose device name
        matches the value of safari:deviceName. Device names are compared
        case-insensitively. NOTE: Device names for connected devices are shown in
        iTunes. If Xcode is installed, device names for connected devices are available
        via the output of instruments(1) and in the Devices and Simulators window
        (accessed in Xcode via "Window -&gt; Devices and Simulators").
        """
        self.set_capability(DEVICE_NAME, value)
