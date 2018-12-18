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

# pylint: disable=too-many-lines,too-many-public-methods,too-many-statements,no-self-use

import base64
import copy

from selenium.common.exceptions import TimeoutException, InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command as RemoteCommand
from selenium.webdriver.support.ui import WebDriverWait

from appium.common.helper import appium_bytes
from appium.webdriver.clipboard_content_type import ClipboardContentType
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from .errorhandler import MobileErrorHandler
from .extensions.context import Context
from .extensions.location import Location
from .mobilecommand import MobileCommand as Command
from .switch_to import MobileSwitchTo
from .webelement import WebElement as MobileWebElement

# From remote/webdriver.py
_W3C_CAPABILITY_NAMES = frozenset([
    'acceptInsecureCerts',
    'browserName',
    'browserVersion',
    'platformName',
    'pageLoadStrategy',
    'proxy',
    'setWindowRect',
    'timeouts',
    'unhandledPromptBehavior',
])

# From remote/webdriver.py
_OSS_W3C_CONVERSION = {
    'acceptSslCerts': 'acceptInsecureCerts',
    'version': 'browserVersion',
    'platform': 'platformName'
}

_EXTENSION_CAPABILITY = ':'
_FORCE_MJSONWP = 'forceMjsonwp'

# override
# Add appium prefix for the non-W3C capabilities


def _make_w3c_caps(caps):
    appium_prefix = 'appium:'

    caps = copy.deepcopy(caps)
    profile = caps.get('firefox_profile')
    first_match = {}
    if caps.get('proxy') and caps['proxy'].get('proxyType'):
        caps['proxy']['proxyType'] = caps['proxy']['proxyType'].lower()
    for k, v in caps.items():
        if v and k in _OSS_W3C_CONVERSION:
            first_match[_OSS_W3C_CONVERSION[k]] = v.lower() if k == 'platform' else v
        if k in _W3C_CAPABILITY_NAMES or _EXTENSION_CAPABILITY in k:
            first_match[k] = v
        else:
            if not k.startswith(appium_prefix):
                first_match[appium_prefix + k] = v
    if profile:
        moz_opts = first_match.get('moz:firefoxOptions', {})
        # If it's already present, assume the caller did that intentionally.
        if 'profile' not in moz_opts:
            # Don't mutate the original capabilities.
            new_opts = copy.deepcopy(moz_opts)
            new_opts['profile'] = profile
            first_match['moz:firefoxOptions'] = new_opts
    return {'firstMatch': [first_match]}


