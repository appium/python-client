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

RECREATE_CHROME_DRIVER_SESSIONS = 'recreateChromeDriverSessions'


class RecreateChromeDriverSessionsOption(SupportsCapabilities):
    @property
    def recreate_chrome_driver_sessions(self) -> Optional[bool]:
        """
        Whether chromedriver sessions should be killed and then recreated instead
        of just suspending it on context switch.
        """
        return self.get_capability(RECREATE_CHROME_DRIVER_SESSIONS)

    @recreate_chrome_driver_sessions.setter
    def recreate_chrome_driver_sessions(self, value: bool) -> None:
        """
        If this capability is set to true then chromedriver session is always going
        to be killed and then recreated instead of just suspending it on context
        switching. false by default.
        """
        self.set_capability(RECREATE_CHROME_DRIVER_SESSIONS, value)
