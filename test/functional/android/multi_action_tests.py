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
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import desired_capabilities

# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 1


class MultiActionTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_parallel_actions(self):
        el1 = self.driver.find_element_by_name('Content')
        el2 = self.driver.find_element_by_name('Animation')
        self.driver.scroll(el1, el2)

        el = self.driver.find_element_by_name('Views')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        el = self.driver.find_element_by_name('Expandable Lists')
        # simulate a swipe/scroll
        action.press(el).move_to(x=100, y=-1000).release().perform()

        el = self.driver.find_element_by_name('Splitting Touches across Views')
        action.tap(el).perform()

        els = self.driver.find_elements_by_class_name('android.widget.ListView')
        a1 = TouchAction()
        a1.press(els[0]) \
            .move_to(x=10, y=0).move_to(x=10, y=-75).move_to(x=10, y=-600).release()

        a2 = TouchAction()
        a2.press(els[1]) \
            .move_to(x=10, y=10).move_to(x=10, y=-300).move_to(x=10, y=-600).release()

        ma = MultiAction(self.driver, els[0])
        ma.add(a1, a2)
        ma.perform()

    def test_actions_with_waits(self):
        el1 = self.driver.find_element_by_name('Content')
        el2 = self.driver.find_element_by_name('Animation')
        self.driver.scroll(el1, el2)

        el = self.driver.find_element_by_name('Views')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        el = self.driver.find_element_by_name('Expandable Lists')
        # simulate a swipe/scroll
        action.press(el).move_to(x=100, y=-1000).release().perform()

        el = self.driver.find_element_by_name('Splitting Touches across Views')
        action.tap(el).perform()

        els = self.driver.find_elements_by_class_name('android.widget.ListView')
        a1 = TouchAction()
        a1.press(els[0]) \
            .move_to(x=10, y=0) \
            .move_to(x=10, y=-75) \
            .wait(1000) \
            .move_to(x=10, y=-600) \
            .release()

        a2 = TouchAction()
        a2.press(els[1]) \
            .move_to(x=10, y=10) \
            .move_to(x=10, y=-300) \
            .wait(500) \
            .move_to(x=10, y=-600) \
            .release()

        ma = MultiAction(self.driver, els[0])
        ma.add(a1, a2)
        ma.perform()

    def test_driver_multi_tap(self):
        el = self.driver.find_element_by_name('Graphics')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        self.driver.scroll(els[len(els) - 1], els[0])

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        if els[len(els) - 1].get_attribute('name') != 'Xfermodes':
            self.driver.scroll(els[len(els) - 1], els[0])

        el = self.driver.find_element_by_name('Touch Paint')
        action.tap(el).perform()

        positions = [(100, 200), (100, 400)]

        # makes two dots in the paint program
        # THE TEST MUST BE WATCHED TO CHECK IF IT WORKS
        self.driver.tap(positions)
        sleep(10)

    def test_driver_pinch(self):
        el1 = self.driver.find_element_by_name('Content')
        el2 = self.driver.find_element_by_name('Animation')
        self.driver.scroll(el1, el2)

        el = self.driver.find_element_by_name('Views')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        self.driver.scroll(els[len(els) - 1], els[0])

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        if els[len(els) - 1].get_attribute('name') != 'WebView':
            self.driver.scroll(els[len(els) - 1], els[0])

        el = self.driver.find_element_by_name('WebView')
        action.tap(el).perform()

        sleep(SLEEPY_TIME)
        el = self.driver.find_element_by_id('com.example.android.apis:id/wv1')
        self.driver.pinch(element=el)

    def test_driver_zoom(self):
        el1 = self.driver.find_element_by_name('Content')
        el2 = self.driver.find_element_by_name('Animation')
        self.driver.scroll(el1, el2)

        el = self.driver.find_element_by_name('Views')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        self.driver.scroll(els[len(els) - 1], els[0])

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        if els[len(els) - 1].get_attribute('name') != 'WebView':
            self.driver.scroll(els[len(els) - 1], els[0])

        el = self.driver.find_element_by_name('WebView')
        action.tap(el).perform()

        sleep(SLEEPY_TIME)
        el = self.driver.find_element_by_id('com.example.android.apis:id/wv1')
        self.driver.zoom(element=el)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MultiActionTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
