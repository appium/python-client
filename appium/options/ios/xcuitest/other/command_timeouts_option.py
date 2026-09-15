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
from typing import Dict, Optional, Union

from appium.options.common.supports_capabilities import SupportsCapabilities

COMMAND_TIMEOUTS = 'commandTimeouts'


class CommandTimeoutsOption(SupportsCapabilities):
    @property
    def command_timeouts(self) -> Optional[Union[Dict[str, timedelta], timedelta]]:
        """
        Custom timeout(s) for WDA backend commands execution.
        """
        value = self.get_capability(COMMAND_TIMEOUTS)
        if value is None:
            return None
        if isinstance(value, dict):
            return {k: timedelta(milliseconds=v) for k, v in value.items()}
        return timedelta(milliseconds=int(value))

    @command_timeouts.setter
    def command_timeouts(self, value: Union[Dict[str, timedelta], timedelta, int]) -> None:
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
        """
        if isinstance(value, dict):
            self.set_capability(COMMAND_TIMEOUTS, {k: int(v.total_seconds() * 1000) for k, v in value.items()})
        elif isinstance(value, timedelta):
            self.set_capability(COMMAND_TIMEOUTS, f'{int(value.total_seconds() * 1000)}')
        else:
            self.set_capability(COMMAND_TIMEOUTS, value)
