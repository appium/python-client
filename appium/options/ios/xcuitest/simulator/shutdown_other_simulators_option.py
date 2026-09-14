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

SHUTDOWN_OTHER_SIMULATORS = 'shutdownOtherSimulators'


class ShutdownOtherSimulatorsOption(SupportsCapabilities):
    @property
    def shutdown_other_simulators(self) -> Optional[bool]:
        """
        Whether to shut down of other booted simulators except of the current one.
        """
        return self.get_capability(SHUTDOWN_OTHER_SIMULATORS)

    @shutdown_other_simulators.setter
    def shutdown_other_simulators(self, value: bool) -> None:
        """
        If this capability set to true and the current device under test is an iOS
        Simulator then Appium will try to shut down all the other running Simulators
        before to start a new session. This might be useful while executing webview
        tests on different devices, since only one device can be debugged remotely
        at once due to an Apple bug. The capability only has an effect if
        --relaxed-security command line argument is provided to the server.
        Defaults to false.
        """
        self.set_capability(SHUTDOWN_OTHER_SIMULATORS, value)
