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

SHOULD_USE_SINGLETON_TEST_MANAGER = 'shouldUseSingletonTestManager'


class ShouldUseSingletonTestManagerOption(SupportsCapabilities):
    @property
    def should_use_singleton_test_manager(self) -> Optional[bool]:
        """
        Whether to use the default proxy for test management within WebDriverAgent.
        """
        return self.get_capability(SHOULD_USE_SINGLETON_TEST_MANAGER)

    @should_use_singleton_test_manager.setter
    def should_use_singleton_test_manager(self, value: bool) -> None:
        """
        Use default proxy for test management within WebDriverAgent. Setting this to false
        sometimes helps with socket hangup problems. Defaults to true.
        """
        self.set_capability(SHOULD_USE_SINGLETON_TEST_MANAGER, value)
