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

from typing import Dict, Any
import copy

from selenium.webdriver.common.options import BaseOptions

from .automation_name_option import AutomationNameOption
from .platform_name_option import PlatformNameOption

APPIUM_PREFIX = 'appium:'
W3C_CAPABILITY_NAMES = frozenset(
    [
        'acceptInsecureCerts',
        'browserName',
        'browserVersion',
        PlatformNameOption.PLATFORM_NAME,
        'pageLoadStrategy',
        'proxy',
        'setWindowRect',
        'timeouts',
        'unhandledPromptBehavior',
    ]
)
OSS_W3C_CONVERSION = {
    'acceptSslCerts': 'acceptInsecureCerts',
    'version': 'browserVersion',
    'platform': 'platformName'
}


class AppiumOptions(
    BaseOptions,
    AutomationNameOption,
    PlatformNameOption,
):
    _caps: Dict

    def set_capability(self, name: str, value: Any) -> 'AppiumOptions':
        """ Sets multiple capabilities """
        if value is None and name in self._caps:
            del self._caps[name]
        else:
            super().set_capability(name, value)
        return self

    def load_capabilities(self, caps: Dict[str, Any]) -> 'AppiumOptions':
        """ Sets multiple capabilities """
        for name, value in caps.items():
            self.set_capability(name, value)
        return self

    @staticmethod
    def as_w3c(capabilities: Dict) -> Dict:
        def process_key(k: str) -> str:
            key = OSS_W3C_CONVERSION.get(k, k)
            if key in W3C_CAPABILITY_NAMES:
                return key
            return key if ':' in key else f'{APPIUM_PREFIX}{key}'

        processed_caps = {process_key(k): v for k, v in copy.deepcopy(capabilities).items()}
        return {'capabilities': {'firstMatch': [{}], 'alwaysMatch': processed_caps}}

    def to_w3c(self) -> Dict:
        return self.as_w3c(self.to_capabilities())

    def to_capabilities(self) -> Dict:
        return copy.deepcopy(self._caps)

    @property
    def default_capabilities(self) -> Dict:
        return {}
