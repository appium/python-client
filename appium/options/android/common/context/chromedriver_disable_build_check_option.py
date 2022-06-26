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

CHROMEDRIVER_DISABLE_BUILD_CHECK = 'chromedriverDisableBuildCheck'


class ChromedriverDisableBuildCheckOption(SupportsCapabilities):
    @property
    def chromedriver_disable_build_check(self) -> Optional[bool]:
        """
        Whether to disable the compatibility validation between the current
        chromedriver and the destination browser/web view.
        """
        return self.get_capability(CHROMEDRIVER_DISABLE_BUILD_CHECK)

    @chromedriver_disable_build_check.setter
    def chromedriver_disable_build_check(self, value: bool) -> None:
        """
        Being set to true disables the compatibility validation between the current
        chromedriver and the destination browser/web view. Use it with care.
        false by default.
        """
        self.set_capability(CHROMEDRIVER_DISABLE_BUILD_CHECK, value)
