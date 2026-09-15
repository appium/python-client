#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

from typing import Generator

import pytest

from appium.webdriver.appium_service import AppiumService


@pytest.fixture
def appium_service() -> Generator[AppiumService, None, None]:
    """Create and configure Appium service for testing."""
    service = AppiumService()
    service.start(
        args=[
            '--address',
            '127.0.0.1',
            '-p',
            '4773',
            '--base-path',
            '/wd/hub',
        ]
    )

    yield service

    service.stop()


def test_appium_service(appium_service: AppiumService) -> None:
    """Test that Appium service is running and listening."""
    assert appium_service.is_running
    assert appium_service.is_listening
