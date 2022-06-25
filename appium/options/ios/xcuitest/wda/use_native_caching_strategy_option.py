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

USE_NATIVE_CACHING_STRATEGY = 'useNativeCachingStrategy'


class UseNativeCachingStrategyOption(SupportsCapabilities):
    @property
    def use_native_caching_strategy(self) -> Optional[bool]:
        """
        Whether to use the native caching strategy.
        """
        return self.get_capability(USE_NATIVE_CACHING_STRATEGY)

    @use_native_caching_strategy.setter
    def use_native_caching_strategy(self, value: bool) -> None:
        """
        Set this capability to false in order to use the custom elements caching
        strategy. This might help to avoid stale element exception on property
        change. By default, the native XCTest cache resolution is used (true)
        for all native locators (e.g. all, but xpath).
        """
        self.set_capability(USE_NATIVE_CACHING_STRATEGY, value)
