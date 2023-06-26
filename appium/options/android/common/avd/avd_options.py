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
from typing import Any, TypeVar, Generic

from appium.options.common.supports_capabilities import SupportsCapabilities

T = TypeVar('T')
C = TypeVar('C', bound='SupportsCapabilities')


class AvdOptionsDescriptor(Generic[T]):
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: C, cls: type[C]) -> Any:
        if self.name in ('AVD_LAUNCH_TIMEOUT', 'AVD_READY_TIMEOUT'):
            value = obj.get_capability(self.name)
            return None if value is None else timedelta(milliseconds=value)
        return obj.get_capability(self.name)

    def __set__(self, obj: C, value: Any) -> C:
        if self.name in ('AVD_LAUNCH_TIMEOUT', 'AVD_READY_TIMEOUT'):
            return obj.get_capability(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)    
        return obj.get_capability(self.name, value)


class AvdArgsOption(SupportsCapabilities):
    AVD_ARGS = 'avdArgs'
    avd_args = AvdOptionsDescriptor('AVD_ARGS')
    """
    Gets and Sets emulator command line arguments.

    Usage
    - `self.avd_args`
    - `self.avd_args` = `value`
    """


class AvdEnvOption(SupportsCapabilities):
    AVD_ENV = 'avdEnv'
    avd_env = AvdOptionsDescriptor('AVD_ENV')
    """
    Gets and Sets the mapping of emulator environment variables.

    Usage
    ----
    - `self.avd_env`
    - `self.avd_env` = `value`
    """


class AvdLaunchTimeoutOption(SupportsCapabilities):
    AVD_LAUNCH_TIMEOUT = 'avdLaunchTimeout'
    avd_launch_timeout = AvdOptionsDescriptor('AVD_LAUNCH_TIMEOUT')
    """
    Timeout to wait until Android Emulator is started.
    Maximum timeout to wait until Android Emulator is started.
    60000 ms by default.

    Usage
    -----
    - `self.avd_launch_timeout`
    - `self.avd_launch_timeout` = `value`
    """


class AvdOption(SupportsCapabilities):
    AVD = 'avd'
    avd = AvdOptionsDescriptor('AVD')
    """
    The name of Android emulator to run the test on.
    Names of currently installed emulators could be listed using
    avdmanager list avd command. If the emulator with the given name
    is not running then it is going to be started before a test.

    Usage
    -----
    - `self.avd`
    - `self.avd` = `value`
    """

class AvdReadyTimeoutOption(SupportsCapabilities):
    AVD_READY_TIMEOUT = 'avdReadyTimeout'
    avd_ready_timeout = AvdOptionsDescriptor('AVD_READY_TIMEOUT')
    """
    Maximum timeout to wait until Android Emulator is fully booted and is ready for usage.
    60000 ms by default

    Usage
    -----
    - `self.avd_ready_timeout`
    - `self.avd_ready_timeout` = `value`
    """


class GpsEnabledOption(SupportsCapabilities):
    GPS_ENABLED = 'gpsEnabled'
    gps_enabled = AvdOptionsDescriptor('GPS_ENABLED')
    """
    Gets and Sets whether to enable (true) or disable (false) GPS service in the Emulator.
    Unset by default, which means to not change the current value.

    Usage
    -----
    - `self.gps_enabled`
    - `self.gps_enabled` = `value`
    """


class NetworkSpeedOption(SupportsCapabilities):
    NETWORK_SPEED = 'networkSpeed'
    network_speed = AvdOptionsDescriptor('NETWORK_SPEED')
    """
    Gets and Sets the desired network speed limit for the emulator.
    It is only applied if the emulator is not running before
    the test starts. See emulator command line arguments description
    for more details.

    Usage
    -----
    - `self.network_speed`
    - `self.network_speed` = `value`
    """