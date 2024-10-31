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

from typing import Dict, List, Union

from selenium.common.exceptions import UnknownMethodException

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.protocols.webdriver.can_remember_extension_presence import CanRememberExtensionPresence
from appium.webdriver.mobilecommand import MobileCommand as Command


class Performance(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    def get_performance_data(
        self, package_name: str, data_type: str, data_read_timeout: Union[int, None] = None
    ) -> List[List[str]]:
        """Returns the information of the system state
        which is supported to read as like cpu, memory, network traffic, and battery.

        Android only.

        Args:
            package_name: The package name of the application
            data_type: The type of system state which wants to read.
                It should be one of the supported performance data types.
                Check :func:`.get_performance_data_types` for supported types
            data_read_timeout: The number of attempts to read

        Usage:
            self.driver.get_performance_data('my.app.package', 'cpuinfo', 5)

        Returns:
            The data along to `data_type`
        """
        ext_name = 'mobile: getPerformanceData'
        args: Dict[str, Union[str, int]] = {'packageName': package_name, 'dataType': data_type}
        try:
            return self.assert_extension_exists(ext_name).execute_script(ext_name, args)
        except UnknownMethodException:
            # TODO: Remove the fallback
            if data_read_timeout is not None:
                args['dataReadTimeout'] = data_read_timeout
            return self.mark_extension_absence(ext_name).execute(Command.GET_PERFORMANCE_DATA, args)['value']

    def get_performance_data_types(self) -> List[str]:
        """Returns the information types of the system state
        which is supported to read as like cpu, memory, network traffic, and battery.
        Android only.

        Usage:
            self.driver.get_performance_data_types()

        Returns:
            Available data types
        """
        ext_name = 'mobile: getPerformanceDataTypes'
        try:
            return self.assert_extension_exists(ext_name).execute_script(ext_name)
        except UnknownMethodException:
            # TODO: Remove the fallback
            return self.mark_extension_absence(ext_name).execute(Command.GET_PERFORMANCE_DATA_TYPES)['value']

    def _add_commands(self) -> None:
        self.command_executor.add_command(
            Command.GET_PERFORMANCE_DATA,
            'POST',
            '/session/$sessionId/appium/getPerformanceData',
        )
        self.command_executor.add_command(
            Command.GET_PERFORMANCE_DATA_TYPES,
            'POST',
            '/session/$sessionId/appium/performanceData/types',
        )
