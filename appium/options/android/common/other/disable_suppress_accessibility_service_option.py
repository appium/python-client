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


class DisableSuppressAccessibilityServiceOption(SupportsCapabilities):
    DISABLE_SUPPRESS_ACCESSIBILITY_SERVICE = "disableSuppressAccessibilityService"
    disable_suppress_accessibility_service = OptionsDescriptor[Optional[bool], bool]
    (DISABLE_SUPPRESS_ACCESSIBILITY_SERVICE)
    """
    Being set to true tells the instrumentation process to not suppress
    accessibility services during the automated test. This might be useful
    if your automated test needs these services. false by default.

    Usage
    -----
    - Get
        - `self.disable_suppress_accessibility_service`
    - Set
        - `self.disable_suppress_accessibility_service` = `value`
    
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
