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

import copy
from typing import Any, Dict, TypeVar

from selenium.webdriver.common.options import BaseOptions

from .automation_name_option import AutomationNameOption
from .browser_name_option import BROWSER_NAME, BrowserNameOption
from .event_timings_option import EventTimingsOption
from .full_reset_option import FullResetOption
from .new_command_timeout_option import NewCommandTimeoutOption
from .no_reset_option import NoResetOption
from .print_page_source_on_find_failure_option import PrintPageSourceOnFindFailureOption

APPIUM_PREFIX = 'appium:'
T = TypeVar('T', bound='AppiumOptions')
PLATFORM_NAME = 'platformName'


class AppiumOptions(
    BaseOptions,
    BrowserNameOption,
    AutomationNameOption,
    EventTimingsOption,
    PrintPageSourceOnFindFailureOption,
    NoResetOption,
    FullResetOption,
    NewCommandTimeoutOption,
):
    _caps: Dict
    W3C_CAPABILITY_NAMES = frozenset(
        [
            'acceptInsecureCerts',
            BROWSER_NAME,
            'browserVersion',
            PLATFORM_NAME,
            'pageLoadStrategy',
            'proxy',
            'setWindowRect',
            'timeouts',
            'unhandledPromptBehavior',
        ]
    )
    _OSS_W3C_CONVERSION = {
        'acceptSslCerts': 'acceptInsecureCerts',
        'version': 'browserVersion',
        'platform': PLATFORM_NAME,
    }

    # noinspection PyMissingConstructor
    def __init__(self) -> None:
        self._caps = self.default_capabilities
        # FIXME: https://github.com/SeleniumHQ/selenium/issues/10755
        self._ignore_local_proxy = False

    def set_capability(self: T, name: str, value: Any) -> T:
        w3c_name = name if name in self.W3C_CAPABILITY_NAMES or ':' in name else f'{APPIUM_PREFIX}{name}'
        if value is None:
            if w3c_name in self._caps:
                del self._caps[w3c_name]
        else:
            self._caps[w3c_name] = value
        return self

    def get_capability(self, name: str) -> Any:
        """Fetches capability value or None if the capability is not set"""
        return self._caps[name] if name in self._caps else self._caps.get(f'{APPIUM_PREFIX}{name}')

    def load_capabilities(self: T, caps: Dict[str, Any]) -> T:
        """Sets multiple capabilities"""
        for name, value in caps.items():
            self.set_capability(name, value)
        return self

    @staticmethod
    def as_w3c(capabilities: Dict) -> Dict:
        """
        Formats given capabilities to a valid W3C session request object

        :param capabilities: Capabilities mapping
        :return: W3C session request object
        """

        def process_key(k: str) -> str:
            key = AppiumOptions._OSS_W3C_CONVERSION.get(k, k)
            if key in AppiumOptions.W3C_CAPABILITY_NAMES:
                return key
            return key if ':' in key else f'{APPIUM_PREFIX}{key}'

        processed_caps = {process_key(k): v for k, v in copy.deepcopy(capabilities).items()}
        return {'capabilities': {'firstMatch': [{}], 'alwaysMatch': processed_caps}}

    def to_w3c(self) -> Dict:
        """
        Formats the instance to a valid W3C session request object

        :return: W3C session request object
        """
        return self.as_w3c(self.to_capabilities())

    def to_capabilities(self) -> Dict:
        return copy.copy(self._caps)

    @property
    def default_capabilities(self) -> Dict:
        return {}
