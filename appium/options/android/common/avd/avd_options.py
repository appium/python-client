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

from typing import Optional, Union, Dict
from datetime import timedelta

from appium.options.common.supports_capabilities import SupportsCapabilities

from appium.options.base_options_descriptor import OptionsDescriptor
from appium.options.transformers import transform_duration_get, transform_duration_set


class AvdArgsOption(SupportsCapabilities):
    AVD_ARGS = 'avdArgs'
    avd_args = OptionsDescriptor[Optional[str], str](AVD_ARGS)
    """
    Gets and Sets emulator command line arguments.

    Usage
    -----
    - Get
        - `self.avd_args`
    - Set
        - `self.avd_args` = `value`
    
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


class AvdEnvOption(SupportsCapabilities):
    AVD_ENV = 'avdEnv'
    avd_env = OptionsDescriptor[Optional[Dict[str, str]], str](AVD_ENV)
    """
    Gets and Sets the mapping of emulator environment variables.

    Usage
    -----
    - Get
        - `self.avd_env`
    - Set
        - `self.avd_env` = `value`

    Parameters
    ----------
    `value`: `str`

    Returns
    -------
    - Get
        - `Optional[Dict[str, str]]`
    - Set
        - `None`
    """


class AvdLaunchTimeoutOption(SupportsCapabilities):
    AVD_LAUNCH_TIMEOUT = 'avdLaunchTimeout'
    avd_launch_timeout = OptionsDescriptor[Optional[timedelta], Union[timedelta, int]](AVD_LAUNCH_TIMEOUT)
    """
    Timeout to wait until Android Emulator is started.
    Maximum timeout to wait until Android Emulator is started.
    60000 ms by default.

    Usage
    -----
    - Get
        - `self.avd_launch_timeout`
    - Set
        - `self.avd_launch_timeout` = `value`
    
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


class AvdOption(SupportsCapabilities):
    AVD = 'avd'
    avd = OptionsDescriptor[Optional[str], str](AVD)
    """
    The name of Android emulator to run the test on.
    Names of currently installed emulators could be listed using
    avdmanager list avd command. If the emulator with the given name
    is not running then it is going to be started before a test.

    Usage
    -----
    - Get
        - `self.avd`
    - Set
        - `self.avd` = `value`
    
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

class AvdReadyTimeoutOption(SupportsCapabilities):
    AVD_READY_TIMEOUT = 'avdReadyTimeout'
    avd_ready_timeout = OptionsDescriptor[Optional[timedelta], Union[timedelta, int]](
        AVD_READY_TIMEOUT, 
        transform_duration_get, 
        transform_duration_set
    )
    """
    Maximum timeout to wait until Android Emulator is fully booted and is ready for usage.
    60000 ms by default

    Usage
    -----
    - Get
        - `self.avd_ready_timeout`
    - Set
        - `self.avd_ready_timeout` = `value`
    
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


class GpsEnabledOption(SupportsCapabilities):
    GPS_ENABLED = 'gpsEnabled'
    gps_enabled = OptionsDescriptor[Optional[bool], bool](GPS_ENABLED)
    """
    Gets and Sets whether to enable (true) or disable (false) GPS service in the Emulator.
    Unset by default, which means to not change the current value.

    Usage
    -----
    - Get
        - `self.gps_enabled`
    - Set
        - `self.gps_enabled` = `value`
    
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


class NetworkSpeedOption(SupportsCapabilities):
    NETWORK_SPEED = 'networkSpeed'
    network_speed = OptionsDescriptor[Optional[str], str](NETWORK_SPEED)
    """
    Gets and Sets the desired network speed limit for the emulator.
    It is only applied if the emulator is not running before
    the test starts. See emulator command line arguments description
    for more details.

    Usage
    -----
    - Get
        - `self.network_speed`
    - Set
        - `self.network_speed` = `value`
    
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
