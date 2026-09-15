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

DEVICE_TYPE = 'safari:deviceType'


class DeviceTypeOption(SupportsCapabilities):
    @property
    def device_type(self) -> Optional[str]:
        """
        String representing the type of the device.
        """
        return self.get_capability(DEVICE_TYPE)

    @device_type.setter
    def device_type(self, value: str) -> None:
        """
        If the value of safari:deviceType is 'iPhone', safaridriver will only create a session
        using an iPhone device or iPhone simulator. If the value of safari:deviceType is 'iPad',
        safaridriver will only create a session using an iPad device or iPad simulator.
        Values of safari:deviceType are compared case-insensitively.
        """
        self.set_capability(DEVICE_TYPE, value)
