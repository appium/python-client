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

KEEP_KEY_CHAINS = 'keepKeyChains'


class KeepKeyChainsOption(SupportsCapabilities):
    @property
    def keep_key_chains(self) -> Optional[bool]:
        """
        Whether to preserve Simulator keychains after full reset.
        """
        return self.get_capability(KEEP_KEY_CHAINS)

    @keep_key_chains.setter
    def keep_key_chains(self, value: bool) -> None:
        """
        Set the capability to true in order to preserve Simulator keychains folder after
        full reset. This feature has no effect on real devices. Defaults to false.
        """
        self.set_capability(KEEP_KEY_CHAINS, value)
