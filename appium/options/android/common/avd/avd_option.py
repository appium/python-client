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

AVD = 'avd'


class AvdOption(SupportsCapabilities):
    @property
    def avd(self) -> Optional[str]:
        """
        Name of Android emulator to run the test on.
        """
        return self.get_capability(AVD)

    @avd.setter
    def avd(self, value: str) -> None:
        """
        The name of Android emulator to run the test on.
        Names of currently installed emulators could be listed using
        avdmanager list avd command. If the emulator with the given name
        is not running then it is going to be started before a test.
        """
        self.set_capability(AVD, value)
