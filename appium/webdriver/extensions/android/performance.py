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

from typing import TYPE_CHECKING, Dict, List, TypeVar, Union

from selenium import webdriver

from appium.webdriver.mobilecommand import MobileCommand as Command

if TYPE_CHECKING:
    # noinspection PyUnresolvedReferences
    from appium.webdriver.webdriver import WebDriver

T = TypeVar('T', bound=Union['WebDriver', 'Performance'])


class Performance(webdriver.Remote):
    def get_performance_data(
        self: T, package_name: str, data_type: str, data_read_timeout: int = None
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
        data: Dict[str, Union[str, int]] = {'packageName': package_name, 'dataType': data_type}
        if data_read_timeout is not None:
            data['dataReadTimeout'] = data_read_timeout
        return self.execute(Command.GET_PERFORMANCE_DATA, data)['value']

    def get_performance_data_types(self: T) -> List:
        """Returns the information types of the system state
        which is supported to read as like cpu, memory, network traffic, and battery.
        Android only.

        Usage:
            self.driver.get_performance_data_types()

        Returns:
            Available data types
        """
        return self.execute(Command.GET_PERFORMANCE_DATA_TYPES)['value']

    # pylint: disable=protected-access

    # noinspection PyProtectedMember
    def _addCommands(self) -> None:
        self.command_executor._commands[Command.GET_PERFORMANCE_DATA] = (
            'POST',
            '/session/$sessionId/appium/getPerformanceData',
        )
        self.command_executor._commands[Command.GET_PERFORMANCE_DATA_TYPES] = (
            'POST',
            '/session/$sessionId/appium/performanceData/types',
        )
