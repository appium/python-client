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

from appium.options.common.supports_capabilities import SupportsCapabilities

ISOLATED_SCRIPT_EXECUTION = 'isolatedScriptExecution'


class IsolatedScriptExecutionOption(SupportsCapabilities):
    @property
    def isolated_script_execution(self) -> bool | None:
        """
        Whether PowerShell scripts run without loading the user profile.
        """
        return self.get_capability(ISOLATED_SCRIPT_EXECUTION)

    @isolated_script_execution.setter
    def isolated_script_execution(self, value: bool) -> None:
        """
        Set whether PowerShell scripts (windows: powerShell, prerun, postrun) run
        without loading the user profile.
        """
        self.set_capability(ISOLATED_SCRIPT_EXECUTION, value)
