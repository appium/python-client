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

WDA_STARTUP_RETRIES = 'wdaStartupRetries'


class WdaStartupRetriesOption(SupportsCapabilities):
    @property
    def wda_startup_retries(self) -> Optional[int]:
        """
        Number of retries before to fail WDA deployment.
        """
        return self.get_capability(WDA_STARTUP_RETRIES)

    @wda_startup_retries.setter
    def wda_startup_retries(self, value: int) -> None:
        """
        Number of times to try to build and launch WebDriverAgent onto the device.
        Defaults to 2.
        """
        self.set_capability(WDA_STARTUP_RETRIES, value)
