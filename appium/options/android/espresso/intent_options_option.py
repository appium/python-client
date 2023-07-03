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

from typing import Any, Dict, Optional

from appium.options.base_options_descriptor import OptionsDescriptor
from appium.options.common.supports_capabilities import SupportsCapabilities


class IntentOptionsOption(SupportsCapabilities):
    INTENT_OPTIONS = "intentOptions"
    intent_options = OptionsDescriptor[Optional[Dict[str, Any]], Dict[str, Any]](INTENT_OPTIONS)
    """
    The mapping of custom options for the intent that is going to be passed
    to the main app activity. Check
    https://github.com/appium/appium-espresso-driver#intent-options
    for more details.

    Usage
    -----
    - Get
        - `self.intent_options`
    - Set
        - `self.intent_options` = `value`
    
    Parameters
    ----------
    `value`: `Dict[str, Any]`

    Returns
    -------
    - Get
        - `Dict[str, Any]`
    - Set
        - `None`
    """
