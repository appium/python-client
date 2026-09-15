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

UNLOCK_KEY = 'unlockKey'


class UnlockKeyOption(SupportsCapabilities):
    @property
    def unlock_key(self) -> Optional[str]:
        """
        Unlock key.
        """
        return self.get_capability(UNLOCK_KEY)

    @unlock_key.setter
    def unlock_key(self, value: str) -> None:
        """
        Allows to set an unlock key.
        Read [Unlock tutorial](https://github.com/appium/appium-android-driver/blob/master/docs/UNLOCK.md)
        for more details.
        """
        self.set_capability(UNLOCK_KEY, value)
