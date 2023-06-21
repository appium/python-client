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
from typing import Optional, Any

from appium.options.common.supports_capabilities import SupportsCapabilities


class AvdOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: Any, cls: Any) -> Any:
        if self.name in ("AVD_LAUNCH_TIMEOUT", "AVD_READY_TIMEOUT"):
            value = getattr(obj, "get_capabilities")(self.name)
            return None if value is None else timedelta(milliseconds=value)
        return getattr(obj, "get_capabilities")(self.name)

    def __set__(self, obj: Any, value: Any) -> Any:
        if self.name in ("AVD_LAUNCH_TIMEOUT", "AVD_READY_TIMEOUT"):
            getattr(obj, "set_capabilities")(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)    
        getattr(obj, "set_capabilities")(self.name, value)


class AvdArgsOption(SupportsCapabilities):
    AVD_ARGS = 'avdArgs'
    avd_args = AvdOptionsDescriptor("AVD_ARGS")


class AvdEnvOption(SupportsCapabilities):
    AVD_ENV = 'avdEnv'
    avd_env = AvdOptionsDescriptor("AVD_ENV")


class AvdLaunchTimeoutOption(SupportsCapabilities):
    AVD_LAUNCH_TIMEOUT = 'avdLaunchTimeout'
    avd_launch_timeout = AvdOptionsDescriptor("AVD_LAUNCH_TIMEOUT")


class AvdOption(SupportsCapabilities):
    AVD = 'avd'
    avd = AvdOptionsDescriptor("AVD")

class AvdReadyTimeoutOption(SupportsCapabilities):
    AVD_READY_TIMEOUT = 'avdReadyTimeout'
    avd_ready_timeout = AvdOptionsDescriptor("AVD_READY_TIMEOUT")


class GpsEnabledOption(SupportsCapabilities):
    GPS_ENABLED = 'gpsEnabled'
    gps_enabled = AvdOptionsDescriptor("GPS_ENABLED")


class NetworkSpeedOption(SupportsCapabilities):
    NETWORK_SPEED = 'networkSpeed'
    network_speed = AvdOptionsDescriptor("NETWORK_SPEED")
