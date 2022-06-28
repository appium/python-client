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

from typing import Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

APP_WAIT_ACTIVITY = 'appWaitActivity'


class AppWaitActivityOption(SupportsCapabilities):
    @property
    def app_wait_activity(self) -> Optional[str]:
        """
        Name of the app activity to wait for.
        """
        return self.get_capability(APP_WAIT_ACTIVITY)

    @app_wait_activity.setter
    def app_wait_activity(self, value: str) -> None:
        """
        Identifier of the activity that the driver should wait for
        (not necessarily the main one).
        If not provided then defaults to appium:appActivity.
        """
        self.set_capability(APP_WAIT_ACTIVITY, value)
