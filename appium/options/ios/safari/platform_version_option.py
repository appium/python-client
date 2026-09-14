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

PLATFORM_VERSION = 'safari:platformVersion'


class PlatformVersionOption(SupportsCapabilities):
    @property
    def platform_version(self) -> Optional[str]:
        """
        String representing the platform version.
        """
        return self.get_capability(PLATFORM_VERSION)

    @platform_version.setter
    def platform_version(self, value: str) -> None:
        """
        safaridriver will only create a session using hosts whose OS
        version matches the value of safari:platformVersion. OS version
        numbers are prefix-matched. For example, if the value of safari:platformVersion
        is '12', this will allow hosts with an OS version of '12.0' or '12.1' but not '10.12'.
        """
        self.set_capability(PLATFORM_VERSION, value)
