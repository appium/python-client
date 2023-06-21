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

from typing import Any

from appium.options.common.supports_capabilities import SupportsCapabilities


class SafariOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: Any, cls: Any) -> Any:
        return getattr(obj, "get_capabilities")(self.name)

    def __set__(self, obj: Any, value: Any) -> Any:
        getattr(obj, "set_capabilities")(self.name, value)


class AutomaticInspectionOption(SupportsCapabilities):
    AUTOMATIC_INSPECTION = 'safari:automaticInspection'
    automatic_inspection = SafariOptionsDescriptor("AUTOMATIC_INSPECTION")


class AutomaticProfilingOption(SupportsCapabilities):
    AUTOMATIC_PROFILING = 'safari:automaticProfiling'
    automatic_profiling = SafariOptionsDescriptor("AUTOMATIC_PROFILING")


class DeviceNameOption(SupportsCapabilities):
    DEVICE_NAME = 'safari:deviceName'
    device_name = SafariOptionsDescriptor("DEVICE_NAME")


class DeviceTypeOption(SupportsCapabilities):
    DEVICE_TYPE = 'safari:deviceType'
    device_type = SafariOptionsDescriptor("DEVICE_TYPE")


class DeviceUdidOption(SupportsCapabilities):
    DEVICE_UDID = 'safari:deviceUDID'
    device_udid = SafariOptionsDescriptor("DEVICE_UDID")

class PlatformBuildVersionOption(SupportsCapabilities):
    PLATFORM_BUILD_VERSION = 'safari:platformBuildVersion'
    platform_build_version = SafariOptionsDescriptor("PLATFORM_BUILD_VERSION")


class PlatformVersionOption(SupportsCapabilities):
    PLATFORM_VERSION = 'safari:platformVersion'
    platform_version = SafariOptionsDescriptor("PLATFORM_VERSION")


class UseSimulatorOption(SupportsCapabilities):
    USE_SIMULATOR = 'safari:useSimulator'
    use_simulator = SafariOptionsDescriptor("USE_SIMULATOR")

class WebkitWebrtcOption(SupportsCapabilities):
    WEBKIT_WEBRTC = 'webkit:WebRTC'
    webkit_webrtc = SafariOptionsDescriptor("WEBKIT_WEBRTC")