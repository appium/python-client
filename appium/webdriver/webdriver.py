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

import copy

from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command as RemoteCommand
from selenium.webdriver.remote.remote_connection import RemoteConnection

from appium.common.logger import logger
from appium.webdriver.common.mobileby import MobileBy

from .appium_connection import AppiumConnection
from .errorhandler import MobileErrorHandler
from .extensions.action_helpers import ActionHelpers
from .extensions.android.activities import Activities
from .extensions.android.common import Common
from .extensions.android.display import Display
from .extensions.android.gsm import Gsm
from .extensions.android.network import Network
from .extensions.android.performance import Performance
from .extensions.android.power import Power
from .extensions.android.sms import Sms
from .extensions.android.system_bars import SystemBars
from .extensions.applications import Applications
from .extensions.clipboard import Clipboard
from .extensions.context import Context
from .extensions.device_time import DeviceTime
from .extensions.execute_driver import ExecuteDriver
from .extensions.execute_mobile_command import ExecuteMobileCommand
from .extensions.hw_actions import HardwareActions
from .extensions.images_comparison import ImagesComparison
from .extensions.ime import IME
from .extensions.keyboard import Keyboard
from .extensions.location import Location
from .extensions.log_event import LogEvent
from .extensions.remote_fs import RemoteFS
from .extensions.screen_record import ScreenRecord
from .extensions.search_context import AppiumSearchContext
from .extensions.session import Session
from .extensions.settings import Settings
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


