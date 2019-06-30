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


# The Selenium team implemented a version of the Touch Action API in their code
# (https://code.google.com/p/selenium/source/browse/py/selenium/webdriver/common/touch_actions.py)
# but it is deficient in many ways, and does not work in such a way as to be
# amenable to Appium's use of iOS UIAutomation and Android UIAutomator
# So it is reimplemented here.
#
# Theirs is `TouchActions`. Appium's is `TouchAction`.

# pylint: disable=no-self-use

import copy

from appium.webdriver.mobilecommand import MobileCommand as Command


class TouchAction(object):
    def __init__(self, driver=None):
        self._driver = driver
        self._actions = []

    def tap(self, element=None, x=None, y=None, count=1):
        """Perform a tap action on the element

        Args:
            element (`appium.webdriver.webelement.WebElement`): the element to tap
            x (:obj:`int`, optional): x coordinate to tap, relative to the top left corner of the element.
            y (:obj:`int`, optional): y coordinate. If y is used, x must also be set, and vice versa

        Returns:
            `TouchAction`: self instance
        """
        opts = self._get_opts(element, x, y)
        opts['count'] = count
        self._add_action('tap', opts)

        return self

    def press(self, el=None, x=None, y=None, pressure=None):
        """Begin a chain with a press down action at a particular element or point

        Args:
            el (:obj:`appium.webdriver.webelement.WebElement`, optional): the element to press
            x (:obj:`int`, optional): x coordiate to press. If y is used, x must also be set
            y (:obj:`int`, optional): y coordiate to press. If x is used, y must also be set
            pressure (:obj:`float`, optional): [iOS Only] press as force touch. Read the description of `force` property on Apple's UITouch class
                                (https://developer.apple.com/documentation/uikit/uitouch?language=objc) for more details on possible value ranges.

        Returns:
            `TouchAction`: self instance
        """
        self._add_action('press', self._get_opts(el, x, y, pressure=pressure))

        return self

    def long_press(self, el=None, x=None, y=None, duration=1000):
        """Begin a chain with a press down that lasts `duration` milliseconds

        Args:
            el (:obj:`appium.webdriver.webelement.WebElement`, optional): the element to press
            x (:obj:`int`, optional): x coordiate to press. If y is used, x must also be set
            y (:obj:`int`, optional): y coordiate to press. If x is used, y must also be set
            duration (:obj:`int`, optional): Duration to press

        Returns:
            `TouchAction`: self instance
        """
        self._add_action('longPress', self._get_opts(el, x, y, duration))

        return self

    def wait(self, ms=0):
        """Pause for `ms` milliseconds.

        Args:
            ms (int): The time to pause

        Returns:
            `TouchAction`: self instance
        """
        if ms is None:
            ms = 0

        opts = {'ms': ms}

        self._add_action('wait', opts)

        return self

    def move_to(self, el=None, x=None, y=None):
        """Move the pointer from the previous point to the element or point specified

        Args:
            el (:obj:`appium.webdriver.webelement.WebElement`, optional): the element to be moved to
            x (:obj:`int`, optional): x coordiate to be moved to. If y is used, x must also be set
            y (:obj:`int`, optional): y coordiate to be moved to. If x is used, y must also be set

        Returns:
            `TouchAction`: self instance
        """
        self._add_action('moveTo', self._get_opts(el, x, y))

        return self

    def release(self):
        """End the action by lifting the pointer off the screen

        Returns:
            `TouchAction`: self instance
        """
        self._add_action('release', {})

        return self

    def perform(self):
        """Perform the action by sending the commands to the server to be operated upon

        Returns:
            `TouchAction`: self instance
        """
        params = {'actions': self._actions}
        self._driver.execute(Command.TOUCH_ACTION, params)

        # get rid of actions so the object can be reused
        self._actions = []

        return self

    @property
    def json_wire_gestures(self):
        gestures = []
        for action in self._actions:
            gestures.append(copy.deepcopy(action))
        return gestures

    def _add_action(self, action, options):
        gesture = {
            'action': action,
            'options': options,
        }
        self._actions.append(gesture)

    def _get_opts(self, element, x, y, duration=None, pressure=None):
        opts = {}
        if element is not None:
            opts['element'] = element.id

        # it makes no sense to have x but no y, or vice versa.
        if x is not None and y is not None:
            opts['x'] = x
            opts['y'] = y

        if duration is not None:
            opts['duration'] = duration

        if pressure is not None:
            opts['pressure'] = pressure

        return opts
