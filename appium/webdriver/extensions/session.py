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

from typing import Dict

from appium.common.logger import logger
from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands

from ..mobilecommand import MobileCommand as Command


class Session(CanExecuteCommands):
    @property
    def events(self) -> Dict:
        """Retrieves events information from the current session

        Usage:
            events = driver.events

        Returns:
            `dict`:  containing events timing information from the current session
        """
        try:
            return self.execute(Command.GET_SESSION)['value']['events']
        except Exception as e:
            logger.warning('Could not find events information in the session. Error: %s', e)
            return {}

    def _add_commands(self) -> None:
        self.command_executor.add_command(Command.GET_SESSION, 'GET', '/session/$sessionId')
