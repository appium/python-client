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

from time import sleep

import pytest
from selenium.common.exceptions import NoSuchElementException

from appium.webdriver.common.mobileby import MobileBy

from ..test_helper import is_ci
from .helper.test_helper import (
    APIDEMO_PKG_NAME,
    BaseTestCase,
    wait_for_element
)


class TestCommon(BaseTestCase):

    def test_current_package(self) -> None:
        assert APIDEMO_PKG_NAME == self.driver.current_package

    @pytest.mark.skip('Not sure how to set this up to run')
    def test_end_test_coverage(self) -> None:
        self.driver.end_test_coverage(intent='android.intent.action.MAIN', path='')
        sleep(5)

    # TODO Due to unexpected dialog, "System UI isn't responding"
    @pytest.mark.skipif(condition=is_ci(), reason='Need to fix flaky test during running on CI.')
    def test_open_notifications(self) -> None:
        for word in ['App', 'Notification', 'Status Bar', ':-|']:
            wait_for_element(self.driver, MobileBy.ANDROID_UIAUTOMATOR,
                             f'new UiSelector().text("{word}")').click()

        self.driver.open_notifications()
        sleep(1)
        with pytest.raises(NoSuchElementException):
            self.driver.find_element_by_android_uiautomator, 'new UiSelector().text(":-|")'

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        # sometimes numbers shift
        title = False
        body = False
        for el in els:
            text = el.text
            if text == 'Mood ring':
                title = True
            elif text == 'I am ok':
                body = True
        assert title
        assert body

        self.driver.keyevent(4)
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text(":-|")')
