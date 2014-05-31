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
from .webelement import WebElement as MobileWebElement

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


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

        # add methods to the WebElement class
        WebElement.set_value = set_value

    @property
    def contexts(self):
        """
        Returns the contexts within the current session.

        :Usage:
            driver.contexts
        """
        return self.execute(Command.CONTEXTS)['value']

    @property
    def current_context(self):
        """
        Returns the current context of the current session.

        :Usage:
            driver.current_context
        """
        return self.execute(Command.GET_CURRENT_CONTEXT)['value']

    @property
    def context(self):
        """
        Returns the current context of the current session.

        :Usage:
            driver.context
        """
        return self.current_context

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
         - id - a string corresponding to a recursive element search using the
         Id/Name that the native Accessibility options utilize

        :Usage:
            driver.find_element_by_accessibility_id()
        """
        return self.find_element(by=By.ACCESSIBILITY_ID, value=id)

    def find_elements_by_accessibility_id(self, id):
        """Finds elements by accessibility id.

        :Args:
         - id - a string corresponding to a recursive element search using the
         Id/Name that the native Accessibility options utilize

        :Usage:
            driver.find_elements_by_accessibility_id()
        """
        return self.find_elements(by=By.ACCESSIBILITY_ID, value=id)

    def create_web_element(self, element_id):
        """
        Creates a web element with the specified element_id.
        Overrides method in Selenium WebDriver in order to always give them
        Appium WebElement
        """
        return MobileWebElement(self, element_id)

    # convenience method added to Appium (NOT Selenium 3)
    def scroll(self, origin_el, destination_el):
        """Scrolls from one element to another

        :Args:
         - originalEl - the element from which to being scrolling
         - destinationEl - the element to scroll to

        :Usage:
            driver.scroll(el1, el2)
        """
        action = TouchAction(self)
        action.press(origin_el).move_to(destination_el).release().perform()
        return self

    # convenience method added to Appium (NOT Selenium 3)
    def drag_and_drop(self, origin_el, destination_el):
        """Drag the origin element to the destination element

        :Args:
         - originEl - the element to drag
         - destinationEl - the element to drag to
        """
        action = TouchAction(self)
        action.long_press(origin_el).move_to(destination_el).release().perform()
        return self

    # convenience method added to Appium (NOT Selenium 3)
    def tap(self, positions, duration=None):
        """Taps on an particular place with up to five fingers, holding for a
        certain time

        :Args:
         - positions - an array of tuples representing the x/y coordinates of
         the fingers to tap. Length can be up to five.
         - duration - (optional) length of time to tap, in ms

        :Usage:
            driver.tap([(100, 20), (100, 60), (100, 100)], 500)
        """
        if len(positions) == 1:
            action = TouchAction(self)
            x = positions[0][0]
            y = positions[0][1]
            if duration:
                duration = duration
                action.long_press(x=x, y=y, duration=duration).release()
            else:
                action.press(x=x, y=y).release()
            action.perform()
        else:
            ma = MultiAction(self)
            for position in positions:
                x = position[0]
                y = position[1]
                action = TouchAction(self)
                if duration:
                    duration *= 1000  # we take seconds, but send milliseconds
                    action.long_press(x=x, y=y, duration=duration).release()
                else:
                    action.press(x=x, y=y).release()
                ma.add(action)

            ma.perform()
        return self

    # convenience method added to Appium (NOT Selenium 3)
    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        """Swipe from one point to another point, for an optional duration.

        :Args:
         - start_x - x-coordinate at which to start
         - start_y - y-coordinate at which to end
         - end_x - x-coordinate at which to stop
         - end_y - y-coordinate at which to stop
         - duration - (optional) time to take the swipe, in ms.

        :Usage:
            driver.swipe(100, 100, 100, 400)
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

    # convenience method added to Appium (NOT Selenium 3)
    def flick(self, start_x, start_y, end_x, end_y):
        """Flick from one point to another point.

        :Args:
         - start_x - x-coordinate at which to start
         - start_y - y-coordinate at which to end
         - end_x - x-coordinate at which to stop
         - end_y - y-coordinate at which to stop

        :Usage:
            driver.flick(100, 100, 100, 400)
        """
        action = TouchAction(self)
        action \
            .press(x=start_x, y=start_y) \
            .move_to(x=end_x, y=end_y) \
            .release()
        action.perform()
        return self

    # convenience method added to Appium (NOT Selenium 3)
    def pinch(self, element=None, percent=200, steps=50):
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
            'percent': percent,
            'steps': steps,
        }
        self.execute_script('mobile: pinchClose', opts)
        return self

    # convenience method added to Appium (NOT Selenium 3)
    def zoom(self, element=None, percent=200, steps=50):
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
            'percent': percent,
            'steps': steps,
        }
        self.execute_script('mobile: pinchOpen', opts)
        return self

    def app_strings(self, language=None):
        """Returns the application strings from the device for the specified
        language.

        :Args:
         - language - strings language code
        """
        data = {}
        if language != None:
            data['language'] = language
        return self.execute(Command.GET_APP_STRINGS, data)['value']

    def reset(self):
        """Resets the current application on the device.
        """
        self.execute(Command.RESET)
        return self

    def hide_keyboard(self, key_name=None):
        """Hides the software keyboard on the device, using the specified key to
        press. If no key name is given, the keyboard is closed by moving focus
        from the text field. iOS only.
        """
        data = {}
        if key_name is not None:
            data['keyName'] = key_name
        self.execute(Command.HIDE_KEYBOARD, data)
        return self

    def press_keycode(self, keycode, metastate=None):
        """Sends a keycode to the device. Android only. Possible keycodes can be
        found in http://developer.android.com/reference/android/view/KeyEvent.html.

        :Args:
         - keycode - the keycode to be sent to the device
         - metastate - meta information about the keycode being sent
        """
        data = {
            'keycode': keycode,
        }
        if metastate is not None:
            data['metastate'] = metastate
        self.execute(Command.PRESS_KEYCODE, data)
        return self

    def long_press_keycode(self, keycode, metastate=None):
        """Sends a long press of keycode to the device. Android only. Possible keycodes can be
        found in http://developer.android.com/reference/android/view/KeyEvent.html.

        :Args:
         - keycode - the keycode to be sent to the device
         - metastate - meta information about the keycode being sent
        """
        data = {
            'keycode': keycode
        }
        if metastate != None:
            data['metastate'] = metastate
        self.execute(Command.LONG_PRESS_KEYCODE, data)
        return self

    @property
    def current_activity(self):
        """Retrieves the current activity on the device.
        """
        return self.execute(Command.GET_CURRENT_ACTIVITY)['value']

    def set_value(self, element, value):
        """Set the value on an element in the application.

        :Args:
         - element - the element whose value will be set
         - Value - the value to set on the element
        """
        data = {
            'elementId': element.id,
            'value': [value],
        }
        self.execute(Command.SET_IMMEDIATE_VALUE, data)
        return self

    def pull_file(self, path):
        """Retrieves the file at `path`. Returns the file's content encoded as
        Base64.

        :Args:
         - path - the path to the file on the device
        """
        data = {
            'path': path,
        }
        return self.execute(Command.PULL_FILE, data)['value']

    def push_file(self, path, base64data):
        """Puts the data, encoded as Base64, in the file specified as `path`.

        :Args:
         - path - the path on the device
         - base64data - data, encoded as Base64, to be written to the file
        """
        data = {
            'path': path,
            'data': base64data,
        }
        self.execute(Command.PUSH_FILE, data)
        return self

    def complex_find(self, selector):
        """Performs a find for elements in the current application.

        :Args:
         - selector - an array of selection criteria
        """
        data = {
            'selector': selector,
        }
        return self.execute(Command.COMPLEX_FIND, data)['value']

    def background_app(self, seconds):
        """Puts the application in the background on the device for a certain
        duration.

        :Args:
         - seconds - the duration for the application to remain in the background
        """
        data = {
            'seconds': seconds,
        }
        self.execute(Command.BACKGROUND, data)
        return self

    def is_app_installed(self, bundle_id):
        """Checks whether the application specified by `bundle_id` is installed
        on the device.

        :Args:
         - bundle_id - the id of the application to query
        """
        data = {
            'bundleId': bundle_id,
        }
        return self.execute(Command.IS_APP_INSTALLED, data)['value']

    def install_app(self, app_path):
        """Install the application found at `app_path` on the device.

        :Args:
         - app_path - the local or remote path to the application to install
        """
        data = {
            'appPath': app_path,
        }
        self.execute(Command.INSTALL_APP, data)
        return self

    def remove_app(self, app_id):
        """Remove the specified application from the device.

        :Args:
         - app_id - the application id to be removed
        """
        data = {
            'appId': app_id,
        }
        self.execute(Command.REMOVE_APP, data)
        return self

    def launch_app(self):
        """Start on the device the application specified in the desired capabilities.
        """
        self.execute(Command.LAUNCH_APP)
        return self

    def close_app(self):
        """Stop the running application, specified in the desired capabilities, on
        the device.
        """
        self.execute(Command.CLOSE_APP)
        return self

    def end_test_coverage(self, intent, path):
        """Ends the coverage collection and pull the coverage.ec file from the device.
        Android only.

        See https://github.com/appium/appium/blob/master/docs/en/android_coverage.md

        :Args:
         - intent - description of operation to be performed
         - path - path to coverage.ec file to be pulled from the device
        """
        data = {
            'intent': intent,
            'path': path,
        }
        return self.execute(Command.END_TEST_COVERAGE, data)['value']

    def lock(self, seconds):
        """Lock the device for a certain period of time. iOS only.

        :Args:
         - the duration to lock the device, in seconds
        """
        data = {
            'seconds': seconds,
        }
        self.execute(Command.LOCK, data)
        return self

    def shake(self):
        """Shake the device.
        """
        self.execute(Command.SHAKE)
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
        self.command_executor._commands[Command.GET_APP_STRINGS] = \
            ('POST', '/session/$sessionId/appium/app/strings')
        self.command_executor._commands[Command.PRESS_KEYCODE] = \
            ('POST', '/session/$sessionId/appium/device/press_keycode')
        self.command_executor._commands[Command.LONG_PRESS_KEYCODE] = \
            ('POST', '/session/$sessionId/appium/device/long_press_keycode')
        self.command_executor._commands[Command.GET_CURRENT_ACTIVITY] = \
            ('GET', '/session/$sessionId/appium/device/current_activity')
        self.command_executor._commands[Command.SET_IMMEDIATE_VALUE] = \
            ('POST', '/session/$sessionId/appium/element/$elementId/value')
        self.command_executor._commands[Command.PULL_FILE] = \
            ('POST', '/session/$sessionId/appium/device/pull_file')
        self.command_executor._commands[Command.PUSH_FILE] = \
            ('POST', '/session/$sessionId/appium/device/push_file')
        self.command_executor._commands[Command.COMPLEX_FIND] = \
            ('POST', '/session/$sessionId/appium/app/complex_find')
        self.command_executor._commands[Command.BACKGROUND] = \
            ('POST', '/session/$sessionId/appium/app/background')
        self.command_executor._commands[Command.IS_APP_INSTALLED] = \
            ('POST', '/session/$sessionId/appium/device/app_installed')
        self.command_executor._commands[Command.INSTALL_APP] = \
            ('POST', '/session/$sessionId/appium/device/install_app')
        self.command_executor._commands[Command.REMOVE_APP] = \
            ('POST', '/session/$sessionId/appium/device/remove_app')
        self.command_executor._commands[Command.LAUNCH_APP] = \
            ('POST', '/session/$sessionId/appium/app/launch')
        self.command_executor._commands[Command.CLOSE_APP] = \
            ('POST', '/session/$sessionId/appium/app/close')
        self.command_executor._commands[Command.END_TEST_COVERAGE] = \
            ('POST', '/session/$sessionId/appium/app/end_test_coverage')
        self.command_executor._commands[Command.LOCK] = \
            ('POST', '/session/$sessionId/appium/device/lock')
        self.command_executor._commands[Command.SHAKE] = \
            ('POST', '/session/$sessionId/appium/device/shake')
        self.command_executor._commands[Command.RESET] = \
            ('POST', '/session/$sessionId/appium/app/reset')
        self.command_executor._commands[Command.HIDE_KEYBOARD] = \
            ('POST', '/session/$sessionId/appium/device/hide_keyboard')


# monkeypatched method for WebElement
def set_value(self, value):
    """Set the value on this element in the application
    """
    data = {
        'elementId': self.id,
        'value': [value],
    }
    self._execute(Command.SET_IMMEDIATE_VALUE, data)
    return self
