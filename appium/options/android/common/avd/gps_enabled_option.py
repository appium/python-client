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

GPS_ENABLED = 'gpsEnabled'


class GpsEnabledOption(SupportsCapabilities):
    @property
    def gps_enabled(self) -> Optional[bool]:
        """
        State of the GPS service on emulator.
        """
        return self.get_capability(GPS_ENABLED)

    @gps_enabled.setter
    def gps_enabled(self, value: bool) -> None:
        """
        Set whether to enable (true) or disable (false) GPS service in the Emulator.
        Unset by default, which means to not change the current value.
        """
        self.set_capability(GPS_ENABLED, value)
