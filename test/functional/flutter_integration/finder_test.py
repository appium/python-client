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

from typing import TYPE_CHECKING

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.flutter_integration.flutter_finder import FlutterFinder

if TYPE_CHECKING:
    from appium.webdriver.extensions.flutter_integration.flutter_commands import FlutterCommand
    from appium.webdriver.webdriver import WebDriver

LOGIN_BUTTON_FINDER = FlutterFinder.by_text('Login')


def test_by_flutter_key(driver: 'WebDriver') -> None:
    """Test finding elements by Flutter key."""
    user_name_field_finder = FlutterFinder.by_key('username_text_field')
    user_name_field = driver.find_element(*user_name_field_finder.as_args())
    assert user_name_field.text == 'admin'

    user_name_field.clear()
    user_name_field = driver.find_element(*user_name_field_finder.as_args()).send_keys('admin123')
    assert user_name_field.text == 'admin123'


def test_by_flutter_type(driver: 'WebDriver') -> None:
    """Test finding elements by Flutter type."""
    login_button = driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TYPE, 'ElevatedButton')
    assert login_button.find_element(AppiumBy.FLUTTER_INTEGRATION_TYPE, 'Text').text == 'Login'


def test_by_flutter_text(driver: 'WebDriver') -> None:
    """Test finding elements by Flutter text."""
    login_button = driver.find_element(*LOGIN_BUTTON_FINDER.as_args())
    assert login_button.text == 'Login'

    login_button.click()
    slider = driver.find_elements(AppiumBy.FLUTTER_INTEGRATION_TEXT, 'Slider')
    assert len(slider) == 1


def test_by_flutter_text_containing(driver: 'WebDriver') -> None:
    """Test finding elements by Flutter text containing."""
    login_button = driver.find_element(*LOGIN_BUTTON_FINDER.as_args())
    login_button.click()
    vertical_swipe_label = driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TEXT_CONTAINING, 'Vertical')
    assert vertical_swipe_label.text == 'Vertical Swiping'


def test_by_flutter_semantics_label(driver: 'WebDriver', flutter_command: 'FlutterCommand') -> None:
    """Test finding elements by Flutter semantics label."""
    login_button = driver.find_element(*LOGIN_BUTTON_FINDER.as_args())
    login_button.click()
    element = flutter_command.scroll_till_visible(FlutterFinder.by_text('Lazy Loading'))
    element.click()
    message_field = driver.find_element(AppiumBy.FLUTTER_INTEGRATION_SEMANTICS_LABEL, 'message_field')
    assert message_field.text == 'Hello world'
