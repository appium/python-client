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

USE_SIMULATOR = 'safari:useSimulator'


class UseSimulatorOption(SupportsCapabilities):
    @property
    def use_simulator(self) -> Optional[bool]:
        """
        Whether to use iOS Simulator.
        """
        return self.get_capability(USE_SIMULATOR)

    @use_simulator.setter
    def use_simulator(self, value: bool) -> None:
        """
        If the value of safari:useSimulator is true, safaridriver will only use
        iOS Simulator hosts. If the value of safari:useSimulator is false, safaridriver
        will not use iOS Simulator hosts. NOTE: An Xcode installation is required
        in order to run WebDriver tests on iOS Simulator hosts.
        """
        self.set_capability(USE_SIMULATOR, value)
