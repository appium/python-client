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

from typing import Optional, TypeVar

from selenium.webdriver.remote.switch_to import SwitchTo

from appium.protocols.protocol import Protocol
from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands

from .mobilecommand import MobileCommand


class HasDriver(Protocol):
    _driver: CanExecuteCommands


T = TypeVar('T', bound=HasDriver)


class MobileSwitchTo(SwitchTo, HasDriver):
    def context(self: T, context_name: Optional[str]) -> T:
        """Sets the context for the current session.
        Passing `None` is equal to switching to native context.

        Args:
            context_name: The name of the context to switch to.

        Usage:
            driver.switch_to.context('WEBVIEW_1')
        """
        self._driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {'name': context_name})
        return self
