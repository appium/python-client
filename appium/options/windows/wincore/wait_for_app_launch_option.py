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

from appium.options.common.supports_capabilities import SupportsCapabilities
from appium.options.windows.windows.wait_for_app_launch_option import WAIT_FOR_APP_LAUNCH

MAX_WAIT_FOR_APP_LAUNCH_SECONDS = 120


class WaitForAppLaunchOption(SupportsCapabilities):
    @property
    def wait_for_app_launch(self) -> timedelta | None:
        """
        Maximum wait duration for the application window to appear after launch.
        Values up to 120 are interpreted as seconds by Wincore; larger values are
        interpreted as milliseconds.
        """
        value = self.get_capability(WAIT_FOR_APP_LAUNCH)
        if value is None:
            return None
        if value > MAX_WAIT_FOR_APP_LAUNCH_SECONDS:
            return timedelta(milliseconds=value)
        return timedelta(seconds=value)

    @wait_for_app_launch.setter
    def wait_for_app_launch(self, value: timedelta | int | float) -> None:
        """
        Set how long to wait for the application window (or main window after a splash
        screen) to appear after launch. Numeric values up to 120 are read as seconds and
        larger values as milliseconds. ``timedelta`` values longer than 120 seconds are
        serialized in milliseconds.
        """
        if isinstance(value, timedelta):
            seconds = value.total_seconds()
            serialized: int | float = round(seconds * 1000) if seconds > MAX_WAIT_FOR_APP_LAUNCH_SECONDS else seconds
        else:
            serialized = value
        self.set_capability(WAIT_FOR_APP_LAUNCH, serialized)
