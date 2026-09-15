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

SKIP_UNLOCK = 'skipUnlock'


class SkipUnlockOption(SupportsCapabilities):
    @property
    def skip_unlock(self) -> Optional[bool]:
        """
        Whether to skip the check for lock screen presence.
        """
        return self.get_capability(SKIP_UNLOCK)

    @skip_unlock.setter
    def skip_unlock(self, value: bool) -> None:
        """
        Whether to skip the check for lock screen presence (true). By default,
        the driver tries to detect if the device's screen is locked
        before starting the test and to unlock that (which sometimes might be unstable).
        Note, that this operation takes some time, so it is highly recommended to set
        this capability to true and disable screen locking on devices under test.
        """
        self.set_capability(SKIP_UNLOCK, value)
