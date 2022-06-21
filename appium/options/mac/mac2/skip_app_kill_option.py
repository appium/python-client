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

SKIP_APP_KILL = 'skipAppKill'


class SkipAppKillOption(SupportsCapabilities):
    @property
    def skip_app_kill(self) -> Optional[bool]:
        """
        Whether to skip the termination of the application under test.
        """
        return self.get_capability(SKIP_APP_KILL)

    @skip_app_kill.setter
    def skip_app_kill(self, value: bool) -> None:
        """
        Set whether to skip the termination of the application under test
        when the testing session quits. false by default. This capability
        is only going to be applied if bundleId is set.
        """
        self.set_capability(SKIP_APP_KILL, value)
