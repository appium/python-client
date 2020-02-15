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

from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.mobileby import MobileBy
from test.functional.android.helper.test_helper import (
    BaseTestCase,
    wait_for_element
)

DEFAULT_PORT = 4723


class TestAppiumService(BaseTestCase):

    service: AppiumService

    @classmethod
    def setup_class(cls) -> None:
        cls.service = AppiumService()
        cls.service.start(args=['--address', '127.0.0.1', '-p', str(DEFAULT_PORT)])

    def test_appium_service(self) -> None:
        assert self.service.is_running
        assert self.service.is_listening
        el = wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Accessibility')
        assert el is not None

    @classmethod
    def teardown_class(cls) -> None:
        cls.service.stop()
