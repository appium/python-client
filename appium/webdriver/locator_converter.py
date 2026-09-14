#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Tuple

from selenium.webdriver.remote.locator_converter import LocatorConverter


class AppiumLocatorConverter(LocatorConverter):
    """A custom locator converter in Appium.

    Appium supports locators which are not defined in W3C WebDriver,
    so Appium Python client wants to keep the given locators
    to the Appium server as-is.
    """

    def convert(self, by: str, value: str) -> Tuple[str, str]:
        return (by, value)
