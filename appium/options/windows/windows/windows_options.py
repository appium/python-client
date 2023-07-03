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
from typing import Optional, Union

from appium.options.base_options_descriptor import OptionsDescriptor
from appium.options.common.supports_capabilities import SupportsCapabilities
from appium.options.transformers import (
    transform_duration_get,
    transform_duration_in_seconds_get,
    transform_duration_in_seconds_set,
    transform_duration_set,
)


class AppArgumentsOption(SupportsCapabilities):
    APP_ARGUMENTS = "appArguments"
    app_arguments = OptionsDescriptor[Optional[str], str](APP_ARGUMENTS)
    """
    Set application arguments string, for example `/argone "/arg two"`.
    Make sure arguments are quoted/escaped properly if necessary:
    https://ss64.com/nt/syntax-esc.html

    Usage
    -----
    - Get
        - `self.app_arguments`
    - Set
        - `self.app_arguments` = `value`
    
    Parameters
    ----------
    `value`: `str`

    Returns
    -------
    - Get
        - `Optional[str]`
    - Set
        - `None`
    """


class AppTopLevelWindowOption(SupportsCapabilities):
    APP_TOP_LEVEL_WINDOW = "appTopLevelWindow"
    app_top_level_window = OptionsDescriptor[Optional[str], str](APP_TOP_LEVEL_WINDOW)
    """
    Set the hexadecimal handle of an existing application top level
    window to attach to, for example 0x12345 (should be of string type).
    Either this capability or app one must be provided on session startup.

    Usage
    -----
    - Get
        - `self.app_top_level_window`
    - Set
        - `self.app_top_level_window` = `value`
    
    Parameters
    ----------
    `value`: `str`

    Returns
    -------
    - Get
        - `Optional[str]`
    - Set
        - `None`
    """


class AppWorkingDirOption(SupportsCapabilities):
    APP_WORKING_DIR = "appWorkingDir"
    app_working_dir = OptionsDescriptor[Optional[str], str](APP_WORKING_DIR)
    """
    Set the full path to the folder, which is going to be set as the working
    dir for the application under test. This is only applicable for classic apps.

    Usage
    -----
    - Get
        - `self.app_working_dir`
    - Set
        - `self.app_working_dir` = `value`
    
    Parameters
    ----------
    `value`: `str`

    Returns
    -------
    - Get
        - `Optional[str]`
    - Set
        - `None`
    """


class CreateSessionTimeoutOption(SupportsCapabilities):
    CREATE_SESSION_TIMEOUT = "createSessionTimeout"
    create_session_timeout = OptionsDescriptor[Optional[timedelta], Union[timedelta, int]](
        CREATE_SESSION_TIMEOUT, transform_duration_get, transform_duration_set
    )
    """
    Set the timeout used to retry Appium Windows Driver session startup.
    This capability could be used as a workaround for the long startup times
    of UWP applications (aka Failed to locate opened application window
    with appId: TestCompany.my_app4!App, and processId: 8480).

    Usage
    -----
    - Get
        - `self.create_session_timeout`
    - Set
        - `self.create_session_timeout` = `value`
    
    Parameters
    ----------
    `value`: `Union[timedelta, int]`

    Returns
    -------
    - Get
        - `Optional[timedelta]`
    - Set
        - `None`
    """


class ExperimentalWebDriverOption(SupportsCapabilities):
    EXPERIMENTAL_WEB_DRIVER = "ms:experimental-webdriver"
    experimental_webdriver = OptionsDescriptor[Optional[bool], bool](EXPERIMENTAL_WEB_DRIVER)
    """
    Enables experimental features and optimizations. See Appium Windows
    Driver release notes for more details on this capability.

    Usage
    -----
    - Get
        - `self.experimental_webdriver`
    - Set
        - `self.experimental_webdriver` = `value`
    
    Parameters
    ----------
    `value`: `bool`

    Returns
    -------
    - Get
        - `Optional[bool]`
    - Set
        - `None`
    """


class WaitForAppLaunchOption(SupportsCapabilities):
    WAIT_FOR_APP_LAUNCH = "ms:waitForAppLaunch"
    wait_for_app_launch = OptionsDescriptor[Optional[timedelta], Union[timedelta, int]](
        WAIT_FOR_APP_LAUNCH, transform_duration_in_seconds_get, transform_duration_in_seconds_set
    )
    """
    Similar to createSessionTimeout, but is
    applied on the server side. Enables Appium Windows Driver to wait for
    a defined amount of time after an app launch is initiated prior to
    attaching to the application session. The limit for this is 50 seconds.

    Usage
    -----
    - Get
        - `self.wait_for_app_launch`
    - Set
        - `self.wait_for_app_launch` = `value`
    
    Parameters
    ----------
    `value`: `Union[timedelta, int]`

    Returns
    -------
    - Get
        - `Optional[timedelta]`
    - Set
        - `None`
    """
