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

from typing import TYPE_CHECKING, List, Optional, Tuple, TypeVar, Union

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton

from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webelement import WebElement

if TYPE_CHECKING:
    # noinspection PyUnresolvedReferences
    from appium.webdriver.webdriver import WebDriver

T = TypeVar('T', bound=Union['WebDriver', 'ActionHelpers'])


class ActionHelpers(webdriver.Remote):
    def scroll(self: T, origin_el: WebElement, destination_el: WebElement, duration: Optional[int] = None) -> T:
        """Scrolls from one element to another

        Args:
            origin_el: the element from which to being scrolling
            destination_el: the element to scroll to
            duration: a duration after pressing originalEl and move the element to destinationEl.
                Default is 600 ms for W3C spec.

        Usage:
            driver.scroll(el1, el2)

        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """

        # XCUITest x W3C spec has no duration by default in server side
        if duration is None:
            duration = 600

        # w3c action requires seconds
        duration_sec = duration / 1000

        actions = ActionChains(self)
        dest_el_rect = destination_el.rect

        # https://github.com/SeleniumHQ/selenium/blob/3c82c868d4f2a7600223a1b3817301d0b04d28e4/py/selenium/webdriver/common/actions/pointer_actions.py#L83
        if duration_sec is None:
            actions.w3c_actions.pointer_action.move_to(origin_el)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(dest_el_rect['x'], dest_el_rect['y'])
            actions.w3c_actions.pointer_action.release()
            actions.perform()
        else:
            actions.w3c_actions.pointer_action.move_to(origin_el)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(duration_sec)
            actions.w3c_actions.pointer_action.move_to_location(dest_el_rect['x'], dest_el_rect['y'])
            actions.w3c_actions.pointer_action.release()
            actions.perform()
        return self

    def drag_and_drop(self: T, origin_el: WebElement, destination_el: WebElement) -> T:
        """Drag the origin element to the destination element

        Args:
            origin_el: the element to drag
            destination_el: the element to drag to

        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        actions = ActionChains(self)
        actions.w3c_actions.pointer_action.click_and_hold(origin_el)
        actions.w3c_actions.pointer_action.move_to(destination_el)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        return self

    def tap(self: T, positions: List[Tuple[int, int]], duration: Optional[int] = None) -> T:
        """Taps on an particular place with up to five fingers, holding for a
        certain time

        Args:
            positions: an array of tuples representing the x/y coordinates of
                the fingers to tap. Length can be up to five.
            duration: length of time to tap, in ms

        Usage:
            driver.tap([(100, 20), (100, 60), (100, 100)], 500)

        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        if len(positions) == 1:
            actions = ActionChains(self)
            x = positions[0][0]
            y = positions[0][1]
            actions.w3c_actions.pointer_action.move_to_location(x, y)
            actions.w3c_actions.pointer_action.pointer_down()
            if duration:
                actions.w3c_actions.pointer_action.pause(duration / 1000)
            else:
                actions.w3c_actions.pointer_action.pause(100)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
        else:
            finger = 0
            actions = ActionChains(self)
            actions.w3c_actions.devices = []

            for position in positions:
                finger += 1
                x = position[0]
                y = position[1]

                # https://github.com/SeleniumHQ/selenium/blob/64447d4b03f6986337d1ca8d8b6476653570bcc1/py/selenium/webdriver/common/actions/pointer_input.py#L24
                new_input = actions.w3c_actions.add_pointer_input('touch', f'finger{finger}')
                new_input.create_pointer_move(x=x, y=y)
                new_input.create_pointer_down(MouseButton.LEFT)
                if duration:
                    new_input.create_pause(duration / 1000)
                else:
                    new_input.create_pause(0.1)
                new_input.create_pointer_up(MouseButton.LEFT)
            actions.perform()

        return self

    def swipe(self: T, start_x: int, start_y: int, end_x: int, end_y: int, duration: int = 0) -> T:
        """Swipe from one point to another point, for an optional duration.

        Args:
            start_x: x-coordinate at which to start
            start_y: y-coordinate at which to start
            end_x: x-coordinate at which to stop
            end_y: y-coordinate at which to stop
            duration: time to take the swipe, in ms.

        Usage:
            driver.swipe(100, 100, 100, 400)

        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        actions = ActionChains(self)
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(duration / 1000)
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        return self

    def flick(self: T, start_x: int, start_y: int, end_x: int, end_y: int) -> T:
        """Flick from one point to another point.

        Args:
            start_x: x-coordinate at which to start
            start_y: y-coordinate at which to start
            end_x: x-coordinate at which to stop
            end_y: y-coordinate at which to stop

        Usage:
            driver.flick(100, 100, 100, 400)

        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        actions = ActionChains(self)
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        return self
