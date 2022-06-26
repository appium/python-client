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

SKIP_SERVER_INSTALLATION = 'skipServerInstallation'


class SkipServerInstallationOption(SupportsCapabilities):
    @property
    def skip_server_installation(self) -> Optional[bool]:
        """
        Whether to skip the server components installation
        on the device under test and all the related checks.
        """
        return self.get_capability(SKIP_SERVER_INSTALLATION)

    @skip_server_installation.setter
    def skip_server_installation(self, value: bool) -> None:
        """
        Set whether to skip the server components installation
        on the device under test and all the related checks.
        This could help to speed up the session startup if you know for sure the
        correct server version is installed on the device.
        In case the server is not installed or an incorrect version of it is installed
        then you may get an unexpected error later.
        """
        self.set_capability(SKIP_SERVER_INSTALLATION, value)
