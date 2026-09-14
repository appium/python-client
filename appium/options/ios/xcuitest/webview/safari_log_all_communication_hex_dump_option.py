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

SAFARI_LOG_ALL_COMMUNICATION_HEX_DUMP = 'safariLogAllCommunicationHexDump'


class SafariLogAllCommunicationHexDumpOption(SupportsCapabilities):
    @property
    def safari_log_all_communication_hex_dump(self) -> Optional[bool]:
        """
        Whether to log of plists sent to and received from the Web Inspector
        in hex dump format.
        """
        return self.get_capability(SAFARI_LOG_ALL_COMMUNICATION_HEX_DUMP)

    @safari_log_all_communication_hex_dump.setter
    def safari_log_all_communication_hex_dump(self, value: bool) -> None:
        """
        Log all communication sent to and received from the Web Inspector, as raw
        hex dump and printable characters. This logging is done before any data
        manipulation, and so can elucidate some communication issues. Like
        appium:safariLogAllCommunication, this can produce a lot of data in some cases,
        so it is recommended to be used only when necessary. Defaults to false.
        """
        self.set_capability(SAFARI_LOG_ALL_COMMUNICATION_HEX_DUMP, value)
