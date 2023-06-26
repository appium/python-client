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


class AdbOptionsDescriptor(Generic[T]):
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: C, cls: type[C]) -> Any:
        if self.name == 'ADB_EXEC_TIMEOUT':
            value = obj.get_capability(self.name)
            return None if value is None else timedelta(milliseconds=value)
        return obj.get_capability(self.name)

    def __set__(self, obj: C, value: Any) -> C:
        if self.name == 'ADB_EXEC_TIMEOUT':
            return obj.set_capability(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)    
        return obj.set_capability(self.name, value)


class AdbExecTimeoutOption(SupportsCapabilities):
    ADB_EXEC_TIMEOUT = 'adbExecTimeout'
    adb_exec_timeout = AdbOptionsDescriptor('ADB_EXEC_TIMEOUT')
    """
    Gets and Sets Maximum time to wait until single ADB command is executed.
    20000 ms by default.

    Usage
    -----
    - `self.adb_exec_timeout`
    - `self.adb_exec_timeout` = `value`
    """


class AdbPortOption(SupportsCapabilities):
    ADB_PORT = 'adbPort'
    adb_port = AdbOptionsDescriptor('ADB_PORT')
    """
    Set number of the port where ADB is running. 5037 by default

    Usage
    -----
    - `self.adb_port`
    - `self.adb_port` = `value`
    """


class AllowDelayAdbOption(SupportsCapabilities):
    ALLOW_DELAY_ADB = 'allowDelayAdb'
    allow_delay_adb = AdbOptionsDescriptor('ALLOW_DELAY_ADB')
    """
    Gets and Sets whether to prevent the emulator to use -delay-adb feature.
    Being set to false prevents emulator to use -delay-adb feature to detect its startup.
    See https://github.com/appium/appium/issues/14773 for more details.

    Usage
    ----
    - `self.allow_delay_adb`
    - `self.allow_delay_adb` = `value`
    """


class BuildToolsVersionOption(SupportsCapabilities):
    BUILD_TOOLS_VERSION = 'buildToolsVersion'
    build_tools_version = AdbOptionsDescriptor('BUILD_TOOLS_VERSION')
    """
    Gets and Sets Version of Android build tools to use.
    The version of Android build tools to use. By default, UiAutomator2
    driver uses the most recent version of build tools installed on
    the machine, but sometimes it might be necessary to give it a hint
    (let say if there is a known bug in the most recent tools version).
    Example: 28.0.3

    Usage
    -----
    - `self.build_tools_version`
    - `self.build_tools_version` = `value`
    """


class ClearDeviceLogsOnStartOption(SupportsCapabilities):
    CLEAR_DEVICE_LOGS_ON_START = 'clearDeviceLogsOnStart'
    clear_device_logs_on_start = AdbOptionsDescriptor('CLEAR_DEVICE_LOGS_ON_START')
    """"
    Gets and Sets if the driver to delete all the existing logs in the
    device buffer before starting a new test.
    If set to true then the driver deletes all the existing logs in the
    device buffer before starting a new test.

    Usage
    ----
    - `self.clear_device_logs_on_start`
    - `self.clear_device_logs_on_start` = `value`
    """


class IgnoreHiddenApiPolicyErrorOption(SupportsCapabilities):
    IGNORE_HIDDEN_API_POLICY_ERROR = 'ignoreHiddenApiPolicyError'
    ignore_hidden_api_policy_error = AdbOptionsDescriptor('IGNORE_HIDDEN_API_POLICY_ERROR')
    """
    Gets and Sets Whether to ignore a failure while changing hidden API access policies.
    Being set to true ignores a failure while changing hidden API access policies.
    Could be useful on some devices, where access to these policies has been locked by its vendor.
    false by default.

    Usage
    -----
    - `self.ignore_hidden_api_ploicy_error`
    - `self.ignore_hidden_api_ploicy_error` = `value`
    """


class LogcatFilterSpecsOption(SupportsCapabilities):
    LOGCAT_FILTER_SPECS = 'logcatFilterSpecs'
    logcat_filter_specs = AdbOptionsDescriptor('LOGCAT_FILTER_SPECS')
    """
    Gets and Sets Logcat filter format.
    Series of tag[:priority] where tag is a log component tag (or * for all)
    and priority is: V Verbose, D Debug, I Info, W Warn, E Error, F Fatal,
    S Silent (supress all output). '' means ':d' and tag by itself means tag:v.
    If not specified on the commandline, filterspec is set from ANDROID_LOG_TAGS.
    If no filterspec is found, filter defaults to '*:I'.

    Usage
    -----
    - `self.logcat_filter_specs`
    - `self.logcat_filter_specs` = `value`
    """


class LogcatFormatOption(SupportsCapabilities):
    LOGCAT_FORMAT = 'logcatFormat' 
    logcat_format = AdbOptionsDescriptor('LOGCAT_FORMAT')
    """
    Gets and Sets Log print format.
    The log print format, where format is one of: brief process tag thread raw time
    threadtime long. threadtime is the default value.

    Usage
    ----
    - `self.logcat_format`
    - `self.logcat_format` = `value`
    """


class MockLocationAppOption(SupportsCapabilities):
    MOCK_LOCATION_APP = 'mockLocationApp'
    mock_location_app = AdbOptionsDescriptor('MOCK_LOCATION_APP')
    """
    Gets and Sets Identifier of the app, which is used as a system mock location provider.

    This capability has no effect on emulators.
    If the value is set to null or an empty string, then Appium will skip the mocked
    location provider setup procedure. Defaults to Appium Setting package
    identifier (io.appium.settings).

    Usage
    ----
    - `self.mock_location_app`
    - `self.mock_location_app` = `value`
    """


class RemoteAdbHostOption(SupportsCapabilities):
    REMOTE_ADB_HOST = 'remoteAdbHost'
    remote_adb_host = AdbOptionsDescriptor('REMOTE_ADB_HOST')
    """
    Gets and Sets Address of the host where ADB is running.
    (the value of -H ADB command line option).Localhost by default.

    Usage
    ----
    - `self.remote_adb_host`
    - `self.remote_adb_host` = `value`
    """


class SkipLogcatCaptureOption(SupportsCapabilities):
    SKIP_LOGCAT_CAPTURE = 'skipLogcatCapture'
    skip_logcat_capture = AdbOptionsDescriptor('SKIP_LOGCAT_CAPTURE')
    """
    Whether to delete all the existing logs in the
    device buffer before starting a new test.
    Being set to true disables automatic logcat output collection during the test run.
    false by default

    Usage
    -----
    - `self.skip_logcat_capture`
    - `self.skip_logcat_capture` = `value`
    """


class SuppressKillServerOption(SupportsCapabilities):
    SUPPRESS_KILL_SERVER = 'suppressKillServer'
    suppress_kill_server = AdbOptionsDescriptor('SUPPRESS_KILL_SERVER')
    """
    Prevents the driver from ever killing the ADB server explicitly.
    Being set to true prevents the driver from ever killing the ADB server explicitly.
    Could be useful if ADB is connected wirelessly. false by default.

    Usage
    -----
    - `self.suppress_kill_server`
    - `self.suppress_kill_server` = `value`
    """