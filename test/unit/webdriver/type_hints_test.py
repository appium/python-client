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

from mypy import api


def test_find_methods_accept_default_locator_strategy() -> None:
    source = """
from typing_extensions import assert_type

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement


def find_elements(driver: WebDriver) -> None:
    assert_type(driver.find_element(value='target'), WebElement)
    assert_type(driver.find_elements(value='target'), list[WebElement])
    assert_type(driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'target'), WebElement)
    assert_type(driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'target'), list[WebElement])
"""
    output, error, status = api.run(['--no-incremental', '--follow-imports=silent', '-c', source])

    assert status == 0, output + error
