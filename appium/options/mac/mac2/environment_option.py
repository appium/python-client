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

from typing import Dict, Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

ENVIRONMENT = 'environment'


class EnvironmentOption(SupportsCapabilities):
    @property
    def environment(self) -> Optional[Dict[str, str]]:
        """
        Application environment variables mapping.
        """
        return self.get_capability(ENVIRONMENT)

    @environment.setter
    def environment(self, value: Dict[str, str]) -> None:
        """
        Set the dictionary of environment variables (name-&gt;value) that are going to be passed
        to the application under test on top of environment variables inherited from
        the parent process. This option is only going to be applied if the application
        is not running on session startup.
        """
        self.set_capability(ENVIRONMENT, value)
