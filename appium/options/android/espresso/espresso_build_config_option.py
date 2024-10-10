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

from appium.options.common.supports_capabilities import SupportsCapabilities

ESPRESSO_BUILD_CONFIG = 'espressoBuildConfig'


class EspressoBuildConfigOption(SupportsCapabilities):
    @property
    def espresso_build_config(self) -> Optional[Union[Dict[str, Any], str]]:
        """
        Espresso build config.
        """
        value = self.get_capability(ESPRESSO_BUILD_CONFIG)
        try:
            return json.loads(value)
        except Exception:
            return value

    @espresso_build_config.setter
    def espresso_build_config(self, value: Union[Dict[str, Any], str]) -> None:
        """
        This config allows to customize several important properties of
        Espresso server. Refer to
        https://github.com/appium/appium-espresso-driver#espresso-build-config
        for more information on how to properly construct such config.
        """
        self.set_capability(ESPRESSO_BUILD_CONFIG, value if isinstance(value, str) else json.dumps(value, ensure_ascii=False))
