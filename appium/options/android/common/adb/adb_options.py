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
from typing import Any

from appium.options.common.supports_capabilities import SupportsCapabilities


class AdbOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: Any, cls: Any) -> Any:
        if self.name == "ADB_EXEC_TIMEOUT":
            value = getattr(obj, "get_capabilities")(self.name)
            return None if value is None else timedelta(milliseconds=value)
        return getattr(obj, "get_capabilities")(self.name)

    def __set__(self, obj: Any, value: Any) -> Any:
        if self.name == "ADB_EXEC_TIMEOUT":
            getattr(obj, "set_capabilities")(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)    
        getattr(obj, "set_capabilities")(self.name, value)


class AdbExecTimeoutOption(SupportsCapabilities):
    ADB_EXEC_TIMEOUT = 'adbExecTimeout'
    adb_exec_timeout = AdbOptionsDescriptor("ADB_EXEC_TIMEOUT")


class AdbPortOption(SupportsCapabilities):
    ADB_PORT = 'adbPort'
    adb_port = AdbOptionsDescriptor("ADB_PORT")


class AllowDelayAdbOption(SupportsCapabilities):
    ALLOW_DELAY_ADB = 'allowDelayAdb'
    allow_delay_adb = AdbOptionsDescriptor("ALLOW_DELAY_ADB")


class BuildToolsVersionOption(SupportsCapabilities):
    BUILD_TOOLS_VERSION = 'buildToolsVersion'
    build_tools_version = AdbOptionsDescriptor("BUILD_TOOLS_VERSION")


class ClearDeviceLogsOnStartOption(SupportsCapabilities):
    CLEAR_DEVICE_LOGS_ON_START = 'clearDeviceLogsOnStart'
    clear_device_logs_on_start = AdbOptionsDescriptor("CLEAR_DEVICE_LOGS_ON_START")


class IgnoreHiddenApiPolicyErrorOption(SupportsCapabilities):
    IGNORE_HIDDEN_API_POLICY_ERROR = 'ignoreHiddenApiPolicyError'
    ignore_hidden_api_policy_error = AdbOptionsDescriptor("IGNORE_HIDDEN_API_POLICY_ERROR")


class LogcatFilterSpecsOption(SupportsCapabilities):
    LOGCAT_FILTER_SPECS = 'logcatFilterSpecs'
    logcat_filter_specs = AdbOptionsDescriptor("LOGCAT_FILTER_SPECS")


class LogcatFormatOption(SupportsCapabilities):
    LOGCAT_FORMAT = 'logcatFormat' 
    logcat_format = AdbOptionsDescriptor("LOGCAT_FORMAT")


class MockLocationAppOption(SupportsCapabilities):
    MOCK_LOCATION_APP = 'mockLocationApp'
    mock_location_app = AdbOptionsDescriptor("MOCK_LOCATION_APP")


class RemoteAdbHostOption(SupportsCapabilities):
    REMOTE_ADB_HOST = 'remoteAdbHost'
    remote_adb_host = AdbOptionsDescriptor("REMOTE_ADB_HOST")


class RemoteAdbHostOption(SupportsCapabilities):
    REMOTE_ADB_HOST = 'remoteAdbHost'
    remote_adb_host = AdbOptionsDescriptor("REMOTE_ADB_HOST")


class SkipLogcatCaptureOption(SupportsCapabilities):
    SKIP_LOGCAT_CAPTURE = 'skipLogcatCapture'
    skip_logcat_capture = AdbOptionsDescriptor("SKIP_LOGCAT_CAPTURE")


class SuppressKillServerOption(SupportsCapabilities):
    SUPPRESS_KILL_SERVER = 'suppressKillServer'
    suppress_kill_server = AdbOptionsDescriptor("SUPPRESS_KILL_SERVER")