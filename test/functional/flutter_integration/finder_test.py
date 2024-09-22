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

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.flutter_integration.flutter_finder import FlutterFinder
from test.functional.flutter_integration.helper.test_helper import BaseTestCase

LOGIN_BUTTON_FINDER = FlutterFinder.by_text("Login")


class TestFlutterFinders(BaseTestCase):

    def test_by_flutter_key(self) -> None:
        user_name_field_finder = FlutterFinder.by_key('username_text_field')
        user_name_field = self.driver.find_element(*user_name_field_finder.as_args())
        assert user_name_field.text == 'admin'

        user_name_field.clear()
        user_name_field = self.driver.find_element(*user_name_field_finder.as_args()).send_keys('admin123')
        assert user_name_field.text == 'admin123'

    def test_by_flutter_type(self) -> None:
        login_button = self.driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TYPE, 'ElevatedButton')
        assert login_button.find_element(AppiumBy.FLUTTER_INTEGRATION_TYPE, 'Text').text == 'Login'

    def test_by_flutter_text(self) -> None:
        login_button = self.driver.find_element(*LOGIN_BUTTON_FINDER.as_args())
        assert login_button.text == 'Login'

        login_button.click()
        slider = self.driver.find_elements(AppiumBy.FLUTTER_INTEGRATION_TEXT, 'Slider')
        assert len(slider) == 1

    def test_by_flutter_text_containing(self) -> None:
        login_button = self.driver.find_element(*LOGIN_BUTTON_FINDER.as_args())
        login_button.click()
        vertical_swipe_label = self.driver.find_element(AppiumBy.FLUTTER_INTEGRATION_TEXT_CONTAINING, 'Vertical')
        assert vertical_swipe_label.text == 'Vertical Swiping'

    def test_by_flutter_semantics_label(self) -> None:
        login_button = self.driver.find_element(*LOGIN_BUTTON_FINDER.as_args())
        login_button.click()
        element = self.flutter_command.scroll_till_visible(FlutterFinder.by_text('Lazy Loading'))
        element.click()
        message_field = self.driver.find_element(AppiumBy.FLUTTER_INTEGRATION_SEMANTICS_LABEL, 'message_field')
        assert message_field.text == 'Hello world'
