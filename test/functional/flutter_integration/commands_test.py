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
from typing import TYPE_CHECKING

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.flutter_integration.flutter_finder import FlutterFinder
from appium.webdriver.extensions.flutter_integration.scroll_directions import ScrollDirection

if TYPE_CHECKING:
    from appium.webdriver.extensions.flutter_integration.flutter_commands import FlutterCommand
    from appium.webdriver.webdriver import WebDriver


def _open_screen(driver: 'WebDriver', flutter_command: 'FlutterCommand', screen_name: str) -> None:
    """Helper function to open a specific screen in the Flutter app."""
    driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TEXT, 'Login').click()
    element = flutter_command.scroll_till_visible(FlutterFinder.by_text(screen_name))
    element.click()


def test_wait_command(driver: 'WebDriver', flutter_command: 'FlutterCommand') -> None:
    """Test Flutter wait commands for element visibility."""
    _open_screen(driver, flutter_command, 'Lazy Loading')

    message_field_finder = FlutterFinder.by_key('message_field')
    toggle_button_finder = FlutterFinder.by_key('toggle_button')

    message_field = driver.find_element(*message_field_finder.as_args())
    toggle_button = driver.find_element(*toggle_button_finder.as_args())
    assert message_field.is_displayed() == True
    assert message_field.text == 'Hello world'

    toggle_button.click()
    flutter_command.wait_for_invisible(message_field_finder)
    assert len(driver.find_elements(*message_field_finder.as_args())) == 0

    toggle_button.click()
    flutter_command.wait_for_visible(message_field)
    assert len(driver.find_elements(*message_field_finder.as_args())) == 1


def test_scroll_till_visible_command(driver: 'WebDriver', flutter_command: 'FlutterCommand') -> None:
    """Test Flutter scroll till visible command."""
    _open_screen(driver, flutter_command, 'Vertical Swiping')

    java_text_finder = FlutterFinder.by_text('Java')
    protractor_text_finder = FlutterFinder.by_text('Protractor')

    first_element = flutter_command.scroll_till_visible(java_text_finder)
    assert first_element.get_attribute('displayed') == 'true'

    second_element = flutter_command.scroll_till_visible(protractor_text_finder)
    assert second_element.get_attribute('displayed') == 'true'
    assert first_element.get_attribute('displayed') == 'false'

    first_element = flutter_command.scroll_till_visible(java_text_finder, ScrollDirection.UP)
    assert second_element.get_attribute('displayed') == 'false'
    assert first_element.get_attribute('displayed') == 'true'


def test_scroll_till_visible_with_scroll_params_command(driver: 'WebDriver', flutter_command: 'FlutterCommand') -> None:
    """Test Flutter scroll till visible command with custom scroll parameters."""
    _open_screen(driver, flutter_command, 'Vertical Swiping')

    scroll_params = {
        'scrollView': FlutterFinder.by_type('Scrollable').to_dict(),
        'delta': 30,
        'maxScrolls': 30,
        'settleBetweenScrollsTimeout': 5000,
        'dragDuration': 35,
    }
    first_element = flutter_command.scroll_till_visible(
        FlutterFinder.by_text('Playwright'), scroll_direction=ScrollDirection.DOWN, **scroll_params
    )
    assert first_element.get_attribute('displayed') == 'true'


def test_double_click_command(driver: 'WebDriver', flutter_command: 'FlutterCommand') -> None:
    """Test Flutter double click command."""
    _open_screen(driver, flutter_command, 'Double Tap')

    double_tap_button = driver.find_element(AppiumBy.FLUTTER_INTEGRATION_KEY, 'double_tap_button').find_element(
        AppiumBy.FLUTTER_INTEGRATION_TEXT, 'Double Tap'
    )
    assert double_tap_button.text == 'Double Tap'

    flutter_command.perform_double_click(double_tap_button)
    assert driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TEXT_CONTAINING, 'Successful').text == 'Double Tap Successful'

    driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TEXT, 'Ok').click()
    flutter_command.perform_double_click(double_tap_button, (10, 2))
    assert driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TEXT_CONTAINING, 'Successful').text == 'Double Tap Successful'

    driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TEXT, 'Ok').click()


def test_long_press_command(driver: 'WebDriver', flutter_command: 'FlutterCommand') -> None:
    """Test Flutter long press command."""
    _open_screen(driver, flutter_command, 'Long Press')

    long_press_button = driver.find_element(AppiumBy.FLUTTER_INTEGRATION_KEY, 'long_press_button')
    flutter_command.perform_long_press(long_press_button)

    success_pop_up = driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TEXT, 'It was a long press')
    assert success_pop_up.text == 'It was a long press'
    assert success_pop_up.is_displayed() == True


def test_drag_and_drop_command(driver: 'WebDriver', flutter_command: 'FlutterCommand') -> None:
    """Test Flutter drag and drop command."""
    _open_screen(driver, flutter_command, 'Drag & Drop')

    drag_element = driver.find_element(AppiumBy.FLUTTER_INTEGRATION_KEY, 'drag_me')
    drop_element = driver.find_element(AppiumBy.FLUTTER_INTEGRATION_KEY, 'drop_zone')
    flutter_command.perform_drag_and_drop(drag_element, drop_element)
    assert driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TEXT, 'The box is dropped').is_displayed() == True


def test_camera_mocking(driver: 'WebDriver', flutter_command: 'FlutterCommand') -> None:
    """Test Flutter camera mocking functionality."""
    _open_screen(driver, flutter_command, 'Image Picker')

    success_qr_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'file', 'success_qr.png')
    second_qr_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'file', 'second_qr.png')

    image_id = flutter_command.inject_mock_image(success_qr_file_path)
    flutter_command.inject_mock_image(second_qr_file_path)
    driver.find_element(AppiumBy.FLUTTER_INTEGRATION_KEY, 'capture_image').click()
    driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TEXT, 'PICK').click()
    assert driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TEXT, 'SecondInjectedImage').is_displayed() == True

    flutter_command.activate_injected_image(image_id)
    driver.find_element(AppiumBy.FLUTTER_INTEGRATION_KEY, 'capture_image').click()
    driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TEXT, 'PICK').click()
    assert driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TEXT, 'Success!').is_displayed() == True
