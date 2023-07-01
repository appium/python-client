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

from appium.options.transformers import OptionsDescriptor
from appium.options.common.supports_capabilities import SupportsCapabilities


class UseJsonSourceOption(SupportsCapabilities):
    USE_JSON_SOURCE = 'useJSONSource'
    use_json_source = OptionsDescriptor('USE_JSON_SOURCE')
    """
    Whether to get JSON source from WDA and transform it to XML on the driver side.
    Defaults to false.

    Usage
    -----
    - Get
        - `self.use_json_source`
    - Set
        - `self.use_json_source` = `value`
    
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


class ShowIosLogOption(SupportsCapabilities):
    SHOW_IOS_LOG = 'showIOSLog'
    show_ios_log = OptionsDescriptor('SHOW_IOS_LOG')
    """
    Whether to show any logs captured from a device in the appium logs.
    Default false.

    Usage
    -----
    - Get
        - `self.show_ios_log`
    - Set
        - `self.show_ios_log` = `value`
    
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


class LaunchWithIdbOption(SupportsCapabilities):
    LAUNCH_WITH_IDB = 'launchWithIDB'
    launch_with_idb = OptionsDescriptor('LAUNCH_WITH_IDB')
    """
    Launch WebDriverAgentRunner with idb instead of xcodebuild. This could save
    a significant amount of time by skipping the xcodebuild process, although the
    idb might not be very reliable, especially with fresh Xcode SDKs. Check
    the idb repository for more details on possible compatibility issues.
    Defaults to false.

    Usage
    -----
    - Get
        - `self.launch_with_idb`
    - Set
        - `self.launch_with_idb` = `value`
    
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


class CommandTimeoutsOption(SupportsCapabilities):
    COMMAND_TIMEOUTS = 'commandTimeouts'

    def transform_get(self, value):
        if value is None:
            return None
        if isinstance(value, dict):
            return {k: timedelta(milliseconds=v) for k, v in value.items()}
        return timedelta(milliseconds=int(value))

    def transform_set(self, value):
        if isinstance(value, dict):
            return {k: int(v.total_seconds() * 1000) for k, v in value.items()}
        elif isinstance(value, timedelta):
            return f'{int(value.total_seconds() * 1000)}'
        else:
            return value
    
    command_timeouts = OptionsDescriptor('COMMAND_TIMEOUTS', transform_get, transform_set)
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
    -----
    - Get
        - `self.command_timeouts`
    - Set
        - `self.command_timeouts` = `value`
    
    Parameters
    ----------
    `value`: `Union[Dict[str, timedelta], timedelta, int]`

    Returns
    -------
    - Get
        - `Optional[Union[Dict[str, timedelta], timedelta]`
    - Set
        - `None`
    """