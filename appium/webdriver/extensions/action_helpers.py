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

from selenium import webdriver

from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction


class ActionHelpers(webdriver.Remote):

    def scroll(self, origin_el, destination_el, duration=None):
        """Scrolls from one element to another

        Args:
            originalEl (`appium.webdriver.webelement.WebElement`): the element from which to being scrolling
            destinationEl (`appium.webdriver.webelement.WebElement`): the element to scroll to
            duration (int): a duration after pressing originalEl and move the element to destinationEl.
                Default is 600 ms for W3C spec. Zero for MJSONWP.

        Usage:
            driver.scroll(el1, el2)

        Returns:
            `appium.webdriver.webelement.WebElement`
        """

        # XCUITest x W3C spec has no duration by default in server side
        if self.w3c and duration is None:
            duration = 600

        action = TouchAction(self)
        if duration is None:
            action.press(origin_el).move_to(destination_el).release().perform()
        else:
            action.press(origin_el).wait(duration).move_to(destination_el).release().perform()
        return self

    def drag_and_drop(self, origin_el, destination_el):
        """Drag the origin element to the destination element

        Args:
            originEl (`appium.webdriver.webelement.WebElement`): the element to drag
            destinationEl (`appium.webdriver.webelement.WebElement`): the element to drag to

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        action = TouchAction(self)
        action.long_press(origin_el).move_to(destination_el).release().perform()
        return self

    def tap(self, positions, duration=None):
        """Taps on an particular place with up to five fingers, holding for a
        certain time

        Args:
            positions (:obj:`list` of :obj:`tuple`): an array of tuples representing the x/y coordinates of
                the fingers to tap. Length can be up to five.
            duration (:obj:`int`, optional): length of time to tap, in ms

        Usage:
            driver.tap([(100, 20), (100, 60), (100, 100)], 500)

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        if len(positions) == 1:
            action = TouchAction(self)
            x = positions[0][0]
            y = positions[0][1]
            if duration:
                action.long_press(x=x, y=y, duration=duration).release()
            else:
                action.tap(x=x, y=y)
            action.perform()
        else:
            ma = MultiAction(self)
            for position in positions:
                x = position[0]
                y = position[1]
                action = TouchAction(self)
                if duration:
                    action.long_press(x=x, y=y, duration=duration).release()
                else:
                    action.press(x=x, y=y).release()
                ma.add(action)

            ma.perform()
        return self

    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        """Swipe from one point to another point, for an optional duration.

        Args:
            start_x (int): x-coordinate at which to start
            start_y (int): y-coordinate at which to start
            end_x (int): x-coordinate at which to stop
            end_y (int): y-coordinate at which to stop
            duration (:obj:`int`, optional): time to take the swipe, in ms.

        Usage:
            driver.swipe(100, 100, 100, 400)

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        # `swipe` is something like press-wait-move_to-release, which the server
        # will translate into the correct action
        action = TouchAction(self)
        action \
            .press(x=start_x, y=start_y) \
            .wait(ms=duration) \
            .move_to(x=end_x, y=end_y) \
            .release()
        action.perform()
        return self

    def flick(self, start_x, start_y, end_x, end_y):
        """Flick from one point to another point.

        Args:
            start_x (int): x-coordinate at which to start
            start_y (int): y-coordinate at which to start
            end_x (int): x-coordinate at which to stop
            end_y (int): y-coordinate at which to stop

        Usage:
            driver.flick(100, 100, 100, 400)

        Returns:
            `appium.webdriver.webelement.WebElement`
        """
        action = TouchAction(self)
        action \
            .press(x=start_x, y=start_y) \
            .move_to(x=end_x, y=end_y) \
            .release()
        action.perform()
        return self
