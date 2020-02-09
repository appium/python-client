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

import unittest

from selenium.common.exceptions import NoSuchElementException

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

from .helper.test_helper import (
    APIDEMO_PKG_NAME,
    BaseTestCase,
    is_ci,
    wait_for_element
)


class TouchActionTests(BaseTestCase):
    def test_tap(self):
        el = self.driver.find_element_by_accessibility_id('Animation')
        action = TouchAction(self.driver)
        action.tap(el).perform()
        el = wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Bouncing Balls')
        self.assertIsNotNone(el)

    def test_tap_x_y(self):
        el = self.driver.find_element_by_accessibility_id('Animation')
        action = TouchAction(self.driver)
        action.tap(el, 100, 10).perform()

        el = wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Bouncing Balls')
        self.assertIsNotNone(el)

    def test_tap_twice(self):
        el = self.driver.find_element_by_accessibility_id('Text')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        el = wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'LogTextBox')
        action.tap(el).perform()

        el = wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Add')
        action.tap(el, count=2).perform()

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        self.assertEqual('This is a test\nThis is a test\n', els[1].get_attribute("text"))

    def test_press_and_immediately_release(self):
        el = self.driver.find_element_by_accessibility_id('Animation')
        action = TouchAction(self.driver)
        action.press(el).release().perform()

        el = wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Bouncing Balls')
        self.assertIsNotNone(el)

    def test_press_and_immediately_release_x_y(self):
        el = self.driver.find_element_by_accessibility_id('Animation')
        action = TouchAction(self.driver)
        action.press(el, 100, 10).release().perform()

        el = wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Bouncing Balls')
        self.assertIsNotNone(el)

    def test_press_and_wait(self):
        self._move_to_custom_adapter()
        action = TouchAction(self.driver)

        el = wait_for_element(self.driver, MobileBy.ANDROID_UIAUTOMATOR,
                              'new UiSelector().text("People Names")')
        action.press(el).wait(2000).perform()

        # 'Sample menu' only comes up with a long press, not a press
        el = wait_for_element(self.driver, MobileBy.ANDROID_UIAUTOMATOR,
                              'new UiSelector().text("Sample menu")')
        self.assertIsNotNone(el)

    def test_press_and_moveto(self):
        el1 = self.driver.find_element_by_accessibility_id('Content')
        el2 = self.driver.find_element_by_accessibility_id('Animation')

        action = TouchAction(self.driver)
        action.press(el1).move_to(el2).release().perform()

        el = wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Views')
        self.assertIsNotNone(el)

    def test_press_and_moveto_x_y(self):
        el1 = self.driver.find_element_by_accessibility_id('Content')
        el2 = self.driver.find_element_by_accessibility_id('App')

        action = TouchAction(self.driver)
        action.press(el1).move_to(el2, 100, 100).release().perform()

        el = wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Views')
        self.assertIsNotNone(el)

    def test_long_press(self):
        self._move_to_custom_adapter()
        action = TouchAction(self.driver)

        el = wait_for_element(self.driver, MobileBy.ANDROID_UIAUTOMATOR,
                              'new UiSelector().text("People Names")')
        action.long_press(el).perform()

        # 'Sample menu' only comes up with a long press, not a tap
        el = wait_for_element(self.driver, MobileBy.ANDROID_UIAUTOMATOR,
                              'new UiSelector().text("Sample menu")')
        self.assertIsNotNone(el)

    def test_long_press_x_y(self):
        if is_ci():
            self.skipTest("Skip since this check is low robust due to hard-coded position.")
        self._move_to_custom_adapter()
        action = TouchAction(self.driver)

        # the element "People Names" is located at 430:310 (top left corner)
        # location can be changed by phone resolusion, OS version
        action.long_press(x=430, y=310).perform()

        # 'Sample menu' only comes up with a long press, not a tap
        el = wait_for_element(self.driver, MobileBy.ANDROID_UIAUTOMATOR,
                              'new UiSelector().text("Sample menu")')
        self.assertIsNotNone(el)

    def test_drag_and_drop(self):
        self._move_to_views()
        action = TouchAction(self.driver)

        el = wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Drag and Drop')
        action.tap(el).perform()

        dd3 = wait_for_element(self.driver, MobileBy.ID, '{}:id/drag_dot_3'.format(APIDEMO_PKG_NAME))
        dd2 = self.driver.find_element_by_id('{}:id/drag_dot_2'.format(APIDEMO_PKG_NAME))

        # dnd is stimulated by longpress-move_to-release
        action.long_press(dd3).move_to(dd2).release().perform()

        el = wait_for_element(self.driver, MobileBy.ID, '{}:id/drag_result_text'.format(APIDEMO_PKG_NAME))
        self.assertTrue('Dropped!' in el.text)

    def test_driver_drag_and_drop(self):
        self._move_to_views()
        action = TouchAction(self.driver)

        el = wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Drag and Drop')
        action.tap(el).perform()

        dd3 = wait_for_element(self.driver, MobileBy.ID, '{}:id/drag_dot_3'.format(APIDEMO_PKG_NAME))
        dd2 = self.driver.find_element_by_id('{}:id/drag_dot_2'.format(APIDEMO_PKG_NAME))

        self.driver.drag_and_drop(dd3, dd2)

        el = wait_for_element(self.driver, MobileBy.ID, '{}:id/drag_result_text'.format(APIDEMO_PKG_NAME))
        self.assertTrue('Dropped!' in el.text)

    def test_driver_swipe(self):
        el = self.driver.find_element_by_accessibility_id('Views')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Animation')
        self.assertRaises(NoSuchElementException, self.driver.find_element_by_accessibility_id, 'ImageView')

        self.driver.swipe(100, 1000, 100, 100, 800)
        el = wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'ImageView')
        self.assertIsNotNone(el)

    def _move_to_views(self):
        el1 = self.driver.find_element_by_accessibility_id('Content')
        el2 = self.driver.find_element_by_accessibility_id('Animation')
        self.driver.scroll(el1, el2)

        el = wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Views')
        action = TouchAction(self.driver)
        action.tap(el).perform()

    def _move_to_custom_adapter(self):
        self._move_to_views()
        action = TouchAction(self.driver)

        el = wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, 'Expandable Lists')
        action.tap(el).perform()

        el = wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, '1. Custom Adapter')
        action.tap(el).perform()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TouchActionTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
