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

APP_WAIT_FOR_LAUNCH = 'appWaitForLaunch'


class AppWaitForLaunchOption(SupportsCapabilities):
    @property
    def app_wait_for_launch(self) -> Optional[bool]:
        """
        Whether to block until the app under test returns the control to the
        caller after its activity has been started by Activity Manager.
        """
        return self.get_capability(APP_WAIT_FOR_LAUNCH)

    @app_wait_for_launch.setter
    def app_wait_for_launch(self, value: bool) -> None:
        """
        Whether to block until the app under test returns the control to the
        caller after its activity has been started by Activity Manager
        (true, the default value) or to continue the test without waiting for that (false).
        """
        self.set_capability(APP_WAIT_FOR_LAUNCH, value)
