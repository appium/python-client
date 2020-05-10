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


import base64
import os
from typing import TYPE_CHECKING

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from appium import webdriver
from test.functional.test_helper import is_ci

from . import desired_capabilities

if TYPE_CHECKING:
    from appium.webdriver.webelement import WebElement
    from appium.webdriver.webdriver import WebDriver

# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 10

# The package name of ApiDemos-debug.apk.zip
APIDEMO_PKG_NAME = 'io.appium.android.apis'


def wait_for_element(driver: 'WebDriver', locator: str, value: str, timeout: int = SLEEPY_TIME) -> 'WebElement':
    """Wait until the element located

    Args:
        driver: WebDriver instance
        locator: Locator like WebDriver, Mobile JSON Wire Protocol
            (e.g. `appium.webdriver.common.mobileby.MobileBy.ACCESSIBILITY_ID`)
        value: Query value to locator
        timeout: Maximum time to wait the element. If time is over, `TimeoutException` is thrown

    Raises:
        `selenium.common.exceptions.TimeoutException`

    Returns:
        The found WebElement
    """
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((locator, value))
    )


class BaseTestCase():

    def setup_method(self, method) -> None:  # type: ignore
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk.zip')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        if is_ci():
            self.driver.start_recording_screen()

    def teardown_method(self, method) -> None:  # type: ignore
        if is_ci():
            payload = self.driver.stop_recording_screen()
            video_path = os.path.join(os.getcwd(), method.__name__ + '.mp4')
            with open(video_path, "wb") as fd:
                fd.write(base64.b64decode(payload))
        self.driver.quit()
