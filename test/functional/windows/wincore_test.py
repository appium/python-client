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
from pathlib import Path

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from test.helpers.constants import SERVER_URL_BASE


def test_find_character_map_font_selector():
    charmap = Path(os.environ['SYSTEMROOT']) / 'System32' / 'charmap.exe'
    options = AppiumOptions().load_capabilities(
        {'platformName': 'windows', 'appium:automationName': 'Wincore', 'appium:app': str(charmap)}
    )
    with webdriver.Remote(SERVER_URL_BASE, options=options) as driver:
        driver.implicitly_wait(10)
        font_selector = driver.find_element(
            AppiumBy.WINDOWS_UI_AUTOMATION, "new PropertyCondition(AutomationElement.AutomationIdProperty, '105')"
        )
        assert font_selector.get_attribute('AutomationId') == '105'
