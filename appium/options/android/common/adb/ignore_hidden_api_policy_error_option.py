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

IGNORE_HIDDEN_API_POLICY_ERROR = 'ignoreHiddenApiPolicyError'


class IgnoreHiddenApiPolicyErrorOption(SupportsCapabilities):
    @property
    def ignore_hidden_api_policy_error(self) -> Optional[bool]:
        """
        Whether to ignore a failure while changing hidden API access policies.
        """
        return self.get_capability(IGNORE_HIDDEN_API_POLICY_ERROR)

    @ignore_hidden_api_policy_error.setter
    def ignore_hidden_api_policy_error(self, value: bool) -> None:
        """
        Being set to true ignores a failure while changing hidden API access policies.
        Could be useful on some devices, where access to these policies has been locked by its vendor.
        false by default.
        """
        self.set_capability(IGNORE_HIDDEN_API_POLICY_ERROR, value)
