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

MJPEG_SERVER_PORT = 'mjpegServerPort'


class MjpegServerPortOption(SupportsCapabilities):
    @property
    def mjpeg_server_port(self) -> Optional[int]:
        """
        Port number on which WDA broadcasts screenshots stream encoded into MJPEG
        format from the device under test.
        """
        return self.get_capability(MJPEG_SERVER_PORT)

    @mjpeg_server_port.setter
    def mjpeg_server_port(self, value: int) -> None:
        """
        Port number on which WDA broadcasts screenshots stream encoded into MJPEG
        format from the device under test. It might be necessary to change this value
        if the default port is busy because of other tests running in parallel.
        Default value: 9100.
        """
        self.set_capability(MJPEG_SERVER_PORT, value)
