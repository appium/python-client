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

LAUNCH_WITH_IDB = 'launchWithIDB'


class LaunchWithIdbOption(SupportsCapabilities):
    @property
    def launch_with_idb(self) -> Optional[bool]:
        """
        Whether to launch WebDriverAgentRunner with idb instead of xcodebuild.
        """
        return self.get_capability(LAUNCH_WITH_IDB)

    @launch_with_idb.setter
    def launch_with_idb(self, value: bool) -> None:
        """
        Launch WebDriverAgentRunner with idb instead of xcodebuild. This could save
        a significant amount of time by skipping the xcodebuild process, although the
        idb might not be very reliable, especially with fresh Xcode SDKs. Check
        the idb repository for more details on possible compatibility issues.
        Defaults to false.
        """
        self.set_capability(LAUNCH_WITH_IDB, value)
