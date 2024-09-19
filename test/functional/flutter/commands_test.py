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

from appium.webdriver.common.flutterby import FlutterBy
from appium.webdriver.flutter_finder import FlutterFinder
from test.functional.flutter.helper.test_helper import BaseTestCase

class TestFlutterCommands(BaseTestCase):
    
    def test_wait_command(self):
        self.__open_screen('Lazy Loading')
    
        message_field_finder = FlutterFinder.by_flutter_key('message_field')
        toggle_button_finder = FlutterFinder.by_flutter_key('toggle_button')
        
        message_field = self.driver.find_element(*message_field_finder.as_strings())
        toggle_button = self.driver.find_element(*toggle_button_finder.as_strings())
        assert message_field.is_displayed() == True
        assert message_field.text == 'Hello world'

        toggle_button.click()
        self.flutter_command.wait_for_invisible(message_field_finder)
        assert len(self.driver.find_elements(*message_field_finder.as_strings())) == 0

        toggle_button.click()
        self.flutter_command.wait_for_visible(message_field)
        assert len(self.driver.find_elements(*message_field_finder.as_strings())) == 1
     
    def test_scroll_till_visible_command(self):
        self.__open_screen('Vertical Swiping')
        
        java_text_finder = FlutterFinder.by_flutter_text("Java")
        protractor_text_finder = FlutterFinder.by_flutter_text("Protractor")
        
        first_element = self.flutter_command.scroll_till_visible(java_text_finder)
        assert first_element.get_attribute('displayed') == 'true'
        
        second_element = self.flutter_command.scroll_till_visible(protractor_text_finder)
        assert second_element.get_attribute('displayed') == 'true'
        assert first_element.get_attribute('displayed') == 'false'

        first_element = self.flutter_command.scroll_till_visible(java_text_finder, scroll_direction='up')
        assert second_element.get_attribute('displayed') == 'false'
        assert first_element.get_attribute('displayed') == 'true'
    
    def test_scroll_till_visible_with_scroll_params_command(self):
        self.__open_screen('Vertical Swiping')
        
        scroll_params = {'scrollView': FlutterFinder.by_flutter_type("Scrollable").to_dict(),
                         'delta': 30,
                         'maxScrolls': 30,
                         'settleBetweenScrollsTimeout': 5000,
                         'dragDuration': 35
                         }
        first_element = self.flutter_command.scroll_till_visible(FlutterFinder.by_flutter_text("Playwright"), **scroll_params)
        assert first_element.get_attribute('displayed') == 'true'
    
    def test_double_click_command(self):
        self.__open_screen('Double Tap')

        double_tap_button = self.driver.find_element(FlutterBy.FLUTTER_KEY, 'double_tap_button').find_element(FlutterBy.FLUTTER_TEXT, 'Double Tap')
        assert double_tap_button.text == 'Double Tap'

        self.flutter_command.perform_double_click(double_tap_button)
        assert self.driver.find_element(FlutterBy.FLUTTER_TEXT_CONTAINING, 'Successful').text == 'Double Tap Successful'
        
        self.driver.find_element(FlutterBy.FLUTTER_TEXT, 'Ok').click()
        self.flutter_command.perform_double_click(double_tap_button, (10,2))
        assert self.driver.find_element(FlutterBy.FLUTTER_TEXT_CONTAINING, 'Successful').text == 'Double Tap Successful'
        
        self.driver.find_element(FlutterBy.FLUTTER_TEXT, 'Ok').click()
    
    def test_long_press_command(self):
        self.__open_screen('Long Press')
        
        long_press_button = self.driver.find_element(FlutterBy.FLUTTER_KEY, 'long_press_button')
        self.flutter_command.perform_long_press(long_press_button)
        
        success_pop_up = self.driver.find_element(FlutterBy.FLUTTER_TEXT,'It was a long press')
        assert success_pop_up.text == 'It was a long press'
        assert success_pop_up.is_displayed() == True
    
    def test_drag_and_drop_command(self):
        self.__open_screen('Drag & Drop')

        drag_element = self.driver.find_element(FlutterBy.FLUTTER_KEY, 'drag_me')
        drop_element = self.driver.find_element(FlutterBy.FLUTTER_KEY, 'drop_zone')
        self.flutter_command.perform_drag_and_drop(drag_element, drop_element)
        assert self.driver.find_element(FlutterBy.FLUTTER_TEXT,'The box is dropped').is_displayed() == True
    
    def test_camera_mocking(self):
        self.__open_screen('Image Picker')
        
        success_qr_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'file', 'success_qr.png')
        second_qr_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'file', 'second_qr.png')
        
        image_id = self.flutter_command.inject_mock_image(success_qr_file_path)
        self.flutter_command.inject_mock_image(second_qr_file_path)
        self.driver.find_element(FlutterBy.FLUTTER_KEY, 'capture_image').click()
        self.driver.find_element(FlutterBy.FLUTTER_TEXT, 'PICK').click()
        assert self.driver.find_element(FlutterBy.FLUTTER_TEXT,'SecondInjectedImage').is_displayed() == True

        self.flutter_command.activate_injected_image(image_id)
        self.driver.find_element(FlutterBy.FLUTTER_KEY, 'capture_image').click()
        self.driver.find_element(FlutterBy.FLUTTER_TEXT, 'PICK').click()
        assert self.driver.find_element(FlutterBy.FLUTTER_TEXT,'Success!').is_displayed() == True
        
    def __open_screen(self, screen_name: str) -> None:
        self.driver.find_element(FlutterBy.FLUTTER_TEXT, 'Login').click()
        element = self.flutter_command.scroll_till_visible(FlutterFinder.by_flutter_text(screen_name))
        element.click()

