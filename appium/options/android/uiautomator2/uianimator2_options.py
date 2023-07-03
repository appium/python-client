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
from appium.options.transformers import transform_duration_get, transform_duration_set


class DisableWindowAnimationOption(SupportsCapabilities):
    DISABLE_WINDOWS_ANIMATION = "disableWindowAnimation"
    disable_window_animation = OptionsDescriptor[Optional[bool], bool](DISABLE_WINDOWS_ANIMATION)
    """
    Gets and Sets whether to disable window animations when starting the instrumentation process.
    false by default

    Usage
    -----
    - Get
        - `self.disable_window_animation`
    
    - Set
        - `self.disable_window_animation` = `value`
    
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


class MjpegServerPortOption(SupportsCapabilities):
    MJPEG_SERVER_PORT = "mjpegServerPort"
    mjpeg_server_port = OptionsDescriptor[Optional[int], int](MJPEG_SERVER_PORT)
    """
    Gets and Sets The number of the port UiAutomator2 server starts the MJPEG server on.
    If not provided then the screenshots broadcasting service on the remote
    device does not get exposed to a local port (e.g. no adb port forwarding
    is happening).

    Usage
    -----
    - Get
        - `self.mjpeg_server_port`
    - Set
        - `self.mjpeg_server_port` = `value`
    
    Parameters
    ----------
    `value`: `int`

    Returns
    -------
    - Get
        - `Optional[int]`
    - Set
        - `None`
    """


class SkipDeviceInitializationOption(SupportsCapabilities):
    SKIP_DEVICE_INITIALIZATION = "skipDeviceInitialization"
    skip_device_initialization = OptionsDescriptor[Optional[bool], bool](SKIP_DEVICE_INITIALIZATION)
    """
    Gets and Sets if the device  is ready and whether
    Settings app is installed will be canceled on session creation.
    Could speed up the session creation if you know what you are doing. false by default

    Usage
    -----
    - Get
        - `self.skip_device_initialization`
    - Set
        - `self.skip_device_initialization` = `value`

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


class SkipServerInstallationOption(SupportsCapabilities):
    SKIP_SERVER_INSTALLATION = "skipServerInstallation"
    skip_server_installation = OptionsDescriptor[Optional[bool], bool](SKIP_SERVER_INSTALLATION)
    """
    Gets and Sets whether to skip the server components installation
    on the device under test and all the related checks.
    This could help to speed up the session startup if you know for sure the
    correct server version is installed on the device.
    In case the server is not installed or an incorrect version of it is installed
    then you may get an unexpected error later.

    Usage
    -----
    - Get
        - `self.skip_server_installation`
    - Set
        - `self.skip_server_installation` = `value`
    
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


class Uiautomator2ServerInstallTimeoutOption(SupportsCapabilities):
    UIAUTOMATOR2_SERVER_INSTALL_TIMEOUT = "uiautomator2ServerInstallTimeout"
    uiautomator2_server_install_timeout = OptionsDescriptor[Optional[timedelta], Union[timedelta, int]]
    (UIAUTOMATOR2_SERVER_INSTALL_TIMEOUT, transform_duration_get, transform_duration_set)
    """
    Gets and Sets the maximum timeout to wait util UiAutomator2 server is installed on the device.
    20000 ms by default

    Usage
    -----
    - Get
        - `self.uiautomator2_server_install_timeout`
    - Set
        - `self.uiautomator2_server_install_timeout` = `value`
    
    Parameters
    ----------
    `value`: `Union[timedelta, int]`
    """


class Uiautomator2ServerLaunchTimeoutOption(SupportsCapabilities):
    UIAUTOMATOR2_SERVER_LAUNCH_TIMEOUT = "uiautomator2ServerLaunchTimeout"
    uiautomator2_server_launch_timeout = OptionsDescriptor[Optional[timedelta], Union[timedelta, int]]
    (UIAUTOMATOR2_SERVER_LAUNCH_TIMEOUT, transform_duration_get, transform_duration_set)
    """
    Set the maximum timeout to wait util UiAutomator2Server is listening on
    the device. 30000 ms by default

    Usage
    -----
    - Get
        - `self.uiautomator2_server_launch_timeout`
    - Set
        - `self.uiautomator2_server_launch_timeout` = `value`
    
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


class Uiautomator2ServerReadTimeoutOption(SupportsCapabilities):
    UIAUTOMATOR2_SERVER_READ_TIMEOUT = "uiautomator2ServerReadTimeout"
    uiautomator2_server_read_timeout = OptionsDescriptor[Optional[timedelta], Union[timedelta, int]]
    (UIAUTOMATOR2_SERVER_READ_TIMEOUT, transform_duration_get, transform_duration_set)
    """
    Set the maximum timeout to wait for a HTTP response from UiAutomator2Server.
    Only values greater than zero are accepted. If the given value is too low
    then expect driver commands to fail with timeout of Xms exceeded error.
    240000 ms by default

    Usage
    -----
    - Get
        - `self.uiautomator2_server_read_timeout`
    - Set
        - `self.uiautomator2_server_read_timeout` = `value`
    
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
