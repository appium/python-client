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

RESET_LOCATION_SERVICE = 'resetLocationService'


class ResetLocationServiceOption(SupportsCapabilities):
    @property
    def reset_location_service(self) -> Optional[bool]:
        """
        Whether to reset the location service in the session deletion on real devices.
        """
        return self.get_capability(RESET_LOCATION_SERVICE)

    @reset_location_service.setter
    def reset_location_service(self, value: bool) -> None:
        """
        Whether reset the location service in the session deletion on real devices.
        Defaults to false.
        """
        self.set_capability(RESET_LOCATION_SERVICE, value)
