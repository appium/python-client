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

PLATFORM_BUILD_VERSION = 'safari:platformBuildVersion'


class PlatformBuildVersionOption(SupportsCapabilities):
    @property
    def platform_build_version(self) -> Optional[str]:
        """
        String representing the platform build version.
        """
        return self.get_capability(PLATFORM_BUILD_VERSION)

    @platform_build_version.setter
    def platform_build_version(self, value: str) -> None:
        """
        safaridriver will only create a session using hosts whose OS build
        version matches the value of safari:platformBuildVersion. Example
        of a macOS build version is '18E193'. On macOS, the OS build version
        can be determined by running the sw_vers(1) utility.
        """
        self.set_capability(PLATFORM_BUILD_VERSION, value)
