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

from typing import Any, Dict, Optional, Union

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands

from ..mobilecommand import MobileCommand as Command


class ExecuteDriver(CanExecuteCommands):
    # TODO Inner class case
    def execute_driver(self, script: str, script_type: str = 'webdriverio', timeout_ms: Optional[int] = None) -> Any:
        """Run a set of script against the current session, allowing execution of many commands in one Appium request.
        Please read http://appium.io/docs/en/commands/session/execute-driver for more details about the acceptable
        scripts and the output format.

        Args:
            script: The string consisting of the script itself
            script_type: The name of the script type. Defaults to 'webdriverio'.
            timeout_ms: The number of `ms` Appium should wait for the script to finish before
             killing it due to timeout_ms.

        Usage:
            | self.driver.execute_driver(script='return [];')
            | self.driver.execute_driver(script='return [];', script_type='webdriverio')
            | self.driver.execute_driver(script='return [];', script_type='webdriverio', timeout_ms=10000)

        Returns:
            ExecuteDriver.Result: The result of the script. It has 'result' and 'logs' keys.

        Raises:
            WebDriverException: If something error happenes in the script. The message has the original error message.
        """

        class Result:
            def __init__(self, res: Dict):
                self.result = res['result']
                self.logs = res['logs']

        option: Dict[str, Union[str, int]] = {'script': script, 'type': script_type}
        if timeout_ms is not None:
            option['timeout'] = timeout_ms

        response = self.execute(Command.EXECUTE_DRIVER, option)['value']
        return Result(response)

    def _add_commands(self) -> None:
        self.command_executor.add_command(Command.EXECUTE_DRIVER, 'POST', '/session/$sessionId/appium/execute_driver')
