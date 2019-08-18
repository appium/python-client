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


import os
import unittest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from appium import webdriver

from . import desired_capabilities

# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 10


def wait_for_element(driver, locator, value, timeout=SLEEPY_TIME):
    """Wait until the element located

    Args:
        driver (`appium.webdriver.webdriver.WebDriver`): WebDriver instance
        locator (str): Locator like WebDriver, Mobile JSON Wire Protocol
            (e.g. `appium.webdriver.common.mobileby.MobileBy.ACCESSIBILITY_ID`)
        value (str): Query value to locator
        timeout (int): Maximum time to wait the element. If time is over, `TimeoutException` is thrown

    Raises:
        `selenium.common.exceptions.TimeoutException`

    Returns:
        `appium.webdriver.webelement.WebElement`: Found WebElement
    """
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((locator, value))
    )


def is_ci():
    """Returns if current execution is running on CI

    Returns:
        bool: `True` if current executions is on CI
    """
    return os.getenv('CI', 'false') == 'true'


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        img_path = os.path.join(os.getcwd(), self._testMethodName + '.png')
        self.driver.get_screenshot_as_file(img_path)
        self.driver.quit()
