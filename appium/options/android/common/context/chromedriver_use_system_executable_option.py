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

CHROMEDRIVER_USE_SYSTEM_EXECUTABLE = 'chromedriverUseSystemExecutable'


class ChromedriverUseSystemExecutableOption(SupportsCapabilities):
    @property
    def chromedriver_use_system_executable(self) -> Optional[bool]:
        """
        Whether to use the system chromedriver.
        """
        return self.get_capability(CHROMEDRIVER_USE_SYSTEM_EXECUTABLE)

    @chromedriver_use_system_executable.setter
    def chromedriver_use_system_executable(self, value: bool) -> None:
        """
        Set it to true in order to enforce the usage of chromedriver, which gets
        downloaded by Appium automatically upon installation. This driver might not
        be compatible with the destination browser or a web view. false by default.
        """
        self.set_capability(CHROMEDRIVER_USE_SYSTEM_EXECUTABLE, value)
