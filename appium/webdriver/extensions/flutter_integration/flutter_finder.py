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

from typing import Tuple, Union

from selenium.webdriver.common.by import ByType as SeleniumByType

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.appiumby import ByType as AppiumByType


class FlutterFinder:
    def __init__(self, using: Union[SeleniumByType, AppiumByType], value: str) -> None:
        self.using = using
        self.value = value

    @staticmethod
    def by_key(value: str) -> 'FlutterFinder':
        return FlutterFinder(AppiumBy.FLUTTER_INTEGRATION_KEY, value)

    @staticmethod
    def by_text(value: str) -> 'FlutterFinder':
        return FlutterFinder(AppiumBy.FLUTTER_INTEGRATION_TEXT, value)

    @staticmethod
    def by_semantics_label(value: str) -> 'FlutterFinder':
        return FlutterFinder(AppiumBy.FLUTTER_INTEGRATION_SEMANTICS_LABEL, value)

    @staticmethod
    def by_type(value: str) -> 'FlutterFinder':
        return FlutterFinder(AppiumBy.FLUTTER_INTEGRATION_TYPE, value)

    @staticmethod
    def by_text_containing(value: str) -> 'FlutterFinder':
        return FlutterFinder(AppiumBy.FLUTTER_INTEGRATION_TEXT_CONTAINING, value)

    def to_dict(self) -> dict:
        return {'using': self.using, 'value': self.value}

    def as_args(self) -> Tuple[str, str]:
        return self.using, self.value
