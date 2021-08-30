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
from typing import Any, Callable, Dict, List, Optional, Tuple, TypeVar, Union

from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command as RemoteCommand
from selenium.webdriver.remote.remote_connection import RemoteConnection

from appium.common.logger import logger
from appium.webdriver.command_method import CommandMethod
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
_W3C_CAPABILITY_NAMES = frozenset(
    [
        'acceptInsecureCerts',
        'browserName',
        'browserVersion',
        'platformName',
        'pageLoadStrategy',
        'proxy',
        'setWindowRect',
        'timeouts',
        'unhandledPromptBehavior',
    ]
)

# From remote/webdriver.py
_OSS_W3C_CONVERSION = {'acceptSslCerts': 'acceptInsecureCerts', 'version': 'browserVersion', 'platform': 'platformName'}

_EXTENSION_CAPABILITY = ':'
_FORCE_MJSONWP = 'forceMjsonwp'

# override
# Add appium prefix for the non-W3C capabilities


def _make_w3c_caps(caps: Dict) -> Dict[str, List[Dict[str, Any]]]:
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


T = TypeVar('T', bound='WebDriver')


class ExtensionBase:
    """
    Used to define an extension command as driver's methods.

    Example:
        When you want to add `example_command` which calls a get request to
        `session/$sessionId/path/to/your/custom/url`.

        1. Defines an extension as a subclass of `ExtensionBase`
            class YourCustomCommand(ExtensionBase):
                def method_name(self):
                    return 'custom_method_name'

                # Define a method with the name of `method_name`
                def custom_method_name(self):
                    # Generally the response of Appium follows `{ 'value': { data } }`
                    # format.
                    return self.execute()['value']

                # Used to register the command pair as "Appium command" in this driver.
                def add_command(self):
                    return ('GET', 'session/$sessionId/path/to/your/custom/url')

        2. Creates a session with the extension.
            # Appium capabilities
            desired_caps = { ... }
            driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps,
                extensions=[YourCustomCommand])

        3. Calls the custom command
            # Then, the driver calls a get request against
            # `session/$sessionId/path/to/your/custom/url`. `$sessionId` will be
            # replaced properly in the driver. Then, the method returns
            # the `value` part of the response.
            driver.custom_method_name()

        4. Remove added commands (if needed)
            # New commands are added by `setattr`. They remain in the module,
            # so you should explicitly delete them to define the same name method
            # with different arguments or process in the method.
            driver.delete_extensions()


        You can give arbitrary arguments for the command like the below.

            class YourCustomCommand(ExtensionBase):
                def method_name(self):
                    return 'custom_method_name'

                def test_command(self, argument):
                    return self.execute(argument)['value']

                def add_command(self):
                    return ('post', 'session/$sessionId/path/to/your/custom/url')

            driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps,
                extensions=[YourCustomCommand])

            # Then, the driver sends a post request to `session/$sessionId/path/to/your/custom/url`
            # with `{'dummy_arg': 'as a value'}` JSON body.
            driver.custom_method_name({'dummy_arg': 'as a value'})


        When you customize the URL dinamically with element id.

            class CustomURLCommand(ExtensionBase):
                def method_name(self):
                    return 'custom_method_name'

                def custom_method_name(self, element_id):
                    return self.execute({'id': element_id})['value']

                def add_command(self):
                    return ('GET', 'session/$sessionId/path/to/your/custom/$id/url')

            driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps,
                extensions=[YourCustomCommand])
            element = driver.find_element_by_accessibility_id('id')

            # Then, the driver calls a get request to `session/$sessionId/path/to/your/custom/$id/url`
            # with replacing the `$id` with the given `element.id`
            driver.custom_method_name(element.id)
    """

    def __init__(self, execute: Callable[[str, Dict], Dict[str, Any]]):
        self._execute = execute

    def execute(self, parameters: Dict[str, Any] = None) -> Any:
        param = {}
        if parameters:
            param = parameters
        return self._execute(self.method_name(), param)

    def method_name(self) -> str:
        """
        Expected to return a method name.
        This name will be available as a driver method.

        Returns:
            'str' The method name.
        """
        raise NotImplementedError()

    def add_command(self) -> Tuple[str, str]:
        """
        Expected to define the pair of HTTP method and its URL.
        """
        raise NotImplementedError()


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
    SystemBars,
):
    def __init__(
        self,
        command_executor: str = 'http://127.0.0.1:4444/wd/hub',
        desired_capabilities: Optional[Dict] = None,
        browser_profile: str = None,
        proxy: str = None,
        keep_alive: bool = True,
        direct_connection: bool = False,
        extensions: List[T] = [],
        strict_ssl: bool = True,
    ):

        if strict_ssl is False:
            # pylint: disable=E1101
            import urllib3

            AppiumConnection.set_certificate_bundle_path(None)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        super().__init__(
            AppiumConnection(command_executor, keep_alive=keep_alive), desired_capabilities, browser_profile, proxy
        )

        if hasattr(self, 'command_executor'):
            self._addCommands()

        self.error_handler = MobileErrorHandler()

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

        self._extensions = extensions
        for extension in self._extensions:
            instance = extension(self.execute)
            method_name = instance.method_name()
            if hasattr(WebDriver, method_name):
                logger.debug(f"Overriding the method '{method_name}'")

            # add a new method named 'instance.method_name()' and call it
            setattr(WebDriver, method_name, getattr(instance, method_name))
            method, url_cmd = instance.add_command()
            self.command_executor._commands[method_name] = (method.upper(), url_cmd)  # type: ignore

    def delete_extensions(self) -> None:
        """Delete extensions added in the class with 'setattr'"""
        for extension in self._extensions:
            instance = extension(self.execute)
            method_name = instance.method_name()
            if hasattr(WebDriver, method_name):
                delattr(WebDriver, method_name)

    def _update_command_executor(self, keep_alive: bool) -> None:
        """Update command executor following directConnect feature"""
        direct_protocol = 'directConnectProtocol'
        direct_host = 'directConnectHost'
        direct_port = 'directConnectPort'
        direct_path = 'directConnectPath'

        if not {direct_protocol, direct_host, direct_port, direct_path}.issubset(set(self.caps)):
            message = 'Direct connect capabilities from server were:\n'
            for key in [direct_protocol, direct_host, direct_port, direct_path]:
                message += '{}: \'{}\'\n'.format(key, self.caps.get(key, ''))
            logger.warning(message)
            return

        protocol = self.caps[direct_protocol]
        hostname = self.caps[direct_host]
        port = self.caps[direct_port]
        path = self.caps[direct_path]
        executor = f'{protocol}://{hostname}:{port}{path}'

        logger.info('Updated request endpoint to %s', executor)
        # Override command executor
        self.command_executor = RemoteConnection(executor, keep_alive=keep_alive)
        self._addCommands()

    # https://github.com/SeleniumHQ/selenium/blob/06fdf2966df6bca47c0ae45e8201cd30db9b9a49/py/selenium/webdriver/remote/webdriver.py#L277
    def start_session(self, capabilities: Dict, browser_profile: Optional[str] = None) -> None:
        """Creates a new session with the desired capabilities.

        Override for Appium

        Args:
            capabilities: Capabilities which have following keys like 'automation_name', 'platform_name', 'platform_version', 'app'.
                          Read https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md for more details.
            browser_profile: Browser profile
        """
        if not isinstance(capabilities, dict):
            raise InvalidArgumentException('Capabilities must be a dictionary')
        if browser_profile:
            if 'moz:firefoxOptions' in capabilities:
                # encoded is defined in selenium's original codes
                capabilities['moz:firefoxOptions']['profile'] = browser_profile.encoded  # type: ignore
            else:
                # encoded is defined in selenium's original codes
                capabilities.update({'firefox_profile': browser_profile.encoded})  # type: ignore

        parameters = self._merge_capabilities(capabilities)

        response = self.execute(RemoteCommand.NEW_SESSION, parameters)
        if 'sessionId' not in response:
            response = response['value']
        self.session_id = response['sessionId']
        self.caps = response.get('value')

        # if capabilities is none we are probably speaking to
        # a W3C endpoint
        if self.caps is None:
            self.caps = response.get('capabilities')

        # Double check to see if we have a W3C Compliant browser
        self.w3c = response.get('status') is None
        self.command_executor.w3c = self.w3c

    def _merge_capabilities(self, capabilities: Dict) -> Dict[str, Any]:
        """Manage capabilities whether W3C format or MJSONWP format"""
        w3c_caps = _make_w3c_caps(capabilities)
        return {'capabilities': w3c_caps, 'desiredCapabilities': capabilities}

    def find_element(self, by: str = By.ID, value: Union[str, Dict] = None) -> MobileWebElement:
        """'Private' method used by the find_element_by_* methods.

        Override for Appium

        Usage:
            Use the corresponding find_element_by_* instead of this.

        Returns:
            `appium.webdriver.webelement.WebElement`: The found element

        """
        # TODO: If we need, we should enable below converter for Web context
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

        return self.execute(RemoteCommand.FIND_ELEMENT, {'using': by, 'value': value})['value']

    def find_elements(self, by: str = By.ID, value: Union[str, Dict] = None) -> Union[List[MobileWebElement], List]:
        """'Private' method used by the find_elements_by_* methods.

        Override for Appium

        Usage:
            Use the corresponding find_elements_by_* instead of this.

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`: The found elements
        """
        # TODO: If we need, we should enable below converter for Web context
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

        return self.execute(RemoteCommand.FIND_ELEMENTS, {'using': by, 'value': value})['value'] or []

    def create_web_element(self, element_id: Union[int, str]) -> MobileWebElement:
        """Creates a web element with the specified element_id.

        Overrides method in Selenium WebDriver in order to always give them
        Appium WebElement

        Args:
            element_id: The element id to create a web element

        Returns:
            `MobileWebElement`
        """
        return MobileWebElement(self, element_id)

    def set_value(self, element: MobileWebElement, value: str) -> T:
        """Set the value on an element in the application.

        Args:
            element: the element whose value will be set
            value: the value to set on the element

        Returns:
            `appium.webdriver.webdriver.WebDriver`: Self instance
        """
        data = {
            'id': element.id,
            'value': [value],
        }
        self.execute(Command.SET_IMMEDIATE_VALUE, data)
        return self

    @property
    def switch_to(self) -> MobileSwitchTo:
        """Returns an object containing all options to switch focus into

        Override for appium

        Returns:
            `appium.webdriver.switch_to.MobileSwitchTo`

        """

        return MobileSwitchTo(self)

    # pylint: disable=protected-access

    def _addCommands(self) -> None:
        # call the overridden command binders from all mixin classes except for
        # appium.webdriver.webdriver.WebDriver and its sub-classes
        # https://github.com/appium/python-client/issues/342
        for mixin_class in filter(lambda x: not issubclass(x, WebDriver), self.__class__.__mro__):
            if hasattr(mixin_class, self._addCommands.__name__):
                getattr(mixin_class, self._addCommands.__name__, None)(self)

        self.command_executor._commands[Command.TOUCH_ACTION] = ('POST', '/session/$sessionId/touch/perform')
        self.command_executor._commands[Command.MULTI_ACTION] = ('POST', '/session/$sessionId/touch/multi/perform')
        self.command_executor._commands[Command.SET_IMMEDIATE_VALUE] = (
            'POST',
            '/session/$sessionId/appium/element/$id/value',
        )

        # TODO Move commands for element to webelement
        self.command_executor._commands[Command.REPLACE_KEYS] = (
            'POST',
            '/session/$sessionId/appium/element/$id/replace_value',
        )
        self.command_executor._commands[Command.CLEAR] = ('POST', '/session/$sessionId/element/$id/clear')
        self.command_executor._commands[Command.LOCATION_IN_VIEW] = (
            'GET',
            '/session/$sessionId/element/$id/location_in_view',
        )

        # override for Appium 1.x
        # Appium 2.0 and Appium 1.22 work with `/se/log` and `/se/log/types`
        self.command_executor._commands[Command.GET_LOG] = ('POST', '/session/$sessionId/log')
        self.command_executor._commands[Command.GET_AVAILABLE_LOG_TYPES] = ('GET', '/session/$sessionId/log/types')
