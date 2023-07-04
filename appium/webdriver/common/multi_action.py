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


# The Selenium team implemented something like the Multi Action API in the form of
# "action chains" (https://code.google.com/p/selenium/source/browse/py/selenium/webdriver/common/action_chains.py).
# These do not quite work for this situation, and do not allow for ad hoc action
# chaining as the spec requires.

import copy
import warnings
from typing import TYPE_CHECKING, Dict, List, Optional, Union

from appium.webdriver.mobilecommand import MobileCommand as Command

if TYPE_CHECKING:
    from appium.webdriver.common.touch_action import TouchAction
    from appium.webdriver.webdriver import WebDriver
    from appium.webdriver.webelement import WebElement


class MultiAction:
    """
    deprecated:: 2.0.0
        Please use W3C actions instead: http://appium.io/docs/en/commands/interactions/actions/
    """

    def __init__(self, driver: 'WebDriver', element: Optional['WebElement'] = None) -> None:
        warnings.warn(
            '[Deprecated] \'MultiAction\' action is deprecated. Please use W3C actions instead.', DeprecationWarning
        )

        self._driver = driver
        self._element = element
        self._touch_actions: List['TouchAction'] = []

    def add(self, *touch_actions: 'TouchAction') -> None:
        """Add TouchAction objects to the MultiAction, to be performed later.

        Args:
            touch_actions: one or more TouchAction objects describing a chain of actions to be performed by one finger

        Usage:
            | a1 = TouchAction(driver)
            | a1.press(el1).move_to(el2).release()
            | a2 = TouchAction(driver)
            | a2.press(el2).move_to(el1).release()
            | MultiAction(driver).add(a1, a2)

        Returns:
            `MultiAction`: Self instance
        """
        for touch_action in touch_actions:
            if self._touch_actions is None:
                self._touch_actions = []

            self._touch_actions.append(copy.copy(touch_action))

    def perform(self) -> 'MultiAction':
        """Perform the actions stored in the object.

        Usage:
            | a1 = TouchAction(driver)
            | a1.press(el1).move_to(el2).release()
            | a2 = TouchAction(driver)
            | a2.press(el2).move_to(el1).release()
            | MultiAction(driver).add(a1, a2).perform()

        Returns:
            `MultiAction`: Self instance
        """
        self._driver.execute(Command.MULTI_ACTION, self.json_wire_gestures)

        # clean up and be ready for the next batch
        self._touch_actions = []

        return self

    @property
    def json_wire_gestures(self) -> Dict[str, Union[List, str]]:
        actions = []
        for action in self._touch_actions:
            actions.append(action.json_wire_gestures)
        if self._element is not None:
            return {'actions': actions, 'elementId': self._element.id}
        return {'actions': actions}
