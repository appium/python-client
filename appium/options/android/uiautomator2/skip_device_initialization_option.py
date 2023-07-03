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


class SkipDeviceInitializationOption(SupportsCapabilities):
    SKIP_DEVICE_INITIALIZATION = "skipDeviceInitialization"
    skip_device_initialization = OptionsDescriptor[Optional[bool], bool](SKIP_DEVICE_INITIALIZATION)
    """
    Gets and Sets if the device  is ready and whether
    Settings app is installed will be canceled on session creation.
    Could speed up the session creation if you know what you are doing. false by default

    Usage
    -----
    - Get
        - `self.skip_device_initialization`
    - Set
        - `self.skip_device_initialization` = `value`

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
