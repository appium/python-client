#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Dict, TypeVar

from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts

T = TypeVar('T', bound=CanExecuteScripts)


class ExecuteMobileCommand(CanExecuteScripts):
    def press_button(self: T, button_name: str) -> T:
        """Sends a physical button name to the device to simulate the user pressing.

        iOS only.
        Possible button names can be found in
        https://github.com/appium/WebDriverAgent/blob/master/WebDriverAgentLib/Categories/XCUIDevice%2BFBHelpers.h

        Args:
            button_name: the button name to be sent to the device

        Returns:
            Union['WebDriver', 'ExecuteMobileCommand']: Self instance

        """
        data = {'name': button_name}
        self.execute_script('mobile: pressButton', data)
        return self

    @property
    def battery_info(self) -> Dict[str, Any]:
        """Retrieves battery information for the device under test.

        Returns:
            `dict`: containing the following entries
                level: Battery level in range [0.0, 1.0], where 1.0 means 100% charge.
                    Any value lower than 0 means the level cannot be retrieved
                state: Platform-dependent battery state value.
                    On iOS (XCUITest):
                        1: Unplugged
                        2: Charging
                        3: Full
                        Any other value means the state cannot be retrieved
                    On Android (UIAutomator2):
                        2: Charging
                        3: Discharging
                        4: Not charging
                        5: Full
                        Any other value means the state cannot be retrieved
        """
        return self.execute_script('mobile: batteryInfo')
