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

SIMULATOR_TRACE_POINTER = 'simulatorTracePointer'


class SimulatorTracePointerOption(SupportsCapabilities):
    @property
    def simulator_trace_pointer(self) -> Optional[bool]:
        """
        Whether to highlight pointer moves in the Simulator window.
        """
        return self.get_capability(SIMULATOR_TRACE_POINTER)

    @simulator_trace_pointer.setter
    def simulator_trace_pointer(self, value: bool) -> None:
        """
        Set whether to highlight pointer moves in the Simulator window.
        The Simulator UI client must be shut down before the session
        startup in order for this capability to be applied properly.
        false by default.
        """
        self.set_capability(SIMULATOR_TRACE_POINTER, value)
