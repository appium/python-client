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


class IncludeDeviceCapsToSessionInfoOption(SupportsCapabilities):
    INCLUDE_DEVICE_CAPS_TO_SESSION_INFO = "includeDeviceCapsToSessionInfo"
    include_device_caps_to_session_info = OptionsDescriptor[Optional[bool], bool](INCLUDE_DEVICE_CAPS_TO_SESSION_INFO)
    """
    Whether to include screen information as the result of Get Session Capabilities.
    It includes pixelRatio, statBarHeight and viewportRect, but
    it causes an extra API call to WDA which may increase the response time.
    Defaults to true.

    Usage
    -----
    - Get
        - `self.include_device_caps_to_session_info`
    - Set
        - `self.include_device_caps_to_session_info` = `value`
    
    Properties
    ----------
    `value`: `bool`

    Returns
    -------
    - Get
        - `Optional[bool]`
    - Set
        - `None`
    """


class ResetLocationServiceOption(SupportsCapabilities):
    RESET_LOCATION_SERVICE = "resetLocationService"
    reset_location_service = OptionsDescriptor[Optional[bool], bool](RESET_LOCATION_SERVICE)
    """
    Whether reset the location service in the session deletion on real devices.
    Defaults to false.

    Usage
    -----
    - Get
        - `self.reset_location_service`
    - Set
        - `self.reset_location_service` = `value`
    
    Parameters
    ----------
    `value`: `bool`

    Returns
    -------
    - Get
        - `Optional[bool]`
    - Set
        - `None`
    """
