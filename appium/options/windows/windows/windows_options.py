# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from datetime import timedelta
from typing import Any, TypeVar

from appium.options.common.supports_capabilities import SupportsCapabilities

C = TypeVar('C', bound='SupportsCapabilities')


class WindowsOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: C, cls: type[C]) -> Any:
        return getattr(obj, 'get_capability')(self.name)

    def __set__(self, obj: C, value: Any) -> C:
        if self.name in ('CREATE_SESSION_TIMEOUT', 'WAIT_FOR_APP_LAUNCH'):
            return getattr(obj, 'set_capability')(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)    
        return getattr(obj, 'set_capability')(self.name, value)


class AppArgumentsOption(SupportsCapabilities):
    APP_ARGUMENTS = 'appArguments'
    app_arguments = WindowsOptionsDescriptor("APP_ARGUMENTS")
    """
    Set application arguments string, for example `/argone "/arg two"`.
    Make sure arguments are quoted/escaped properly if necessary:
    https://ss64.com/nt/syntax-esc.html

    Usage
    -----
    - `self.app_arguments`
    - `self.app_arguments` = `value`
    """


class AppTopLevelWindowOption(SupportsCapabilities):
    APP_TOP_LEVEL_WINDOW = 'appTopLevelWindow'
    app_top_level_window = WindowsOptionsDescriptor('APP_TOP_LEVEL_WINDOW')
    """
    Set the hexadecimal handle of an existing application top level
    window to attach to, for example 0x12345 (should be of string type).
    Either this capability or app one must be provided on session startup.

    Usage
    -----
    - `self.app_top_level_window`
    - `self.app_top_level_window` = `value`
    """


class AppWorkingDirOption(SupportsCapabilities):
    APP_WORKING_DIR = 'appWorkingDir'
    app_working_dir = WindowsOptionsDescriptor('APP_WORKING_DIR')
    """
    Set the full path to the folder, which is going to be set as the working
    dir for the application under test. This is only applicable for classic apps.

    Usage
    -----
    - `self.app_working_dir`
    - `self.app_working_dir` = `value`
    """


class CreateSessionTimeoutOption(SupportsCapabilities):
    CREATE_SESSION_TIMEOUT = 'createSessionTimeout'
    create_session_timeout = WindowsOptionsDescriptor('CREATE_SESSION_TIMEOUT')
    """
    Set the timeout used to retry Appium Windows Driver session startup.
    This capability could be used as a workaround for the long startup times
    of UWP applications (aka Failed to locate opened application window
    with appId: TestCompany.my_app4!App, and processId: 8480).

    Usage
    -----
    - `self.create_session_timeout`
    - `self.create_session_timeout` = `value`
    """


class ExperimentalWebDriverOption(SupportsCapabilities):
    EXPERIMENTAL_WEB_DRIVER = 'ms:experimental-webdriver'
    experimental_webdriver = WindowsOptionsDescriptor('EXPERIMENTAL_WEB_DRIVER')
    """
    Enables experimental features and optimizations. See Appium Windows
    Driver release notes for more details on this capability.

    Usage
    -----
    - `self.experimental_webdriver`
    - `self.experimental_webdriver` = `value`
    """


class WaitForAppLaunchOption(SupportsCapabilities):
    WAIT_FOR_APP_LAUNCH = 'ms:waitForAppLaunch'
    wait_for_app_launch = WindowsOptionsDescriptor('WAIT_FOR_APP_LAUNCH')
    """
    Similar to createSessionTimeout, but is
    applied on the server side. Enables Appium Windows Driver to wait for
    a defined amount of time after an app launch is initiated prior to
    attaching to the application session. The limit for this is 50 seconds.

    Usage
    -----
    - `self.wait_for_app_launch`
    - `self.wait_for_app_launch` = `value`
    """