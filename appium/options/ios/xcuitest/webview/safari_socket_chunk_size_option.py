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

SAFARI_SOCKET_CHUNK_SIZE = 'safariSocketChunkSize'


class SafariSocketChunkSizeOption(SupportsCapabilities):
    @property
    def safari_socket_chunk_size(self) -> Optional[int]:
        """
        Get the size of a single remote debugger socket chunk.
        """
        return self.get_capability(SAFARI_SOCKET_CHUNK_SIZE)

    @safari_socket_chunk_size.setter
    def safari_socket_chunk_size(self, value: int) -> None:
        """
        The size, in bytes, of the data to be sent to the Web Inspector on
        iOS 11+ real devices. Some devices hang when sending large amounts of
        data to the Web Inspector, and breaking them into smaller parts can be
        helpful in those cases. Defaults to 16384 (also the maximum possible).
        """
        self.set_capability(SAFARI_SOCKET_CHUNK_SIZE, value)
