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

from .mobilecommand import MobileCommand as Command
from .errorhandler import MobileErrorHandler
from .switch_to import MobileSwitchTo

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

from selenium.webdriver.common.by import By

class WebDriver(webdriver.Remote):
    def __init__(self, command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=None, browser_profile=None, proxy=None, keep_alive=False):

        super(WebDriver, self).__init__(command_executor, desired_capabilities, browser_profile, proxy, keep_alive)

        if self.command_executor is not None:
            self._addCommands()

        self.error_handler = MobileErrorHandler()
        self._switch_to = MobileSwitchTo(self)

        # add new method to the `find_by_*` pantheon
        By.IOS_UIAUTOMATION = MobileBy.IOS_UIAUTOMATION
        By.ANDROID_UIAUTOMATOR = MobileBy.ANDROID_UIAUTOMATOR
        By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID

    @property
    def contexts(self):
        """
        Returns the contexts within the current session.

        :Usage:
            driver.contexts
        """
        return self.execute(Command.CONTEXTS)['value'];

    @property
    def current_context(self):
        """
        Returns the current context of the current session.

        :Usage:
            driver.current_context
        """
        return self.execute(Command.GET_CURRENT_CONTEXT)['value']

    def find_element_by_ios_uiautomation(self, uia_string):
        """Finds an element by uiautomation in iOS.

        :Args:
         - uia_string - The element name in the iOS UIAutomation library

        :Usage:
            driver.find_element_by_ios_uiautomation('.elements()[1].cells()[2]')
        """
        return self.find_element(by=By.IOS_UIAUTOMATION, value=uia_string)

    def find_elements_by_ios_uiautomation(self, uia_string):
        """Finds elements by uiautomation in iOS.

        :Args:
         - uia_string - The element name in the iOS UIAutomation library

        :Usage:
            driver.find_elements_by_ios_uiautomation('.elements()[1].cells()[2]')
        """
        return self.find_elements(by=By.IOS_UIAUTOMATION, value=uia_string)

    def find_element_by_android_uiautomator(self, uia_string):
        """Finds element by uiautomator in Android.

        :Args:
         - uia_string - The element name in the Android UIAutomator library

        :Usage:
            driver.find_element_by_android_uiautomator('.elements()[1].cells()[2]')
        """
        return self.find_element(by=By.ANDROID_UIAUTOMATOR, value=uia_string)

    def find_elements_by_android_uiautomator(self, uia_string):
        """Finds elements by uiautomator in Android.

        :Args:
         - uia_string - The element name in the Android UIAutomator library

        :Usage:
            driver.find_elements_by_android_uiautomator('.elements()[1].cells()[2]')
        """
        return self.find_elements(by=By.ANDROID_UIAUTOMATOR, value=uia_string)

    def find_element_by_accessibility_id(self, id):
        """Finds an element by accessibility id.

        :Args:
         - id - a string corresponding to a recursive element search using the Id/Name that the native Accessibility options utilize

        :Usage:
            driver.find_element_by_accessibility_id()
        """
        return self.find_element(by=By.ACCESSIBILITY_ID, value=id)

    def find_elements_by_accessibility_id(self, id):
        """Finds elements by accessibility id.

        :Args:
         - id - a string corresponding to a recursive element search using the Id/Name that the native Accessibility options utilize

        :Usage:
            driver.find_elements_by_accessibility_id()
        """
        return self.find_elements(by=By.ACCESSIBILITY_ID, value=id)


    # convenience method added to Appium (NOT Selenium 3)
    def scroll(self, originEl, destinationEl):
        """Scrolls from one element to another

        :Args:
         - originalEl - the element from which to being scrolling
         - destinationEl - the element to scroll to

        :Usage:
            driver.scroll(el1, el2)
        """
        action = TouchAction(self)
        action.press(originEl).move_to(destinationEl).release().perform()

        return self

    # convenience method added to Appium (NOT Selenium 3)
    def drag_and_drop(self, originEl, destinationEl):
        """Drag the origin element to the destination element

        :Args:
         - originEl - the element to drag
         - destinationEl - the element to drag to
        """
        action = TouchAction(self)
        action.long_press(originEl).move_to(destinationEl).release().perform()

        return self

    # convenience method added to Appium (NOT Selenium 3)
    def tap(self, positions, duration=None):
        """Taps on an particular place with up to five fingers, holding for a certain time

        :Args:
         - positions - an array of tuples representing the x/y coordinates of the fingers to tap. Length can be up to five.
         - duration - (optional) length of time to tap, in seconds

        :Usage:
            driver.tap([(100, 20), (100, 60), (100, 100)], 500)
        """
        ma = MultiAction(self)
        for position in positions:
            x = position[0]
            y = position[1]
            action = TouchAction(self)
            if duration:
                duration = duration * 1000 # we take seconds, but send milliseconds
                action.long_press(x=x, y=y, duration=duration).release()
            else:
                action.press(x=x, y=y).release()
            ma.add(action)

        ma.perform()

        return self

    # convenience method added to Appium (NOT Selenium 3)
    def swipe(self, startx, starty, endx, endy, duration=0):
        """Swipe from one point to another point, for an optional duration.

        :Args:
         - startx - x-coordinate at which to start
         - starty - y-coordinate at which to end
         - endx - x-coordinate at which to stop
         - endy - y-coordinate at which to stop
         - duration - (optional) time to take the swipe, in seconds.

        :Usage:
            driver.swipe(100, 100, 100, 400)
        """
        # `swipe` is something like press-wait-move_to-release, which the server
        # will translate into the correct action
        action = TouchAction(self)
        action \
            .press(x=startx, y=starty) \
            .wait(ms=duration) \
            .move_to(x=endx, y=endy) \
            .release()
        action.perform()

        return self

    # convenience method added to Appium (NOT Selenium 3)
    def pinch(self, element=None, startx=None, starty=None, endx=None, endy=None, duration=None):
        """Pinch on an element a certain amount

        :Args:
         - element - the element to pinch
         - percent - (optional) amount to pinch. Defaults to 200%
         - steps - (optional) number of steps in the pinch action

        :Usage:
            driver.pinch(element)
        """
        if element:
            element = element.id

        opts = {
            'element': element,
            'startX': startx,
            'startY': starty,
            'endX': endx,
            'endY': endy,
            'duration': duration
        };
        self.execute_script('mobile: pinchClose', opts)

        return self

    # convenience method added to Appium (NOT Selenium 3)
    # {startX: 114.0, startY: 198.0, endX: 257.0,
    #       endY: 256.0, duration: 5.0}
    def zoom(self, element=None, startx=None, starty=None, endx=None, endy=None, duration=None):
        """Zooms in on an element a certain amount

        :Args:
         - element - the element to zoom
         - percent - (optional) amount to zoom. Defaults to 200%
         - steps - (optional) number of steps in the zoom action

        :Usage:
            driver.zoom(element)
        """
        if element:
            element = element.id

        opts = {
            'element': element,
            'startX': startx,
            'startY': starty,
            'endX': endx,
            'endY': endy,
            'duration': duration
        };
        self.execute_script('mobile: pinchOpen', opts)

        return self


    def _addCommands(self):
        self.command_executor._commands[Command.CONTEXTS] = \
            ('GET', '/session/$sessionId/contexts')
        self.command_executor._commands[Command.GET_CURRENT_CONTEXT] = \
            ('GET', '/session/$sessionId/context')
        self.command_executor._commands[Command.SWITCH_TO_CONTEXT] = \
            ('POST', '/session/$sessionId/context')
        self.command_executor._commands[Command.TOUCH_ACTION] = \
            ('POST', '/session/$sessionId/touch/perform')
        self.command_executor._commands[Command.MULTI_ACTION] = \
            ('POST', '/session/$sessionId/touch/multi/perform')
