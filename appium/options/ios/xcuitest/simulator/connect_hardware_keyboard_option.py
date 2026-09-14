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

CONNECT_HARDWARE_KEYBOARD = 'connectHardwareKeyboard'


class ConnectHardwareKeyboardOption(SupportsCapabilities):
    @property
    def connect_hardware_keyboard(self) -> Optional[bool]:
        """
        Whether to connect hardware keyboard to Simulator.
        """
        return self.get_capability(CONNECT_HARDWARE_KEYBOARD)

    @connect_hardware_keyboard.setter
    def connect_hardware_keyboard(self, value: bool) -> None:
        """
        Set this option to true in order to enable hardware keyboard in Simulator.
        The preference works only when Appium launches a simulator instance with
        this value. It is set to false by default, because this helps to workaround
        some XCTest bugs. connectHardwareKeyboard: true makes
        forceSimulatorSoftwareKeyboardPresence: false if no explicit value is set
        for forceSimulatorSoftwareKeyboardPresence capability since Appium 1.22.0.
        """
        self.set_capability(CONNECT_HARDWARE_KEYBOARD, value)
