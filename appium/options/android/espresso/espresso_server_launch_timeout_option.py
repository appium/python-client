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

from appium.options.base_options_descriptor import OptionsDescriptor
from appium.options.common.supports_capabilities import SupportsCapabilities
from appium.options.transformers import transform_duration_get, transform_duration_set


class EspressoServerLaunchTimeoutOption(SupportsCapabilities):
    ESPRESSO_SERVER_LAUNCH_TIMEOUT = "espressoServerLaunchTimeout"
    espresso_server_launch_timeout = OptionsDescriptor[Optional[timedelta], Union[timedelta, int]]
    (ESPRESSO_SERVER_LAUNCH_TIMEOUT, transform_duration_get, transform_duration_set)
    """Gets and Sets the maximum timeout to wait util Espresso  is listening on the device.
    45000 ms by default

    Usage
    -----
    - Get
        - `self.espresso_server_launch_timeout`
    - Set
        - `self.espresso_server_launch_timeout` = `value`

    Parameters
    ----------
    `value`: `Union[timedelta, int]`

    Returns
    -------
    - Get
        - `Optional[timedelta]`
    - Set
        - `None`
    """
