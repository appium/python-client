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

from appium.options.base_options_descriptor import OptionsDescriptor
from appium.options.common.supports_capabilities import SupportsCapabilities


class MjpegServerPortOption(SupportsCapabilities):
    MJPEG_SERVER_PORT = "mjpegServerPort"
    mjpeg_server_port = OptionsDescriptor[Optional[int], int](MJPEG_SERVER_PORT)
    """
    Gets and Sets The number of the port UiAutomator2 server starts the MJPEG server on.
    If not provided then the screenshots broadcasting service on the remote
    device does not get exposed to a local port (e.g. no adb port forwarding
    is happening).

    Usage
    -----
    - Get
        - `self.mjpeg_server_port`
    - Set
        - `self.mjpeg_server_port` = `value`
    
    Parameters
    ----------
    `value`: `int`

    Returns
    -------
    - Get
        - `Optional[int]`
    - Set
        - `None`
    """
