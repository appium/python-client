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

ADB_EXEC_TIMEOUT = 'adbExecTimeout'


class AdbExecTimeoutOption(SupportsCapabilities):
    @property
    def adb_exec_timeout(self) -> Optional[timedelta]:
        """
        Maximum time to wait until single ADB command is executed.
        """
        value = self.get_capability(ADB_EXEC_TIMEOUT)
        return None if value is None else timedelta(milliseconds=value)

    @adb_exec_timeout.setter
    def adb_exec_timeout(self, value: Union[timedelta, int]) -> None:
        """
        Maximum time to wait until single ADB command is executed.
        20000 ms by default.
        """
        self.set_capability(
            ADB_EXEC_TIMEOUT, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value
        )
