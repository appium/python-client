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
from typing import Optional, Union

from .supports_capabilities import SupportsCapabilities

NEW_COMMAND_TIMEOUT = 'newCommandTimeout'


class NewCommandTimeoutOption(SupportsCapabilities):
    @property
    def new_command_timeout(self) -> Optional[timedelta]:
        """
        The allowed time before seeing a new server command.
        """
        value = self.get_capability(NEW_COMMAND_TIMEOUT)
        return None if value is None else timedelta(seconds=value)

    @new_command_timeout.setter
    def new_command_timeout(self, value: Union[timedelta, int]) -> None:
        """
        Set the allowed time before seeing a new server command.
        The value could either be provided as timedelta instance or an integer number of seconds.
        """
        self.set_capability(NEW_COMMAND_TIMEOUT, value.total_seconds() if isinstance(value, timedelta) else value)