class WebDriver(Location, Context):

    def __init__(self, command_executor='http://127.0.0.1:4444/wd/hub',
                 desired_capabilities=None, browser_profile=None, proxy=None, keep_alive=False):

        super(WebDriver, self).__init__(command_executor, desired_capabilities, browser_profile, proxy, keep_alive)

        if self.command_executor is not None:
            self._addCommands()

        self.error_handler = MobileErrorHandler()
        self._switch_to = MobileSwitchTo(self)

        # add new method to the `find_by_*` pantheon
        By.IOS_UIAUTOMATION = MobileBy.IOS_UIAUTOMATION
        By.IOS_PREDICATE = MobileBy.IOS_PREDICATE
        By.IOS_CLASS_CHAIN = MobileBy.IOS_CLASS_CHAIN
        By.ANDROID_UIAUTOMATOR = MobileBy.ANDROID_UIAUTOMATOR
        By.ANDROID_VIEWTAG = MobileBy.ANDROID_VIEWTAG
        By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID
        By.IMAGE = MobileBy.IMAGE
        By.CUSTOM = MobileBy.CUSTOM

    def start_session(self, capabilities, browser_profile=None):
        """
        Override for Appium
        Creates a new session with the desired capabilities.

        :Args:
         - automation_name - The name of automation engine to use.
         - platform_name - The name of target platform.
         - platform_version - The kind of mobile device or emulator to use
         - app - The absolute local path or remote http URL to an .ipa or .apk file, or a .zip containing one of these.

        Read https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md for more details.
        """
        if not isinstance(capabilities, dict):
            raise InvalidArgumentException('Capabilities must be a dictionary')
        if browser_profile:
            if 'moz:firefoxOptions' in capabilities:
                capabilities['moz:firefoxOptions']['profile'] = browser_profile.encoded
            else:
                capabilities.update({'firefox_profile': browser_profile.encoded})

        parameters = self._merge_capabilities(capabilities)

        response = self.execute(RemoteCommand.NEW_SESSION, parameters)
        if 'sessionId' not in response:
            response = response['value']
        self.session_id = response['sessionId']
        self.capabilities = response.get('value')

        # if capabilities is none we are probably speaking to
        # a W3C endpoint
        if self.capabilities is None:
            self.capabilities = response.get('capabilities')

        # Double check to see if we have a W3C Compliant browser
        self.w3c = response.get('status') is None

    def _merge_capabilities(self, capabilities):
        """
        Manage capabilities whether W3C format or MJSONWP format
        """
        if _FORCE_MJSONWP in capabilities:
            force_mjsonwp = capabilities[_FORCE_MJSONWP]
            del capabilities[_FORCE_MJSONWP]

            if force_mjsonwp != False:
                return {'desiredCapabilities': capabilities}

        w3c_caps = _make_w3c_caps(capabilities)
        return {'capabilities': w3c_caps, 'desiredCapabilities': capabilities}

    def find_element(self, by=By.ID, value=None):
        """
        Override for Appium
        'Private' method used by the find_element_by_* methods.

        :Usage:
            Use the corresponding find_element_by_* instead of this.

        :rtype: WebElement
        """
        # TODO: If we need, we should enable below converter for Web context
        # if self.w3c:
        #     if by == By.ID:
        #         by = By.CSS_SELECTOR
        #         value = '[id="%s"]' % value
        #     elif by == By.TAG_NAME:
        #         by = By.CSS_SELECTOR
        #     elif by == By.CLASS_NAME:
        #         by = By.CSS_SELECTOR
        #         value = ".%s" % value
        #     elif by == By.NAME:
        #         by = By.CSS_SELECTOR
        #         value = '[name="%s"]' % value

        return self.execute(RemoteCommand.FIND_ELEMENT, {
            'using': by,
            'value': value})['value']

    def find_elements(self, by=By.ID, value=None):
        """
        Override for Appium
        'Private' method used by the find_elements_by_* methods.

        :Usage:
            Use the corresponding find_elements_by_* instead of this.

        :rtype: list of WebElement
        """
        # TODO: If we need, we should enable below converter for Web context
        # if self.w3c:
        #     if by == By.ID:
        #         by = By.CSS_SELECTOR
        #         value = '[id="%s"]' % value
        #     elif by == By.TAG_NAME:
        #         by = By.CSS_SELECTOR
        #     elif by == By.CLASS_NAME:
        #         by = By.CSS_SELECTOR
        #         value = ".%s" % value
        #     elif by == By.NAME:
        #         by = By.CSS_SELECTOR
        #         value = '[name="%s"]' % value

        # Return empty list if driver returns null
        # See https://github.com/SeleniumHQ/selenium/issues/4555

        return self.execute(RemoteCommand.FIND_ELEMENTS, {
            'using': by,
            'value': value})['value'] or []

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

    def find_element_by_ios_predicate(self, predicate_string):
        """Find an element by ios predicate string.

        :Args:
         - predicate_string - The predicate string

        :Usage:
            driver.find_element_by_ios_predicate('label == "myLabel"')
        """
        return self.find_element(by=By.IOS_PREDICATE, value=predicate_string)

    def find_elements_by_ios_predicate(self, predicate_string):
        """Finds elements by ios predicate string.

        :Args:
         - predicate_string - The predicate string

        :Usage:
            driver.find_elements_by_ios_predicate('label == "myLabel"')
        """
        return self.find_elements(by=By.IOS_PREDICATE, value=predicate_string)

    def find_element_by_ios_class_chain(self, class_chain_string):
        """Find an element by ios class chain string.

        :Args:
         - class_chain_string - The class chain string

        :Usage:
            driver.find_element_by_ios_class_chain('XCUIElementTypeWindow/XCUIElementTypeButton[3]')
        """
        return self.find_element(by=By.IOS_CLASS_CHAIN, value=class_chain_string)

    def find_elements_by_ios_class_chain(self, class_chain_string):
        """Finds elements by ios class chain string.

        :Args:
         - class_chain_string - The class chain string

        :Usage:
            driver.find_elements_by_ios_class_chain('XCUIElementTypeWindow[2]/XCUIElementTypeAny[-2]')
        """
        return self.find_elements(by=By.IOS_CLASS_CHAIN, value=class_chain_string)

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

    def find_element_by_android_viewtag(self, tag):
        """Finds element by [View#tags](https://developer.android.com/reference/android/view/View#tags) in Android.
        It works with [Espresso Driver](https://github.com/appium/appium-espresso-driver).

        :Args:
         - tag - The tag name of the view to look for

        :Usage:
            driver.find_element_by_android_viewtag('a tag name')
        """
        return self.find_element(by=By.ANDROID_VIEWTAG, value=tag)

    def find_elements_by_android_viewtag(self, tag):
        """Finds element by [View#tags](https://developer.android.com/reference/android/view/View#tags) in Android.
        It works with [Espresso Driver](https://github.com/appium/appium-espresso-driver).

        :Args:
         - tag - The tag name of the view to look for

        :Usage:
            driver.find_elements_by_android_viewtag('a tag name')
        """
        return self.find_elements(by=By.ANDROID_VIEWTAG, value=tag)

    def find_element_by_image(self, img_path):
        """Finds a portion of a screenshot by an image.
        Uses driver.find_image_occurrence under the hood.

        :Args:
        - img_path - a string corresponding to the path of a image

        :return: an Element object
        """
        with open(img_path, 'rb') as i_file:
            b64_data = base64.b64encode(i_file.read()).decode('UTF-8')

        return self.find_element(by=By.IMAGE, value=b64_data)

    def find_elements_by_image(self, img_path):
        """Finds a portion of a screenshot by an image.
        Uses driver.find_image_occurrence under the hood. Note that this will
        only ever return at most one element

        :Args:
        - img_path - a string corresponding to the path of a image

        :return: possibly-empty list of Elements
        """
        with open(img_path, 'rb') as i_file:
            b64_data = base64.b64encode(i_file.read()).decode('UTF-8')

        return self.find_elements(by=By.IMAGE, value=b64_data)

    def find_element_by_accessibility_id(self, accessibility_id):
        """Finds an element by accessibility id.

        :Args:
         - accessibility_id - a string corresponding to a recursive element search using the
         Id/Name that the native Accessibility options utilize

        :Usage:
            driver.find_element_by_accessibility_id()
        """
        return self.find_element(by=By.ACCESSIBILITY_ID, value=accessibility_id)

    def find_elements_by_accessibility_id(self, accessibility_id):
        """Finds elements by accessibility id.

        :Args:
         - accessibility_id - a string corresponding to a recursive element search using the
         Id/Name that the native Accessibility options utilize

        :Usage:
            driver.find_elements_by_accessibility_id()
        """
        return self.find_elements(by=By.ACCESSIBILITY_ID, value=accessibility_id)

    def find_element_by_custom(self, selector):
        """Finds an element in conjunction with a custom element finding plugin

        :Args:
         - selector - a string of the form "module:selector", where "module" is
           the shortcut name given in the customFindModules capability, and
           "selector" is the string that will be passed to the custom element
           finding plugin itself

        :Usage:
            driver.find_element_by_custom("foo:bar")
        """
        return self.find_element(by=By.CUSTOM, value=selector)

    def find_elements_by_custom(self, selector):
        """Finds elements in conjunction with a custom element finding plugin

        :Args:
         - selector - a string of the form "module:selector", where "module" is
           the shortcut name given in the customFindModules capability, and
           "selector" is the string that will be passed to the custom element
           finding plugin itself

        :Usage:
            driver.find_elements_by_custom("foo:bar")
        """
        return self.find_elements(by=By.CUSTOM, value=selector)

    def create_web_element(self, element_id):
        """
        Creates a web element with the specified element_id.
        Overrides method in Selenium WebDriver in order to always give them
        Appium WebElement
        """
        return MobileWebElement(self, element_id)

    # convenience method added to Appium (NOT Selenium 3)
    def scroll(self, origin_el, destination_el, duration=None):
        """Scrolls from one element to another

        :Args:
         - originalEl - the element from which to being scrolling
         - destinationEl - the element to scroll to
         - duration - a duration after pressing originalEl and move the element to destinationEl. Default is 600 ms for W3C spec. Zero for MJSONWP.

        :Usage:
            driver.scroll(el1, el2)
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

    # convenience method added to Appium (NOT Selenium 3)
    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        """Swipe from one point to another point, for an optional duration.

        :Args:
         - start_x - x-coordinate at which to start
         - start_y - y-coordinate at which to start
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
         - start_y - y-coordinate at which to start
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

    def app_strings(self, language=None, string_file=None):
        """Returns the application strings from the device for the specified
        language.

        :Args:
         - language - strings language code
         - string_file - the name of the string file to query
        """
        data = {}
        if language != None:
            data['language'] = language
        if string_file != None:
            data['stringFile'] = string_file
        return self.execute(Command.GET_APP_STRINGS, data)['value']

    def reset(self):
        """Resets the current application on the device.
        """
        self.execute(Command.RESET)
        return self

    def hide_keyboard(self, key_name=None, key=None, strategy=None):
        """Hides the software keyboard on the device. In iOS, use `key_name` to press
        a particular key, or `strategy`. In Android, no parameters are used.

        :Args:
         - key_name - key to press
         - strategy - strategy for closing the keyboard (e.g., `tapOutside`)
        """
        data = {}
        if key_name is not None:
            data['keyName'] = key_name
        elif key is not None:
            data['key'] = key
        elif strategy is None:
            strategy = 'tapOutside'
        data['strategy'] = strategy
        self.execute(Command.HIDE_KEYBOARD, data)
        return self

    def is_keyboard_shown(self):
        """Attempts to detect whether a software keyboard is present"""
        return self.execute(Command.IS_KEYBOARD_SHOWN)['value']

    # Needed for Selendroid
    def keyevent(self, keycode, metastate=None):
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
        self.execute(Command.KEY_EVENT, data)
        return self

    def press_keycode(self, keycode, metastate=None, flags=None):
        """Sends a keycode to the device. Android only. Possible keycodes can be
        found in http://developer.android.com/reference/android/view/KeyEvent.html.

        :Args:
         - keycode - the keycode to be sent to the device
         - metastate - meta information about the keycode being sent
         - flags - the set of key event flags
        """
        data = {
            'keycode': keycode,
        }
        if metastate is not None:
            data['metastate'] = metastate
        if flags is not None:
            data['flags'] = flags
        self.execute(Command.PRESS_KEYCODE, data)
        return self

    def long_press_keycode(self, keycode, metastate=None, flags=None):
        """Sends a long press of keycode to the device. Android only. Possible keycodes can be
        found in http://developer.android.com/reference/android/view/KeyEvent.html.

        :Args:
         - keycode - the keycode to be sent to the device
         - metastate - meta information about the keycode being sent
         - flags - the set of key event flags
        """
        data = {
            'keycode': keycode
        }
        if metastate is not None:
            data['metastate'] = metastate
        if flags is not None:
            data['flags'] = flags
        self.execute(Command.LONG_PRESS_KEYCODE, data)
        return self

    def press_button(self, button_name):
        """Sends a physical button name to the device to simulate the user pressing. iOS only.
        Possible button names can be found in
        https://github.com/appium/WebDriverAgent/blob/master/WebDriverAgentLib/Categories/XCUIDevice%2BFBHelpers.h

        :Args:
         - button_name - the button name to be sent to the device
        """
        data = {
            'name': button_name
        }
        self.execute_script('mobile: pressButton', data)
        return self

    @property
    def current_activity(self):
        """Retrieves the current activity running on the device.
        """
        return self.execute(Command.GET_CURRENT_ACTIVITY)['value']

    @property
    def current_package(self):
        """Retrieves the current package running on the device.
        """
        return self.execute(Command.GET_CURRENT_PACKAGE)['value']

    def wait_activity(self, activity, timeout, interval=1):
        """Wait for an activity: block until target activity presents
        or time out.

        This is an Android-only method.

        :Agrs:
         - activity - target activity
         - timeout - max wait time, in seconds
         - interval - sleep interval between retries, in seconds
        """
        try:
            WebDriverWait(self, timeout, interval).until(
                lambda d: d.current_activity == activity)
            return True
        except TimeoutException:
            return False

    def set_value(self, element, value):
        """Set the value on an element in the application.

        :Args:
         - element - the element whose value will be set
         - Value - the value to set on the element
        """
        data = {
            'id': element.id,
            'value': [value],
        }
        self.execute(Command.SET_IMMEDIATE_VALUE, data)
        return self

    def pull_file(self, path):
        """Retrieves the file at `path`. Returns the file's contents as base64.

        :Args:
         - path - the path to the file on the device
        """
        data = {
            'path': path,
        }
        return self.execute(Command.PULL_FILE, data)['value']

    def pull_folder(self, path):
        """Retrieves a folder at `path`. Returns the folder's contents zipped
        and encoded as Base64.

        :Args:
         - path - the path to the folder on the device
        """
        data = {
            'path': path,
        }
        return self.execute(Command.PULL_FOLDER, data)['value']

    def push_file(self, destination_path, base64data=None, source_path=None):
        """Puts the data from the file at `source_path`, encoded as Base64, in the file specified as `path`.

        Specify either `base64data` or `source_path`, if both specified default to `source_path`
        :param destination_path: the location on the device/simulator where the local file contents should be saved
        :param base64data: file contents, encoded as Base64, to be written to the file on the device/simulator
        :param source_path: local file path for the file to be loaded on device
        :return: WebDriver instance
        """
        if source_path is None and base64data is None:
            raise InvalidArgumentException('Must either pass base64 data or a local file path')

        if source_path is not None:
            try:
                with open(source_path, 'rb') as file:
                    data = file.read()
            except IOError:
                message = 'source_path {} could not be found. Are you sure the file exists?'.format(source_path)
                raise InvalidArgumentException(message)
            base64data = base64.b64encode(data).decode('utf-8')

        data = {
            'path': destination_path,
            'data': base64data,
        }
        self.execute(Command.PUSH_FILE, data)
        return self

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

    def install_app(self, app_path, **options):
        """Install the application found at `app_path` on the device.

        :Args:
         - app_path - the local or remote path to the application to install
         - options - the possible installation options.
         The following options are available for Android:
         `replace`: whether to reinstall/upgrade the package if it is
         already present on the device under test. True by default
         `timeout`: how much time to wait for the installation to complete.
         60000ms by default.
         `allowTestPackages`: whether to allow installation of packages marked
         as test in the manifest. False by default
         `useSdcard`: whether to use the SD card to install the app. False
         by default
         `grantPermissions`: whether to automatically grant application permissions
         on Android 6+ after the installation completes. False by default
        """
        data = {
            'appPath': app_path,
        }
        if options:
            data.update({'options': options})
        self.execute(Command.INSTALL_APP, data)
        return self

    def remove_app(self, app_id, **options):
        """Remove the specified application from the device.

        :Args:
         - app_id - the application id to be removed
         - options - the possible removal options.
         The following options are available for Android:
         `keepData`: whether to keep application data and caches after it is uninstalled.
         False by default
         `timeout`: how much time to wait for the uninstall to complete.
         20000ms by default.
        """
        data = {
            'appId': app_id,
        }
        if options:
            data.update({'options': options})
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

    def terminate_app(self, app_id, **options):
        """Terminates the application if it is running.

        :Args:
         - app_id - the application id to be terminates
         - options - the possible termination options.
         The following options are available for Android:
         `timeout`: how much time to wait for the uninstall to complete.
         500ms by default.

        :return: True if the app has been successfully terminated
        """
        data = {
            'appId': app_id,
        }
        if options:
            data.update({'options': options})
        return self.execute(Command.TERMINATE_APP, data)['value']

    def activate_app(self, app_id):
        """Activates the application if it is not running
        or is running in the background.

        :Args:
         - app_id - the application id to be activated

        :return: self instance for chaining
        """
        data = {
            'appId': app_id,
        }
        self.execute(Command.ACTIVATE_APP, data)
        return self

    def query_app_state(self, app_id):
        """Queries the state of the application.

        :Args:
         - app_id - the application id to be queried

        :return: One of possible application state constants. See ApplicationState
        class for more details.
        """
        data = {
            'appId': app_id,
        }
        return self.execute(Command.QUERY_APP_STATE, data)['value']

    def start_activity(self, app_package, app_activity, **opts):
        """Opens an arbitrary activity during a test. If the activity belongs to
        another application, that application is started and the activity is opened.

        This is an Android-only method.

        :Args:
        - app_package - The package containing the activity to start.
        - app_activity - The activity to start.
        - app_wait_package - Begin automation after this package starts (optional).
        - app_wait_activity - Begin automation after this activity starts (optional).
        - intent_action - Intent to start (optional).
        - intent_category - Intent category to start (optional).
        - intent_flags - Flags to send to the intent (optional).
        - optional_intent_arguments - Optional arguments to the intent (optional).
        - dont_stop_app_on_reset - Should the app be stopped on reset (optional)?
        """
        data = {
            'appPackage': app_package,
            'appActivity': app_activity
        }
        arguments = {
            'app_wait_package': 'appWaitPackage',
            'app_wait_activity': 'appWaitActivity',
            'intent_action': 'intentAction',
            'intent_category': 'intentCategory',
            'intent_flags': 'intentFlags',
            'optional_intent_arguments': 'optionalIntentArguments',
            'dont_stop_app_on_reset': 'dontStopAppOnReset'
        }
        for key, value in arguments.items():
            if key in opts:
                data[value] = opts[key]
        self.execute(Command.START_ACTIVITY, data)
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

    def lock(self, seconds=None):
        """Lock the device. No changes are made if the device is already unlocked.

        :Args:
         - seconds - (optional) the duration to lock the device, in seconds.
         The device is going to be locked forever until `unlock` is called
         if it equals or is less than zero, otherwise this call blocks until
         the timeout expires and unlocks the screen automatically.
        """
        if seconds is None:
            self.execute(Command.LOCK)
        else:
            self.execute(Command.LOCK, {'seconds': seconds})

        return self

    def unlock(self):
        """Unlock the device. No changes are made if the device
        is already locked.
        """
        self.execute(Command.UNLOCK)
        return self

    def is_locked(self):
        """Checks whether the device is locked.

        :returns:
         Either True or False
        """
        return self.execute(Command.IS_LOCKED)['value']

    def shake(self):
        """Shake the device.
        """
        self.execute(Command.SHAKE)
        return self

    def touch_id(self, match):
        """Simulate touchId on iOS Simulator
        """
        data = {
            'match': match
        }
        self.execute(Command.TOUCH_ID, data)
        return self

    def toggle_touch_id_enrollment(self):
        """Toggle enroll touchId on iOS Simulator
        """
        self.execute(Command.TOGGLE_TOUCH_ID_ENROLLMENT)
        return self

    def open_notifications(self):
        """Open notification shade in Android (API Level 18 and above)
        """
        self.execute(Command.OPEN_NOTIFICATIONS, {})
        return self

    @property
    def network_connection(self):
        """Returns an integer bitmask specifying the network connection type.
        Android only.
        Possible values are available through the enumeration `appium.webdriver.ConnectionType`
        """
        return self.execute(Command.GET_NETWORK_CONNECTION, {})['value']

    def set_network_connection(self, connectionType):
        """Sets the network connection type. Android only.
        Possible values:
            Value (Alias)      | Data | Wifi | Airplane Mode
            -------------------------------------------------
            0 (None)           | 0    | 0    | 0
            1 (Airplane Mode)  | 0    | 0    | 1
            2 (Wifi only)      | 0    | 1    | 0
            4 (Data only)      | 1    | 0    | 0
            6 (All network on) | 1    | 1    | 0
        These are available through the enumeration `appium.webdriver.ConnectionType`

        :Args:
         - connectionType - a member of the enum appium.webdriver.ConnectionType
        """
        data = {
            'parameters': {
                'type': connectionType
            }
        }
        return self.execute(Command.SET_NETWORK_CONNECTION, data)['value']

    @property
    def available_ime_engines(self):
        """Get the available input methods for an Android device. Package and
        activity are returned (e.g., ['com.android.inputmethod.latin/.LatinIME'])
        Android only.
        """
        return self.execute(Command.GET_AVAILABLE_IME_ENGINES, {})['value']

    def is_ime_active(self):
        """Checks whether the device has IME service active. Returns True/False.
        Android only.
        """
        return self.execute(Command.IS_IME_ACTIVE, {})['value']

    def activate_ime_engine(self, engine):
        """Activates the given IME engine on the device.
        Android only.

        :Args:
         - engine - the package and activity of the IME engine to activate (e.g.,
            'com.android.inputmethod.latin/.LatinIME')
        """
        data = {
            'engine': engine
        }
        self.execute(Command.ACTIVATE_IME_ENGINE, data)
        return self

    def deactivate_ime_engine(self):
        """Deactivates the currently active IME engine on the device.
        Android only.
        """
        self.execute(Command.DEACTIVATE_IME_ENGINE, {})
        return self

    @property
    def active_ime_engine(self):
        """Returns the activity and package of the currently active IME engine (e.g.,
        'com.android.inputmethod.latin/.LatinIME').
        Android only.
        """
        return self.execute(Command.GET_ACTIVE_IME_ENGINE, {})['value']

    def get_settings(self):
        """Returns the appium server Settings for the current session.
        Do not get Settings confused with Desired Capabilities, they are
        separate concepts. See https://github.com/appium/appium/blob/master/docs/en/advanced-concepts/settings.md
        """
        return self.execute(Command.GET_SETTINGS, {})['value']

    def update_settings(self, settings):
        """Set settings for the current session.
        For more on settings, see: https://github.com/appium/appium/blob/master/docs/en/advanced-concepts/settings.md

        :Args:
         - settings - dictionary of settings to apply to the current test session
        """
        data = {"settings": settings}

        self.execute(Command.UPDATE_SETTINGS, data)
        return self

    def toggle_wifi(self):
        """Toggle the wifi on the device, Android only.
        """
        self.execute(Command.TOGGLE_WIFI, {})
        return self

    def start_recording_screen(self, **options):
        """
        Start asynchronous screen recording process.

        :param options: The following options are supported:
        - remotePath: The remotePath upload option is the path to the remote location,
        where the resulting video from the previous screen recording should be uploaded.
        The following protocols are supported: http/https (multipart), ftp.
        Missing value (the default setting) means the content of the resulting
        file should be encoded as Base64 and passed as the endpoint response value, but
        an exception will be thrown if the generated media file is too big to
        fit into the available process memory.
        This option only has an effect if there is/was an active screen recording session
        and forced restart is not enabled (the default setting).
        - user: The name of the user for the remote authentication.
        Only has an effect if both `remotePath` and `password` are set.
        - password: The password for the remote authentication.
        Only has an effect if both `remotePath` and `user` are set.
        - method: The HTTP method name ('PUT'/'POST'). PUT method is used by default.
        Only has an effect if `remotePath` is set.
        - timeLimit: The actual time limit of the recorded video in seconds.
        The default value for both iOS and Android is 180 seconds (3 minutes).
        The maximum value for Android is 3 minutes.
        The maximum value for iOS is 10 minutes.
        - forcedRestart: Whether to ignore the result of previous capture and start a new recording
        immediately (`True` value). By default  (`False`) the endpoint will try to catch and return the result of
        the previous capture if it's still available.
        - bugReport: Makes the recorder to display an additional information on the video overlay,
        such as a timestamp, that is helpful in videos captured to illustrate bugs.
        This option is only supported since API level 27 (Android P).

        iOS Specific:
        - videoQuality: The video encoding quality: 'low', 'medium', 'high', 'photo'. Defaults to 'medium'.
        - videoType: The format of the screen capture to be recorded.
        Available formats: Execute `ffmpeg -codecs` in the terminal to see the list of supported video codecs.
        'mjpeg' by default. (Since Appium 1.10.0)
        - videoFps: The Frames Per Second rate of the recorded video. Change this value if the resulting video
        is too slow or too fast. Defaults to 10. This can decrease the resulting file size.
        - videoScale: The scaling value to apply. Read https://trac.ffmpeg.org/wiki/Scaling for possible values.
        No scale is applied by default. (Since Appium 1.10.0)

        Android Specific:
        - videoSize: The video size of the generated media file. The format is WIDTHxHEIGHT.
        The default value is the device's native display resolution (if supported),
        1280x720 if not. For best results, use a size supported by your device's
        Advanced Video Coding (AVC) encoder.
        - bitRate: The video bit rate for the video, in megabits per second.
        The default value is 4. You can increase the bit rate to improve video quality,
        but doing so results in larger movie files.

        :return: Base-64 encoded content of the recorded media file or an empty string
                 if the file has been successfully uploaded to a remote location
                 (depends on the actual `remotePath` value).
        """
        if 'password' in options:
            options['pass'] = options['password']
            del options['password']
        return self.execute(Command.START_RECORDING_SCREEN, options)['value']

    def stop_recording_screen(self, **options):
        """
        Gather the output from the previously started screen recording to a media file.

        :param options: The following options are supported:
        - remotePath: The remotePath upload option is the path to the remote location,
        where the resulting video should be uploaded.
        The following protocols are supported: http/https (multipart), ftp.
        Missing value (the default setting) means the content of the resulting
        file should be encoded as Base64 and passed as the endpoint response value, but
        an exception will be thrown if the generated media file is too big to
        fit into the available process memory.
        - user: The name of the user for the remote authentication.
        Only has an effect if both `remotePath` and `password` are set.
        - password: The password for the remote authentication.
        Only has an effect if both `remotePath` and `user` are set.
        - method: The HTTP method name ('PUT'/'POST'). PUT method is used by default.
        Only has an effect if `remotePath` is set.

        :return: Base-64 encoded content of the recorded media file or an empty string
                 if the file has been successfully uploaded to a remote location
                 (depends on the actual `remotePath` value).
        """
        if 'password' in options:
            options['pass'] = options['password']
            del options['password']
        return self.execute(Command.STOP_RECORDING_SCREEN, options)['value']

    def set_clipboard(self, content, content_type=ClipboardContentType.PLAINTEXT, label=None):
        """
        Set the content of the system clipboard

        :param content: The content to be set as bytearray string
        :param content_type: One of ClipboardContentType items. Only ClipboardContentType.PLAINTEXT
        is supported on Android
        :param label: Optional label argument, which only works for Android
        """
        options = {
            'content': base64.b64encode(content).decode('UTF-8'),
            'contentType': content_type,
        }
        if label:
            options['label'] = label
        self.execute(Command.SET_CLIPBOARD, options)

    def set_clipboard_text(self, text, label=None):
        """
        Copies the given text to the system clipboard

        :param text: The text to be set
        :param label: Optional label argument, which only works for Android
        """

        self.set_clipboard(appium_bytes(str(text), 'UTF-8'), ClipboardContentType.PLAINTEXT, label)

    def get_clipboard(self, content_type=ClipboardContentType.PLAINTEXT):
        """
        Receives the content of the system clipboard

        :param content_type: One of ClipboardContentType items. Only ClipboardContentType.PLAINTEXT
        is supported on Android
        :return: Clipboard content as base64-encoded string or an empty string
        if the clipboard is empty
        """
        base64_str = self.execute(Command.GET_CLIPBOARD, {
            'contentType': content_type
        })['value']
        return base64.b64decode(base64_str)

    def get_clipboard_text(self):
        """
        Receives the text of the system clipboard

        :return: The actual clipboard text or an empty string if the clipboard is empty
        """
        return self.get_clipboard(ClipboardContentType.PLAINTEXT).decode('UTF-8')

    def match_images_features(self, base64Image1, base64Image2, **opts):
        """
        Performs images matching by features. Read
        https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html
        for more details on this topic.
        The method supports all image formats, which are supported by OpenCV itself.

        :param base64Image1: base64-encoded content of the first image
        :param base64Image2: base64-encoded content of the second image
        :param opts: Possible options are:
        - visualize: Set it to True in order to return the visualization of the matching operation.
        matching visualization. False by default
        - detectorName: One of possible feature detector names:
        'AKAZE', 'AGAST', 'BRISK', 'FAST', 'GFTT', 'KAZE', 'MSER', 'SIFT', 'ORB'
        Some of these detectors are not enabled in the default OpenCV deployment.
        'ORB' By default.
        - matchFunc: One of supported matching functions names:
        'FlannBased', 'BruteForce', 'BruteForceL1', 'BruteForceHamming',
        'BruteForceHammingLut', 'BruteForceSL2'
        'BruteForce' by default
        - goodMatchesFactor: The maximum count of "good" matches (e. g. with minimal distances).
        This count is unlimited by default.
        :return: The dictionary containing the following entries:
        - visualization: base64-encoded content of PNG visualization of the current comparison
        operation. This entry is only present if `visualize` option is enabled
        - count: The count of matched edges on both images.
        The more matching edges there are no both images the more similar they are.
        - totalCount: The total count of matched edges on both images.
        It is equal to `count` if `goodMatchesFactor` does not limit the matches,
        otherwise it contains the total count of matches before `goodMatchesFactor` is
        applied.
        - points1: The array of matching points on the first image. Each point is a dictionary
        with 'x' and 'y' keys
        - rect1: The bounding rect for the `points1` array or a zero rect if not enough matching points
        were found. The rect is represented by a dictionary with 'x', 'y', 'width' and 'height' keys
        - points2: The array of matching points on the second image. Each point is a dictionary
        with 'x' and 'y' keys
        - rect2: The bounding rect for the `points2` array or a zero rect if not enough matching points
        were found. The rect is represented by a dictionary with 'x', 'y', 'width' and 'height' keys
        """
        options = {
            'mode': 'matchFeatures',
            'firstImage': base64Image1,
            'secondImage': base64Image2,
            'options': opts
        }
        return self.execute(Command.COMPARE_IMAGES, options)['value']

    def find_image_occurrence(self, base64FullImage, base64PartialImage, **opts):
        """
        Performs images matching by template to find possible occurrence of the partial image
        in the full image. Read
        https://docs.opencv.org/2.4/doc/tutorials/imgproc/histograms/template_matching/template_matching.html
        for more details on this topic.
        The method supports all image formats, which are supported by OpenCV itself.

        :param base64FullImage: base64-encoded content of the full image
        :param base64PartialImage: base64-encoded content of the partial image
        :param opts: Possible options are:
        - visualize: Set it to True in order to return the visualization of the matching operation.
        False by default
        :return:
        - visualization: base64-encoded content of PNG visualization of the current comparison
        operation. This entry is only present if `visualize` option is enabled
        - rect: The region of the partial image occurrence on the full image.
        The rect is represented by a dictionary with 'x', 'y', 'width' and 'height' keys
        """
        options = {
            'mode': 'matchTemplate',
            'firstImage': base64FullImage,
            'secondImage': base64PartialImage,
            'options': opts
        }
        return self.execute(Command.COMPARE_IMAGES, options)['value']

    def get_images_similarity(self, base64Image1, base64Image2, **opts):
        """
        Performs images matching to calculate the similarity score between them.
        The flow there is similar to the one used in
        `find_image_occurrence`, but it is mandatory that both images are of equal resolution.
        The method supports all image formats, which are supported by OpenCV itself.

        :param base64Image1: base64-encoded content of the first image
        :param base64Image2: base64-encoded content of the second image
        :param opts: Possible options are:
        - visualize: Set it to True in order to return the visualization of the matching operation.
        False by default
        :return:
        - visualization: base64-encoded content of PNG visualization of the current comparison
        operation. This entry is only present if `visualize` option is enabled
        - score: The similarity score as a float number in range [0.0, 1.0].
        1.0 is the highest score (means both images are totally equal).
        """
        options = {
            'mode': 'getSimilarity',
            'firstImage': base64Image1,
            'secondImage': base64Image2,
            'options': opts
        }
        return self.execute(Command.COMPARE_IMAGES, options)['value']

    @property
    def device_time(self):
        """Returns the date and time from the device
        """
        return self.execute(Command.GET_DEVICE_TIME, {})['value']

    @property
    def battery_info(self):
        """
        Retrieves battery information for the device under test.

        :return: A dictionary containing the following entries
        - level: Battery level in range [0.0, 1.0], where 1.0 means 100% charge.
        Any value lower than 0 means the level cannot be retrieved
        - state: Platform-dependent battery state value.
        On iOS (XCUITest):
        - 1: Unplugged
        - 2: Charging
        - 3: Full
        Any other value means the state cannot be retrieved
        On Android (UIAutomator2):
        - 2: Charging
        - 3: Discharging
        - 4: Not charging
        - 5: Full
        Any other value means the state cannot be retrieved
        """
        return self.execute_script('mobile: batteryInfo')

    def finger_print(self, finger_id):
        """
        Authenticate users by using their finger print scans on supported emulators.

        :param finger_id: Finger prints stored in Android Keystore system (from 1 to 10)
        """
        return self.execute(Command.FINGER_PRINT, {'fingerprintId': finger_id})['value']

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.CONTEXTS] = \
            ('GET', '/session/$sessionId/contexts')
        self.command_executor._commands[Command.GET_CURRENT_CONTEXT] = \
            ('GET', '/session/$sessionId/context')
        self.command_executor._commands[Command.SWITCH_TO_CONTEXT] = \
            ('POST', '/session/$sessionId/context')

        self.command_executor._commands[Command.TOGGLE_LOCATION_SERVICES] = \
            ('POST', '/session/$sessionId/appium/device/toggle_location_services')
        self.command_executor._commands[Command.GET_LOCATION] = \
            ('GET', '/session/$sessionId/location')
        self.command_executor._commands[Command.SET_LOCATION] = \
            ('POST', '/session/$sessionId/location')

        self.command_executor._commands[Command.TOUCH_ACTION] = \
            ('POST', '/session/$sessionId/touch/perform')
        self.command_executor._commands[Command.MULTI_ACTION] = \
            ('POST', '/session/$sessionId/touch/multi/perform')
        self.command_executor._commands[Command.GET_APP_STRINGS] = \
            ('POST', '/session/$sessionId/appium/app/strings')
        # Needed for Selendroid
        self.command_executor._commands[Command.KEY_EVENT] = \
            ('POST', '/session/$sessionId/appium/device/keyevent')
        self.command_executor._commands[Command.PRESS_KEYCODE] = \
            ('POST', '/session/$sessionId/appium/device/press_keycode')
        self.command_executor._commands[Command.LONG_PRESS_KEYCODE] = \
            ('POST', '/session/$sessionId/appium/device/long_press_keycode')
        self.command_executor._commands[Command.GET_CURRENT_ACTIVITY] = \
            ('GET', '/session/$sessionId/appium/device/current_activity')
        self.command_executor._commands[Command.GET_CURRENT_PACKAGE] = \
            ('GET', '/session/$sessionId/appium/device/current_package')
        self.command_executor._commands[Command.SET_IMMEDIATE_VALUE] = \
            ('POST', '/session/$sessionId/appium/element/$id/value')
        self.command_executor._commands[Command.PULL_FILE] = \
            ('POST', '/session/$sessionId/appium/device/pull_file')
        self.command_executor._commands[Command.PULL_FOLDER] = \
            ('POST', '/session/$sessionId/appium/device/pull_folder')
        self.command_executor._commands[Command.PUSH_FILE] = \
            ('POST', '/session/$sessionId/appium/device/push_file')
        self.command_executor._commands[Command.BACKGROUND] = \
            ('POST', '/session/$sessionId/appium/app/background')
        self.command_executor._commands[Command.IS_APP_INSTALLED] = \
            ('POST', '/session/$sessionId/appium/device/app_installed')
        self.command_executor._commands[Command.INSTALL_APP] = \
            ('POST', '/session/$sessionId/appium/device/install_app')
        self.command_executor._commands[Command.REMOVE_APP] = \
            ('POST', '/session/$sessionId/appium/device/remove_app')
        self.command_executor._commands[Command.TERMINATE_APP] = \
            ('POST', '/session/$sessionId/appium/device/terminate_app')
        self.command_executor._commands[Command.ACTIVATE_APP] = \
            ('POST', '/session/$sessionId/appium/device/activate_app')
        self.command_executor._commands[Command.QUERY_APP_STATE] = \
            ('POST', '/session/$sessionId/appium/device/app_state')
        self.command_executor._commands[Command.START_ACTIVITY] = \
            ('POST', '/session/$sessionId/appium/device/start_activity')
        self.command_executor._commands[Command.LAUNCH_APP] = \
            ('POST', '/session/$sessionId/appium/app/launch')
        self.command_executor._commands[Command.CLOSE_APP] = \
            ('POST', '/session/$sessionId/appium/app/close')
        self.command_executor._commands[Command.END_TEST_COVERAGE] = \
            ('POST', '/session/$sessionId/appium/app/end_test_coverage')
        self.command_executor._commands[Command.LOCK] = \
            ('POST', '/session/$sessionId/appium/device/lock')
        self.command_executor._commands[Command.UNLOCK] = \
            ('POST', '/session/$sessionId/appium/device/unlock')
        self.command_executor._commands[Command.IS_LOCKED] = \
            ('POST', '/session/$sessionId/appium/device/is_locked')
        self.command_executor._commands[Command.SHAKE] = \
            ('POST', '/session/$sessionId/appium/device/shake')
        self.command_executor._commands[Command.TOUCH_ID] = \
            ('POST', '/session/$sessionId/appium/simulator/touch_id')
        self.command_executor._commands[Command.TOGGLE_TOUCH_ID_ENROLLMENT] = \
            ('POST', '/session/$sessionId/appium/simulator/toggle_touch_id_enrollment')
        self.command_executor._commands[Command.RESET] = \
            ('POST', '/session/$sessionId/appium/app/reset')
        self.command_executor._commands[Command.HIDE_KEYBOARD] = \
            ('POST', '/session/$sessionId/appium/device/hide_keyboard')
        self.command_executor._commands[Command.IS_KEYBOARD_SHOWN] = \
            ('GET', '/session/$sessionId/appium/device/is_keyboard_shown')
        self.command_executor._commands[Command.OPEN_NOTIFICATIONS] = \
            ('POST', '/session/$sessionId/appium/device/open_notifications')
        self.command_executor._commands[Command.GET_NETWORK_CONNECTION] = \
            ('GET', '/session/$sessionId/network_connection')
        self.command_executor._commands[Command.SET_NETWORK_CONNECTION] = \
            ('POST', '/session/$sessionId/network_connection')
        self.command_executor._commands[Command.GET_AVAILABLE_IME_ENGINES] = \
            ('GET', '/session/$sessionId/ime/available_engines')
        self.command_executor._commands[Command.IS_IME_ACTIVE] = \
            ('GET', '/session/$sessionId/ime/activated')
        self.command_executor._commands[Command.ACTIVATE_IME_ENGINE] = \
            ('POST', '/session/$sessionId/ime/activate')
        self.command_executor._commands[Command.DEACTIVATE_IME_ENGINE] = \
            ('POST', '/session/$sessionId/ime/deactivate')
        self.command_executor._commands[Command.GET_ACTIVE_IME_ENGINE] = \
            ('GET', '/session/$sessionId/ime/active_engine')
        self.command_executor._commands[Command.REPLACE_KEYS] = \
            ('POST', '/session/$sessionId/appium/element/$id/replace_value')
        self.command_executor._commands[Command.GET_SETTINGS] = \
            ('GET', '/session/$sessionId/appium/settings')
        self.command_executor._commands[Command.UPDATE_SETTINGS] = \
            ('POST', '/session/$sessionId/appium/settings')
        self.command_executor._commands[Command.TOGGLE_WIFI] = \
            ('POST', '/session/$sessionId/appium/device/toggle_wifi')
        self.command_executor._commands[Command.LOCATION_IN_VIEW] = \
            ('GET', '/session/$sessionId/element/$id/location_in_view')
        self.command_executor._commands[Command.GET_DEVICE_TIME] = \
            ('GET', '/session/$sessionId/appium/device/system_time')
        self.command_executor._commands[Command.CLEAR] = \
            ('POST', '/session/$sessionId/element/$id/clear')
        self.command_executor._commands[Command.START_RECORDING_SCREEN] = \
            ('POST', '/session/$sessionId/appium/start_recording_screen')
        self.command_executor._commands[Command.STOP_RECORDING_SCREEN] = \
            ('POST', '/session/$sessionId/appium/stop_recording_screen')
        self.command_executor._commands[Command.SET_CLIPBOARD] = \
            ('POST', '/session/$sessionId/appium/device/set_clipboard')
        self.command_executor._commands[Command.GET_CLIPBOARD] = \
            ('POST', '/session/$sessionId/appium/device/get_clipboard')
        self.command_executor._commands[Command.COMPARE_IMAGES] = \
            ('POST', '/session/$sessionId/appium/compare_images')
        self.command_executor._commands[Command.FINGER_PRINT] = \
            ('POST', '/session/$sessionId/appium/device/finger_print')
