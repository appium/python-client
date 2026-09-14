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

SHOW_SERVER_LOGS = 'showServerLogs'


class ShowServerLogsOption(SupportsCapabilities):
    @property
    def show_server_logs(self) -> Optional[bool]:
        """
        Whether to show WDA server logs in the Appium log.
        """
        return self.get_capability(SHOW_SERVER_LOGS)

    @show_server_logs.setter
    def show_server_logs(self, value: bool) -> None:
        """
        Set it to true in order to include xcodebuild output to the Appium
        server log. false by default.
        """
        self.set_capability(SHOW_SERVER_LOGS, value)
