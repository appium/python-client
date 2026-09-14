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

FORCE_SIMULATOR_SOFTWARE_KEYBOARD_PRESENCE = 'forceSimulatorSoftwareKeyboardPresence'


class ForceSimulatorSoftwareKeyboardPresenceOption(SupportsCapabilities):
    @property
    def force_simulator_software_keyboard_presence(self) -> Optional[bool]:
        """
        Whether to enforce software keyboard presence.
        """
        return self.get_capability(FORCE_SIMULATOR_SOFTWARE_KEYBOARD_PRESENCE)

    @force_simulator_software_keyboard_presence.setter
    def force_simulator_software_keyboard_presence(self, value: bool) -> None:
        """
        Set this option to true in order to turn software keyboard on and turn
        hardware keyboard off in Simulator since Appium 1.22.0. This option helps
        to avoid Keyboard is not present error. It is set to true by default.
        Appium respects preset simulator software/hardware keyboard preference
        when this value is false, so connectHardwareKeyboard: false and
        forceSimulatorSoftwareKeyboardPresence: false means for Appium to keep
        the current Simulator keyboard preferences. This option has priority
        over connectHardwareKeyboard.
        """
        self.set_capability(FORCE_SIMULATOR_SOFTWARE_KEYBOARD_PRESENCE, value)
