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

from typing import Any, TypeVar, Generic

from appium.options.common.supports_capabilities import SupportsCapabilities

T = TypeVar('T')
C = TypeVar('C', bound='SupportsCapabilities')


class SafariOptionsDescriptor(Generic[T]):
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: C, cls: type[C]) -> Any:
        return obj.get_capability(self.name)

    def __set__(self, obj: C, value: Any) -> C:
        return obj.set_capability(self.name, value)


class AutomaticInspectionOption(SupportsCapabilities):
    AUTOMATIC_INSPECTION = 'safari:automaticInspection'
    automatic_inspection = SafariOptionsDescriptor('AUTOMATIC_INSPECTION')
    """
    This capability instructs Safari to preload the Web Inspector and JavaScript
    debugger in the background prior to returning a newly-created window.
    To pause the test's execution in JavaScript and bring up Web Inspector's
    Debugger tab, you can simply evaluate a debugger statement in the test page.

    Usage
    ----
    - `self.automatic_inspection`
    - `self.automatic_inspection` = `value`
    """


class AutomaticProfilingOption(SupportsCapabilities):
    AUTOMATIC_PROFILING = 'safari:automaticProfiling'
    automatic_profiling = SafariOptionsDescriptor('AUTOMATIC_PROFILING')
    """
    This capability instructs Safari to preload the Web Inspector and start
    a Timeline recording in the background prior to returning a newly-created
    window. To view the recording, open the Web Inspector through Safari's
    Develop menu.

    Usage
    -----
    - `self.automatic_profiling`
    - `self.automatic_profiling` = `value`
    """


class DeviceNameOption(SupportsCapabilities):
    DEVICE_NAME = 'safari:deviceName'
    device_name = SafariOptionsDescriptor('DEVICE_NAME')
    """
    safaridriver will only create a session using hosts whose device name
    matches the value of safari:deviceName. Device names are compared
    case-insensitively. NOTE: Device names for connected devices are shown in
    iTunes. If Xcode is installed, device names for connected devices are available
    via the output of instruments(1) and in the Devices and Simulators window
    (accessed in Xcode via "Window -&gt; Devices and Simulators").

    Usage
    -----
    - `self.device_name`
    - `self.device_name` = `value`
    """


class DeviceTypeOption(SupportsCapabilities):
    DEVICE_TYPE = 'safari:deviceType'
    device_type = SafariOptionsDescriptor('DEVICE_TYPE')
    """
    If the value of safari:deviceType is 'iPhone', safaridriver will only create a session
    using an iPhone device or iPhone simulator. If the value of safari:deviceType is 'iPad',
    safaridriver will only create a session using an iPad device or iPad simulator.
    Values of safari:deviceType are compared case-insensitively.

    Usage
    -----
    - `self.device_type`
    - `self.device_type` = `value`
    """


class DeviceUdidOption(SupportsCapabilities):
    DEVICE_UDID = 'safari:deviceUDID'
    device_udid = SafariOptionsDescriptor('DEVICE_UDID')
    """
    safaridriver will only create a session using hosts whose device UDID
    matches the value of safari:deviceUDID. Device UDIDs are compared
    case-insensitively. NOTE: If Xcode is installed, UDIDs for connected
    devices are available via the output of instruments(1) and in the
    Devices and Simulators window (accessed in Xcode via
    "Window -&gt; Devices and Simulators").

    Usage
    ----
    - `self.device_udid`
    - `self.device_udid` = `value`
    """

class PlatformBuildVersionOption(SupportsCapabilities):
    PLATFORM_BUILD_VERSION = 'safari:platformBuildVersion'
    platform_build_version = SafariOptionsDescriptor('PLATFORM_BUILD_VERSION')
    """
    safaridriver will only create a session using hosts whose OS build
    version matches the value of safari:platformBuildVersion. Example
    of a macOS build version is '18E193'. On macOS, the OS build version
    can be determined by running the sw_vers(1) utility.

    Usage
    -----
    - `self.platform_build_version`
    - `self.platform_build_version` = `value`
    """


class PlatformVersionOption(SupportsCapabilities):
    PLATFORM_VERSION = 'safari:platformVersion'
    platform_version = SafariOptionsDescriptor('PLATFORM_VERSION')
    """
    safaridriver will only create a session using hosts whose OS
    version matches the value of safari:platformVersion. OS version
    numbers are prefix-matched. For example, if the value of safari:platformVersion
    is '12', this will allow hosts with an OS version of '12.0' or '12.1' but not '10.12'.

    Usage
    ----
    - `self.platform_version`
    - `self.platform_version` = `value`
    """


class UseSimulatorOption(SupportsCapabilities):
    USE_SIMULATOR = 'safari:useSimulator'
    use_simulator = SafariOptionsDescriptor('USE_SIMULATOR')
    """
     If the value of safari:useSimulator is true, safaridriver will only use
    iOS Simulator hosts. If the value of safari:useSimulator is false, safaridriver
    will not use iOS Simulator hosts. NOTE: An Xcode installation is required
    in order to run WebDriver tests on iOS Simulator hosts.

    Usage
    -----
    - `self.use_simulator`
    - `self.use_simulator` = `value`
    """

class WebkitWebrtcOption(SupportsCapabilities):
    WEBKIT_WEBRTC = 'webkit:WebRTC'
    webkit_webrtc = SafariOptionsDescriptor('WEBKIT_WEBRTC')
    """
    This option allows a test to temporarily change Safari's policies
    for WebRTC and Media Capture.
    The following dictionary values are supported:
    - DisableInsecureMediaCapture: Boolean value.
    Normally, Safari refuses to allow media capture over insecure connections.
    This restriction is relaxed by default for WebDriver sessions for testing
    purposes (for example, a test web server not configured for HTTPS). When
    this capability is specified, Safari will revert to the normal behavior of
    preventing media capture over insecure connections.
    - DisableICECandidateFiltering: Boolean value.
    To protect a user's privacy, Safari normally filters out WebRTC
    ICE candidates that correspond to internal network addresses when
    capture devices are not in use. This capability suppresses ICE candidate
    filtering so that both internal and external network addresses are
    always sent as ICE candidates.

    Usage
    -----
    - `self.webkit_webrtc`
    - `self.webkit_webrtc` = `value`
    """