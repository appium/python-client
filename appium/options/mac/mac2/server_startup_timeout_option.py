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

SERVER_STARTUP_TIMEOUT = 'serverStartupTimeout'


class ServerStartupTimeoutOption(SupportsCapabilities):
    @property
    def server_startup_timeout(self) -> Optional[timedelta]:
        """
        Get the timeout to wait util the WebDriverAgentMac
        project is built and started.
        """
        value_ms = self.get_capability(SERVER_STARTUP_TIMEOUT)
        return None if value_ms is None else timedelta(milliseconds=value_ms)

    @server_startup_timeout.setter
    def server_startup_timeout(self, value: Union[int, timedelta]) -> None:
        """
        Set the timeout to wait util the WebDriverAgentMac
        project is built and started.
        """
        self.set_capability(
            SERVER_STARTUP_TIMEOUT, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value
        )