class WebDriver(
    AppiumSearchContext,
    ActionHelpers,
    Activities,
    Applications,
    Clipboard,
    Context,
    Common,
    DeviceTime,
    Display,
    ExecuteDriver,
    ExecuteMobileCommand,
    Gsm,
    HardwareActions,
    ImagesComparison,
    IME,
    Keyboard,
    Location,
    LogEvent,
    Network,
    Performance,
    Power,
    RemoteFS,
    ScreenRecord,
    Session,
    Settings,
    Sms,
    SystemBars
):

    def __init__(self, command_executor='http://127.0.0.1:4444/wd/hub',
                 desired_capabilities=None, browser_profile=None, proxy=None, keep_alive=True, direct_connection=False):

        super(WebDriver, self).__init__(
            AppiumConnection(command_executor, keep_alive=keep_alive),
            desired_capabilities,
            browser_profile,
            proxy
        )

        if hasattr(self, 'command_executor'):
            self._addCommands()

        self.error_handler = MobileErrorHandler()
        self._switch_to = MobileSwitchTo(self)

        if direct_connection:
            self._update_command_executor(keep_alive=keep_alive)

        # add new method to the `find_by_*` pantheon
        By.IOS_UIAUTOMATION = MobileBy.IOS_UIAUTOMATION
        By.IOS_PREDICATE = MobileBy.IOS_PREDICATE
        By.IOS_CLASS_CHAIN = MobileBy.IOS_CLASS_CHAIN
        By.ANDROID_UIAUTOMATOR = MobileBy.ANDROID_UIAUTOMATOR
        By.ANDROID_VIEWTAG = MobileBy.ANDROID_VIEWTAG
        By.WINDOWS_UI_AUTOMATION = MobileBy.WINDOWS_UI_AUTOMATION
        By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID
        By.IMAGE = MobileBy.IMAGE
        By.CUSTOM = MobileBy.CUSTOM

    def _update_command_executor(self, keep_alive):
        """Update command executor following directConnect feature"""
        direct_protocol = 'directConnectProtocol'
        direct_host = 'directConnectHost'
        direct_port = 'directConnectPort'
        direct_path = 'directConnectPath'

        if (not {direct_protocol, direct_host, direct_port, direct_path}.issubset(set(self.capabilities))):
            message = 'Direct connect capabilities from server were:\n'
            for key in [direct_protocol, direct_host, direct_port, direct_path]:
                message += '{}: \'{}\'\n'.format(key, self.capabilities.get(key, ''))
            logger.warning(message)
            return

        protocol = self.capabilities[direct_protocol]
        hostname = self.capabilities[direct_host]
        port = self.capabilities[direct_port]
        path = self.capabilities[direct_path]
        executor = '{scheme}://{hostname}:{port}{path}'.format(
            scheme=protocol,
            hostname=hostname,
            port=port,
            path=path
        )

        logger.info('Updated request endpoint to %s', executor)
        # Override command executor
        self.command_executor = RemoteConnection(executor, keep_alive=keep_alive)
        self._addCommands()

    def start_session(self, capabilities, browser_profile=None):
        """Creates a new session with the desired capabilities.

        Override for Appium

        Args:
            automation_name: The name of automation engine to use.
            platform_name: The name of target platform.
            platform_version: The kind of mobile device or emulator to use
            app: The absolute local path or remote http URL to an .ipa or .apk file, or a .zip containing one of these.

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
        self.command_executor.w3c = self.w3c

    def _merge_capabilities(self, capabilities):
        """Manage capabilities whether W3C format or MJSONWP format
        """
        if _FORCE_MJSONWP in capabilities:
            force_mjsonwp = capabilities[_FORCE_MJSONWP]
            del capabilities[_FORCE_MJSONWP]

            if force_mjsonwp != False:
                return {'desiredCapabilities': capabilities}

        w3c_caps = _make_w3c_caps(capabilities)
        return {'capabilities': w3c_caps, 'desiredCapabilities': capabilities}

    def find_element(self, by=By.ID, value=None):
        """'Private' method used by the find_element_by_* methods.

        Override for Appium

        Usage:
            Use the corresponding find_element_by_* instead of this.

        Returns:
            `appium.webdriver.webelement.WebElement`

        :rtype: `MobileWebElement`
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
        """'Private' method used by the find_elements_by_* methods.

        Override for Appium

        Usage:
            Use the corresponding find_elements_by_* instead of this.

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`

        :rtype: list of `MobileWebElement`
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

    def create_web_element(self, element_id, w3c=False):
        """Creates a web element with the specified element_id.

        Overrides method in Selenium WebDriver in order to always give them
        Appium WebElement

        Args:
            element_id (int): The element id to create a web element
            w3c (bool): Whether the element is W3C or MJSONWP

        Returns:
            `MobileWebElement`
        """
        return MobileWebElement(self, element_id, w3c)

    def set_value(self, element, value):
        """Set the value on an element in the application.

        Args:
            element (`appium.webdriver.webelement.WebElement`: the element whose value will be set
            value (str): the value to set on the element

        Returns:
            `appium.webdriver.webdriver.WebDriver`
        """
        data = {
            'id': element.id,
            'value': [value],
        }
        self.execute(Command.SET_IMMEDIATE_VALUE, data)
        return self

    # pylint: disable=protected-access

    def _addCommands(self):
        # call the overridden command binders from all mixin classes except for
        # appium.webdriver.webdriver.WebDriver and its sub-classes
        # https://github.com/appium/python-client/issues/342
        for mixin_class in filter(lambda x: not issubclass(x, WebDriver), self.__class__.__mro__):
            if hasattr(mixin_class, self._addCommands.__name__):
                getattr(mixin_class, self._addCommands.__name__, None)(self)

        self.command_executor._commands[Command.TOUCH_ACTION] = \
            ('POST', '/session/$sessionId/touch/perform')
        self.command_executor._commands[Command.MULTI_ACTION] = \
            ('POST', '/session/$sessionId/touch/multi/perform')
        self.command_executor._commands[Command.SET_IMMEDIATE_VALUE] = \
            ('POST', '/session/$sessionId/appium/element/$id/value')

        # TODO Move commands for element to webelement
        self.command_executor._commands[Command.REPLACE_KEYS] = \
            ('POST', '/session/$sessionId/appium/element/$id/replace_value')
        self.command_executor._commands[Command.CLEAR] = \
            ('POST', '/session/$sessionId/element/$id/clear')
        self.command_executor._commands[Command.LOCATION_IN_VIEW] = \
            ('GET', '/session/$sessionId/element/$id/location_in_view')
