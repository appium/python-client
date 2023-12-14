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

from typing import TYPE_CHECKING, List, Optional, Tuple, cast

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.actions.pointer_input import PointerInput

from appium.webdriver.webelement import WebElement

if TYPE_CHECKING:
    from appium.webdriver.webdriver import WebDriver


class ActionHelpers:
    def scroll(self, origin_el: WebElement, destination_el: WebElement, duration: Optional[int] = None) -> 'WebDriver':
        """Scrolls from one element to another

        Args:
            origin_el: the element from which to begin scrolling (center of element)
            destination_el: the element to scroll to (center of element)
            duration: defines speed of scroll action when moving from originalEl to destinationEl.
                Default is 600 ms for W3C spec.

        Usage:
            driver.scroll(el1, el2)

        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        # XCUITest x W3C spec has no duration by default in server side
        if duration is None:
            duration = 600

        touch_input = PointerInput(interaction.POINTER_TOUCH, 'touch')

        actions = ActionChains(self)
        actions.w3c_actions = ActionBuilder(self, mouse=touch_input)

        # https://github.com/SeleniumHQ/selenium/blob/3c82c868d4f2a7600223a1b3817301d0b04d28e4/py/selenium/webdriver/common/actions/pointer_actions.py#L83
        actions.w3c_actions.pointer_action.move_to(origin_el)
        actions.w3c_actions.pointer_action.pointer_down()
        # setup duration for second move only, assuming duration always has atleast default value
        actions.w3c_actions = ActionBuilder(self, mouse=touch_input, duration=duration)
        actions.w3c_actions.pointer_action.move_to(destination_el)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        return cast('WebDriver', self)

    def drag_and_drop(self, origin_el: WebElement, destination_el: WebElement) -> 'WebDriver':
        """Drag the origin element to the destination element

        Args:
            origin_el: the element to drag
            destination_el: the element to drag to

        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        actions = ActionChains(self)
        # 'mouse' pointer action
        actions.w3c_actions.pointer_action.click_and_hold(origin_el)
        actions.w3c_actions.pointer_action.move_to(destination_el)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        return cast('WebDriver', self)

    def tap(self, positions: List[Tuple[int, int]], duration: Optional[int] = None) -> 'WebDriver':
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
            actions.w3c_actions = ActionBuilder(self, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
            x = positions[0][0]
            y = positions[0][1]
            actions.w3c_actions.pointer_action.move_to_location(x, y)
            actions.w3c_actions.pointer_action.pointer_down()
            if duration:
                actions.w3c_actions.pointer_action.pause(duration / 1000)
            else:
                actions.w3c_actions.pointer_action.pause(0.1)
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

                # https://github.com/SeleniumHQ/selenium/blob/trunk/py/selenium/webdriver/common/actions/pointer_input.py
                new_input = actions.w3c_actions.add_pointer_input('touch', f'finger{finger}')
                new_input.create_pointer_move(x=x, y=y)
                new_input.create_pointer_down(button=MouseButton.LEFT)
                if duration:
                    new_input.create_pause(duration / 1000)
                else:
                    new_input.create_pause(0.1)
                new_input.create_pointer_up(MouseButton.LEFT)
            actions.perform()
        return cast('WebDriver', self)

    def swipe(self, start_x: int, start_y: int, end_x: int, end_y: int, duration: int = 0) -> 'WebDriver':
        """Swipe from one point to another point, for an optional duration.

        Args:
            start_x: x-coordinate at which to start
            start_y: y-coordinate at which to start
            end_x: x-coordinate at which to stop
            end_y: y-coordinate at which to stop
            duration: defines the swipe speed as time taken to swipe from point a to point b, in ms.

        Usage:
            driver.swipe(100, 100, 100, 400)

        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        touch_input = PointerInput(interaction.POINTER_TOUCH, 'touch')

        actions = ActionChains(self)
        actions.w3c_actions = ActionBuilder(self, mouse=touch_input)
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        if duration > 0:
            actions.w3c_actions = ActionBuilder(self, mouse=touch_input, duration=duration)
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        return cast('WebDriver', self)

    def flick(self, start_x: int, start_y: int, end_x: int, end_y: int) -> 'WebDriver':
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
        actions.w3c_actions = ActionBuilder(self, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        return cast('WebDriver', self)
