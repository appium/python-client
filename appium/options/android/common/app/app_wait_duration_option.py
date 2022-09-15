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

from appium.options.common.supports_capabilities import SupportsCapabilities

APP_WAIT_DURATION = 'appWaitDuration'


class AppWaitDurationOption(SupportsCapabilities):
    @property
    def app_wait_duration(self) -> Optional[timedelta]:
        """
        Identifier of the app package to wait for.
        """
        value = self.get_capability(APP_WAIT_DURATION)
        return None if value is None else timedelta(milliseconds=value)

    @app_wait_duration.setter
    def app_wait_duration(self, value: Union[timedelta, int]) -> None:
        """
        Maximum amount of time to wait until the application under test is started
        (e.g. an activity returns the control to the caller). 20000 ms by default.
        """
        self.set_capability(
            APP_WAIT_DURATION, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value
        )
