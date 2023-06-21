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


class OtherOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: Any, cls: Any) -> Any:
        if self.name == "COMMAND_TIMEOUTS":
            value = getattr(obj, "get_capabilities")(self.name)
            if value is None:
                return None
            if isinstance(value, dict):
                return {k: timedelta(milliseconds=v) for k, v in value.items()}
            return timedelta(milliseconds=int(value))
        return getattr(obj, "get_capabilities")(self.name)

    def __set__(self, obj: Any, value: Any) -> Any:
        if self.name == "COMMAND_TIMEOUTS":
            if isinstance(value, dict):
                getattr(obj, "set_capabilities")(self.name, {k: int(v.total_seconds() * 1000) for k, v in value.items()})
            elif isinstance(value, timedelta):
                getattr(obj, "set_capabilities")(self.name, f'{int(value.total_seconds() * 1000)}')
            else:
                getattr(obj, "set_capabilities")(self.name, value)
        getattr(obj, "set_capabilities")(self.name, value)


class UseJsonSourceOption(SupportsCapabilities):
    USE_JSON_SOURCE = 'useJSONSource'
    use_json_source = OtherOptionsDescriptor("USE_JSON_SOURCE")


class ShowIosLogOption(SupportsCapabilities):
    SHOW_IOS_LOG = 'showIOSLog'
    show_ios_log = OtherOptionsDescriptor("SHOW_IOS_LOG")


class LaunchWithIdbOption(SupportsCapabilities):
    LAUNCH_WITH_IDB = 'launchWithIDB'
    launch_with_idb = OtherOptionsDescriptor("LAUNCH_WITH_IDB")


class CommandTimeoutsOption(SupportsCapabilities):
    COMMAND_TIMEOUTS = 'commandTimeouts'
    command_timeouts = OtherOptionsDescriptor("COMMAND_TIMEOUTS")