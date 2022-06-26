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

UNLOCK_STRATEGY = 'unlockStrategy'


class UnlockStrategyOption(SupportsCapabilities):
    @property
    def unlock_strategy(self) -> Optional[str]:
        """
        Unlock strategy name.
        """
        return self.get_capability(UNLOCK_STRATEGY)

    @unlock_strategy.setter
    def unlock_strategy(self, value: str) -> None:
        """
        Either 'locksettings' (default) or 'uiautomator'.
        Setting it to 'uiautomator' will enforce the driver to avoid using special
        ADB shortcuts in order to speed up the unlock procedure.
        """
        self.set_capability(UNLOCK_STRATEGY, value)
