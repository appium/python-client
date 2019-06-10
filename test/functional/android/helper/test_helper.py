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

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 3


def wait_for_element(driver, locator, value, timeout=SLEEPY_TIME):
    '''
    Wait until the element located

    :param driver: Webdriver
    :param locator: Locator like WebDriver, Mobile JSON Wire Protocol (e.g. MobileBy.ACCESSIBILITY_ID)
    :param value: Query value to locator
    :param timeout: Maximum time to wait the element. If time is over, TimeoutException is thrown
    :return: Webelement
    '''
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((locator, value))
    )
