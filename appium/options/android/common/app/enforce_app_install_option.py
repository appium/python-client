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

ENFORCE_APP_INSTALL = 'enforceAppInstall'


class EnforceAppInstallOption(SupportsCapabilities):
    @property
    def enforce_app_install(self) -> Optional[bool]:
        """
        Whether the application under test is always reinstalled even
        if a newer version of it already exists on the device under test.
        """
        return self.get_capability(ENFORCE_APP_INSTALL)

    @enforce_app_install.setter
    def enforce_app_install(self, value: bool) -> None:
        """
        Allows setting whether the application under test is always reinstalled even
        if a newer version of it already exists on the device under test. false by default.
        """
        self.set_capability(ENFORCE_APP_INSTALL, value)
