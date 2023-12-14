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

from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union

from selenium import webdriver
from selenium.common.exceptions import (
    InvalidArgumentException,
    SessionNotCreatedException,
    UnknownMethodException,
    WebDriverException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command as RemoteCommand
from selenium.webdriver.remote.remote_connection import RemoteConnection

from appium.common.logger import logger
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

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
from .extensions.keyboard import Keyboard
from .extensions.location import Location
from .extensions.log_event import LogEvent
from .extensions.remote_fs import RemoteFS
from .extensions.screen_record import ScreenRecord
from .extensions.session import Session
from .extensions.settings import Settings
from .mobilecommand import MobileCommand as Command
from .switch_to import MobileSwitchTo
from .webelement import WebElement as MobileWebElement


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
            options = AppiumOptions()
            driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options,
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
            element = driver.find_elemeent(by=AppiumBy.ACCESSIBILITY_ID, value='id')

            # Then, the driver calls a get request to `session/$sessionId/path/to/your/custom/$id/url`
            # with replacing the `$id` with the given `element.id`
            driver.custom_method_name(element.id)
    """

    def __init__(self, execute: Callable[[str, Dict], Dict[str, Any]]):
        self._execute = execute

    def execute(self, parameters: Union[Dict[str, Any], None] = None) -> Any:
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
    webdriver.Remote,
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
        command_executor: Union[str, AppiumConnection] = 'http://127.0.0.1:4444/wd/hub',
        keep_alive: bool = True,
        direct_connection: bool = True,
        extensions: Optional[List['WebDriver']] = None,
        strict_ssl: bool = True,
        options: Union[AppiumOptions, List[AppiumOptions], None] = None,
    ):
        if strict_ssl is False:
            # pylint: disable=E1101
            # noinspection PyPackageRequirements
            import urllib3

            # pylint: disable=E1101
            # noinspection PyPackageRequirements
            import urllib3.exceptions

            # noinspection PyUnresolvedReferences
            AppiumConnection.set_certificate_bundle_path(None)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        if isinstance(command_executor, str):
            command_executor = AppiumConnection(command_executor, keep_alive=keep_alive)

        super().__init__(
            command_executor=command_executor,
            options=options,
        )

        if hasattr(self, 'command_executor'):
            self._add_commands()

        self.error_handler = MobileErrorHandler()

        if direct_connection:
            self._update_command_executor(keep_alive=keep_alive)

        # add new method to the `find_by_*` pantheon
        By.IOS_UIAUTOMATION = AppiumBy.IOS_UIAUTOMATION
        By.IOS_PREDICATE = AppiumBy.IOS_PREDICATE
        By.IOS_CLASS_CHAIN = AppiumBy.IOS_CLASS_CHAIN
        By.ANDROID_UIAUTOMATOR = AppiumBy.ANDROID_UIAUTOMATOR
        By.ANDROID_VIEWTAG = AppiumBy.ANDROID_VIEWTAG
        By.WINDOWS_UI_AUTOMATION = AppiumBy.WINDOWS_UI_AUTOMATION
        By.ACCESSIBILITY_ID = AppiumBy.ACCESSIBILITY_ID
        By.IMAGE = AppiumBy.IMAGE
        By.CUSTOM = AppiumBy.CUSTOM

        self._absent_extensions: Set[str] = set()

        self._extensions = extensions or []
        for extension in self._extensions:
            instance = extension(self.execute)
            method_name = instance.method_name()
            if hasattr(WebDriver, method_name):
                logger.debug(f'Overriding the method \'{method_name}\'')

            # add a new method named 'instance.method_name()' and call it
            setattr(WebDriver, method_name, getattr(instance, method_name))
            method, url_cmd = instance.add_command()
            # noinspection PyProtectedMember
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

        assert self.caps, 'Driver capabilities must be defined'
        if not {direct_protocol, direct_host, direct_port, direct_path}.issubset(set(self.caps)):
            message = 'Direct connect capabilities from server were:\n'
            for key in [direct_protocol, direct_host, direct_port, direct_path]:
                message += f'{key}: \'{self.caps.get(key, "")}\' '
            logger.debug(message)
            return

        protocol = self.caps[direct_protocol]
        hostname = self.caps[direct_host]
        port = self.caps[direct_port]
        path = self.caps[direct_path]
        executor = f'{protocol}://{hostname}:{port}{path}'

        logger.debug('Updated request endpoint to %s', executor)
        # Override command executor.
        if isinstance(self.command_executor, AppiumConnection):  # type: ignore
            self.command_executor = AppiumConnection(executor, keep_alive=keep_alive)
        else:
            self.command_executor = RemoteConnection(executor, keep_alive=keep_alive)
        self._add_commands()

    # https://github.com/SeleniumHQ/selenium/blob/06fdf2966df6bca47c0ae45e8201cd30db9b9a49/py/selenium/webdriver/remote/webdriver.py#L277
    # noinspection PyAttributeOutsideInit
    def start_session(self, capabilities: Union[Dict, AppiumOptions], browser_profile: Optional[str] = None) -> None:
        """Creates a new session with the desired capabilities.

        Override for Appium

        Args:
            capabilities: Read https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md
             for more details.
            browser_profile: Browser profile
        """
        if not isinstance(capabilities, (dict, AppiumOptions)):
            raise InvalidArgumentException('Capabilities must be a dictionary or AppiumOptions instance')

        w3c_caps = AppiumOptions.as_w3c(capabilities) if isinstance(capabilities, dict) else capabilities.to_w3c()
        response = self.execute(RemoteCommand.NEW_SESSION, w3c_caps)
        # https://w3c.github.io/webdriver/#new-session
        if not isinstance(response, dict):
            raise SessionNotCreatedException(
                f'A valid W3C session creation response must be a dictionary. Got "{response}" instead'
            )
        # Due to a W3C spec parsing misconception some servers
        # pack the createSession response stuff into 'value' dictionary and
        # some other put it to the top level of the response JSON nesting hierarchy
        get_response_value: Callable[[str], Optional[Any]] = lambda key: response.get(key) or (
            response['value'].get(key) if isinstance(response.get('value'), dict) else None
        )
        session_id = get_response_value('sessionId')
        if not session_id:
            raise SessionNotCreatedException(
                f'A valid W3C session creation response must contain a non-empty "sessionId" entry. '
                f'Got "{response}" instead'
            )
        self.session_id = session_id
        self.caps = get_response_value('capabilities') or {}

    def get_status(self) -> Dict:
        """
        Get the Appium server status

        Usage:
            driver.get_status()
        Returns:
            Dict: The status information

        """
        return self.execute(Command.GET_STATUS)['value']

    def find_element(self, by: str = AppiumBy.ID, value: Union[str, Dict, None] = None) -> MobileWebElement:
        """
        Find an element given a AppiumBy strategy and locator

        Args:
            by: The strategy
            value: The locator

        Usage:
            driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='accessibility_id')

        Returns:
            `appium.webdriver.webelement.WebElement`: The found element

        """
        # We prefer to patch locators in the client code
        # Checking current context every time a locator is accessed could significantly slow down tests
        # Check https://github.com/appium/python-client/pull/724 before submitting any issue
        # if by == By.ID:
        #     by = By.CSS_SELECTOR
        #     value = '[id="%s"]' % value
        # elif by == By.TAG_NAME:
        #     by = By.CSS_SELECTOR
        # elif by == By.CLASS_NAME:
        #     by = By.CSS_SELECTOR
        #     value = ".%s" % value
        # elif by == By.NAME:
        #     by = By.CSS_SELECTOR
        #     value = '[name="%s"]' % value

        return self.execute(RemoteCommand.FIND_ELEMENT, {'using': by, 'value': value})['value']

    def find_elements(
        self, by: str = AppiumBy.ID, value: Union[str, Dict, None] = None
    ) -> Union[List[MobileWebElement], List]:
        """
        Find elements given a AppiumBy strategy and locator

        Args:
            by: The strategy
            value: The locator

        Usage:
            driver.find_elements(by=AppiumBy.ACCESSIBILITY_ID, value='accessibility_id')

        Returns:
            :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`: The found elements
        """
        # We prefer to patch locators in the client code
        # Checking current context every time a locator is accessed could significantly slow down tests
        # Check https://github.com/appium/python-client/pull/724 before submitting any issue
        # if by == By.ID:
        #     by = By.CSS_SELECTOR
        #     value = '[id="%s"]' % value
        # elif by == By.TAG_NAME:
        #     by = By.CSS_SELECTOR
        # elif by == By.CLASS_NAME:
        #     by = By.CSS_SELECTOR
        #     value = ".%s" % value
        # elif by == By.NAME:
        #     by = By.CSS_SELECTOR
        #     value = '[name="%s"]' % value

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

    @property
    def switch_to(self) -> MobileSwitchTo:
        """Returns an object containing all options to switch focus into

        Override for appium

        Returns:
            `appium.webdriver.switch_to.MobileSwitchTo`

        """

        return MobileSwitchTo(self)

    # MJSONWP for Selenium v4
    @property
    def orientation(self) -> str:
        """
        Gets the current orientation of the device
        :Usage:
            ::
                orientation = driver.orientation
        """
        return self.execute(Command.GET_SCREEN_ORIENTATION)['value']

    # MJSONWP for Selenium v4
    @orientation.setter
    def orientation(self, value: str) -> None:
        """
        Sets the current orientation of the device
        :Args:
         - value: orientation to set it to.
        :Usage:
            ::
                driver.orientation = 'landscape'
        """
        allowed_values = ['LANDSCAPE', 'PORTRAIT']
        if value.upper() in allowed_values:
            self.execute(Command.SET_SCREEN_ORIENTATION, {'orientation': value})
        else:
            raise WebDriverException('You can only set the orientation to \'LANDSCAPE\' and \'PORTRAIT\'')

    def assert_extension_exists(self, ext_name: str) -> 'WebDriver':
        """
        Verifies if the given extension is not present in the list of absent extensions
        for the given driver instance.
        This API is designed for private usage.

        :param ext_name: extension name
        :return: self instance for chaining
        :raise UnknownMethodException: If the extension has been marked as absent once
        """
        if ext_name in self._absent_extensions:
            raise UnknownMethodException()
        return self

    def mark_extension_absence(self, ext_name: str) -> 'WebDriver':
        """
        Marks the given extension as absent for the given driver instance.
        This API is designed for private usage.

        :param ext_name: extension name
        :return: self instance for chaining
        """
        logger.debug(f'Marking driver extension "{ext_name}" as absent for the current instance')
        self._absent_extensions.add(ext_name)
        return self

    def _add_commands(self) -> None:
        # call the overridden command binders from all mixin classes except for
        # appium.webdriver.webdriver.WebDriver and its sub-classes
        # https://github.com/appium/python-client/issues/342
        for mixin_class in filter(lambda x: not issubclass(x, WebDriver), self.__class__.__mro__):
            if hasattr(mixin_class, self._add_commands.__name__):
                get_atter = getattr(mixin_class, self._add_commands.__name__, None)
                if get_atter:
                    get_atter(self)

        # noinspection PyProtectedMember,PyUnresolvedReferences
        commands = self.command_executor._commands

        commands[Command.GET_STATUS] = ('GET', '/status')

        # FIXME: remove after a while as MJSONWP
        commands[Command.TOUCH_ACTION] = ('POST', '/session/$sessionId/touch/perform')
        commands[Command.MULTI_ACTION] = ('POST', '/session/$sessionId/touch/multi/perform')

        # TODO Move commands for element to webelement
        commands[Command.CLEAR] = ('POST', '/session/$sessionId/element/$id/clear')
        commands[Command.LOCATION_IN_VIEW] = (
            'GET',
            '/session/$sessionId/element/$id/location_in_view',
        )

        # MJSONWP for Selenium v4
        commands[Command.IS_ELEMENT_DISPLAYED] = ('GET', '/session/$sessionId/element/$id/displayed')
        commands[Command.GET_CAPABILITIES] = ('GET', '/session/$sessionId')

        commands[Command.GET_SCREEN_ORIENTATION] = ('GET', '/session/$sessionId/orientation')
        commands[Command.SET_SCREEN_ORIENTATION] = ('POST', '/session/$sessionId/orientation')

        # override for Appium 1.x
        # Appium 2.0 and Appium 1.22 work with `/se/log` and `/se/log/types`
        # FIXME: remove after a while
        commands[Command.GET_LOG] = ('POST', '/session/$sessionId/log')
        commands[Command.GET_AVAILABLE_LOG_TYPES] = ('GET', '/session/$sessionId/log/types')
