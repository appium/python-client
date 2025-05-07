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

from typing import Any, Dict, List

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands

from ..mobilecommand import MobileCommand as Command


class Logs(CanExecuteCommands):
    @property
    def log_types(self) -> List[str]:
        """Gets a list of the available log types. This only works with w3c
        compliant browsers.

        Example:
        --------
        >>> driver.log_types
        """
        return self.execute(Command.GET_AVAILABLE_LOG_TYPES)['value']

    def get_log(self, log_type: str) -> List[Dict[str, Any]]:
        """Gets the log for a given log type.

        Parameters:
        ----------
        log_type : str
            - Type of log that which will be returned

        Example:
        --------
        >>> driver.get_log('browser')
        >>> driver.get_log('driver')
        >>> driver.get_log('client')
        >>> driver.get_log('server')
        """
        return self.execute(Command.GET_LOG, {'type': log_type})['value']

    def _add_commands(self) -> None:
        self.command_executor.add_command(Command.GET_LOG, 'POST', '/session/$sessionId/se/log')
        self.command_executor.add_command(Command.GET_AVAILABLE_LOG_TYPES, 'GET', '/session/$sessionId/se/log/types')
