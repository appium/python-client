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

CLEAR_DEVICE_LOGS_ON_START = 'clearDeviceLogsOnStart'


class ClearDeviceLogsOnStartOption(SupportsCapabilities):
    @property
    def clear_device_logs_on_start(self) -> Optional[bool]:
        """
        Makes the driver to delete all the existing logs in the
        device buffer before starting a new test.
        """
        return self.get_capability(CLEAR_DEVICE_LOGS_ON_START)

    @clear_device_logs_on_start.setter
    def clear_device_logs_on_start(self, value: bool) -> None:
        """
        If set to true then the driver deletes all the existing logs in the
        device buffer before starting a new test.
        """
        self.set_capability(CLEAR_DEVICE_LOGS_ON_START, value)
