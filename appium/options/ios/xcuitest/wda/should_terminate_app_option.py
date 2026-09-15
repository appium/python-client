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

SHOULD_TERMINATE_APP = 'shouldTerminateApp'


class ShouldTerminateAppOption(SupportsCapabilities):
    @property
    def should_terminate_app(self) -> Optional[bool]:
        """
        Whether to enforce app termination on session quit.
        """
        return self.get_capability(SHOULD_TERMINATE_APP)

    @should_terminate_app.setter
    def should_terminate_app(self, value: bool) -> None:
        """
        Specify if the app should be terminated on session end.
        This capability only has an effect if an application identifier
        has been passed to the test session (either explicitly,
        by setting bundleId, or implicitly, by providing app).
        Default is true unless noReset capability is set to true.
        """
        self.set_capability(SHOULD_TERMINATE_APP, value)
