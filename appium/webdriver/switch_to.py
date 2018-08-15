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

from selenium.webdriver.remote.switch_to import SwitchTo

from .mobilecommand import MobileCommand


class MobileSwitchTo(SwitchTo):
    def context(self, context_name):
        """
        Sets the context for the current session.

        :Args:
         - context_name: The name of the context to switch to.

        :Usage:
            driver.switch_to.context('WEBVIEW_1')
        """
        self._driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {'name': context_name})
