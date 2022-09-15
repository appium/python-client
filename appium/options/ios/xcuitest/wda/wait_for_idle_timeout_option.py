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

WAIT_FOR_IDLE_TIMEOUT = 'waitForIdleTimeout'


class WaitForIdleTimeoutOption(SupportsCapabilities):
    @property
    def wait_for_idle_timeout(self) -> Optional[timedelta]:
        """
        Maximum timeout to wait until WDA responds to HTTP requests.
        """
        value = self.get_capability(WAIT_FOR_IDLE_TIMEOUT)
        return None if value is None else timedelta(seconds=value)

    @wait_for_idle_timeout.setter
    def wait_for_idle_timeout(self, value: Union[timedelta, float]) -> None:
        """
        The time to wait until the application under test is idling.
        XCTest requires the app's main thread to be idling in order to execute any action on it,
        so WDA might not even start/freeze if the app under test is constantly hogging the main
        thread. The default value is 10 (seconds). Setting it to zero disables idling checks completely
        (not recommended) and has the same effect as setting waitForQuiescence to false.
        Available since Appium 1.20.0.
        """
        self.set_capability(WAIT_FOR_IDLE_TIMEOUT, value.total_seconds() if isinstance(value, timedelta) else value)
