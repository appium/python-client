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

import json
from typing import Any, Dict, Optional, Union

from appium.options.base_options_descriptor import OptionsDescriptor
from appium.options.common.supports_capabilities import SupportsCapabilities


class EspressoBuildConfigOption(SupportsCapabilities):
    ESPRESSO_BUILD_CONFIG = "espressoBuildConfig"

    @staticmethod
    def transform_get(value: Any) -> Any:
        try:
            return json.loads(value)
        except Exception:
            return value

    @staticmethod
    def transform_set(value: Union[str, Any]) -> str:
        return value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)

    espresso_build_config = OptionsDescriptor[Optional[Union[Dict[str, Any], str]], Union[Dict[str, Any], str]]
    (ESPRESSO_BUILD_CONFIG, transform_get, transform_set)
    """
    This config allows to customize several important properties of
    Espresso server. Refer to
    https://github.com/appium/appium-espresso-driver#espresso-build-config
    for more information on how to properly construct such config.

    Usage
    -----
    - Get
        - `self.espresso_build_config`
    - Set
        - `self.espresso_build_config` = `value`
    
    Parameters
    ----------
    `value`: `Union[Dict[str, Any], str]`

    Returns
    -------
    - Get
        - `Optional[Union[Dict[str, Any], str]]`
    - Set
        - `None`
    """
