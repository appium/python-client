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

from typing import TYPE_CHECKING, Generator

import pytest

from appium import webdriver
from appium.webdriver.client_config import AppiumClientConfig
from appium.webdriver.extensions.flutter_integration.flutter_commands import FlutterCommand
from test.helpers.constants import SERVER_URL_BASE

from .helper.options import make_options

if TYPE_CHECKING:
    from appium.webdriver.webdriver import WebDriver


@pytest.fixture
def driver() -> Generator['WebDriver', None, None]:
    """Create and configure Flutter driver for testing."""
    options = make_options()

    client_config = AppiumClientConfig(remote_server_addr=SERVER_URL_BASE)
    client_config.timeout = 600

    driver = webdriver.Remote(options=options, client_config=client_config)

    yield driver

    driver.quit()


@pytest.fixture
def flutter_command(driver: 'WebDriver') -> FlutterCommand:
    """Create FlutterCommand instance for the driver."""
    return FlutterCommand(driver)
