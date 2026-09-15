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

from datetime import timedelta
from typing import Optional, Union

from appium.options.common.supports_capabilities import SupportsCapabilities

AVD_READY_TIMEOUT = 'avdReadyTimeout'


class AvdReadyTimeoutOption(SupportsCapabilities):
    @property
    def avd_ready_timeout(self) -> Optional[timedelta]:
        """
        Timeout to wait until Android Emulator is fully booted and is ready for usage.
        """
        value = self.get_capability(AVD_READY_TIMEOUT)
        return None if value is None else timedelta(milliseconds=value)

    @avd_ready_timeout.setter
    def avd_ready_timeout(self, value: Union[timedelta, int]) -> None:
        """
        Maximum timeout to wait until Android Emulator is fully booted and is ready for usage.
        60000 ms by default
        """
        self.set_capability(AVD_READY_TIMEOUT, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)
