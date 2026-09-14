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

USE_PREBUILT_WDA = 'usePrebuiltWDA'


class UsePrebuiltWdaOption(SupportsCapabilities):
    @property
    def use_prebuilt_wda(self) -> Optional[bool]:
        """
        Whether to skip the build phase of running the WDA app.
        """
        return self.get_capability(USE_PREBUILT_WDA)

    @use_prebuilt_wda.setter
    def use_prebuilt_wda(self, value: bool) -> None:
        """
        Skips the build phase of running the WDA app. Building is then the responsibility
        of the user. Only works for Xcode 8+. Defaults to false.
        """
        self.set_capability(USE_PREBUILT_WDA, value)
