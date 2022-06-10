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

from .supports_capabilities import SupportsCapabilities


class AutomationNameOption(SupportsCapabilities):
    AUTOMATION_NAME = 'automationName'

    @property
    def automation_name(self) -> Optional[str]:
        """
        :Returns: String representing the name of the automation engine
        """
        return self.get_capability(self.AUTOMATION_NAME)

    @automation_name.setter
    def automation_name(self, value: str) -> None:
        """
        Set the automation driver to use.

        :Args:
         - value: One of supported automation names

        """
        self.set_capability(self.AUTOMATION_NAME, value)
