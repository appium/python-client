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

C = TypeVar("C", bound="SupportsCapabilities")


class OtherOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: C, cls: type[C]) -> Any:
        if self.name == "COMMAND_TIMEOUTS":
            value = getattr(obj, "get_capability")(self.name)
            if value is None:
                return None
            if isinstance(value, dict):
                return {k: timedelta(milliseconds=v) for k, v in value.items()}
            return timedelta(milliseconds=int(value))
        return getattr(obj, "get_capability")(self.name)

    def __set__(self, obj: C, value: Any) -> C:
        if self.name == "COMMAND_TIMEOUTS":
            if isinstance(value, dict):
                getattr(obj, "set_capability")(self.name, {k: int(v.total_seconds() * 1000) for k, v in value.items()})
            elif isinstance(value, timedelta):
                getattr(obj, "set_capability")(self.name, f'{int(value.total_seconds() * 1000)}')
            else:
                return getattr(obj, "set_capability")(self.name, value)
        return getattr(obj, "set_capability")(self.name, value)


class UseJsonSourceOption(SupportsCapabilities):
    USE_JSON_SOURCE = 'useJSONSource'
    use_json_source = OtherOptionsDescriptor("USE_JSON_SOURCE")
    """
    Whether to get JSON source from WDA and transform it to XML on the driver side.
    Defaults to false.

    Usage
    -----
    - `self.use_json_source`
    - `self.use_json_source` = `value`
    """


class ShowIosLogOption(SupportsCapabilities):
    SHOW_IOS_LOG = 'showIOSLog'
    show_ios_log = OtherOptionsDescriptor("SHOW_IOS_LOG")
    """
    Whether to show any logs captured from a device in the appium logs.
    Default false.

    Usage
    ----
    - `self.show_ios_log`
    - `self.show_ios_log` = `value`
    """


class LaunchWithIdbOption(SupportsCapabilities):
    LAUNCH_WITH_IDB = 'launchWithIDB'
    launch_with_idb = OtherOptionsDescriptor("LAUNCH_WITH_IDB")
    """
    Launch WebDriverAgentRunner with idb instead of xcodebuild. This could save
    a significant amount of time by skipping the xcodebuild process, although the
    idb might not be very reliable, especially with fresh Xcode SDKs. Check
    the idb repository for more details on possible compatibility issues.
    Defaults to false.

    Usage
    -----
    - `self.launch_with_idb`
    - `self.launch_with_idb` = `value`
    """


class CommandTimeoutsOption(SupportsCapabilities):
    COMMAND_TIMEOUTS = 'commandTimeouts'
    command_timeouts = OtherOptionsDescriptor("COMMAND_TIMEOUTS")
    """
    Custom timeout for all WDA backend commands execution.
    This might be useful if WDA backend freezes unexpectedly or requires too
    much time to fail and blocks automated test execution.
    Dictionary keys are command names which you can find in server logs. Look for
    "Executing command 'command_name'" records.
    Timeout value is expected to contain max duration to wait for
    the given WDA command to be executed before terminating the session forcefully.
    The magic 'default' key allows to provide the timeout for all other commands that
    were not explicitly mentioned as dictionary keys

    Usage
    ----
    - `self.command_timeouts`
    - `self.command_timeouts` = `value`
    """