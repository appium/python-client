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

from appium.options.common.supports_capabilities import SupportsCapabilities

BOOTSTRAP_ROOT = 'bootstrapRoot'


class BootstrapRootOption(SupportsCapabilities):
    @property
    def bootstrap_root(self) -> Optional[str]:
        """
        The full path to WebDriverAgentMac root folder where Xcode project
        of the server sources lives.
        """
        return self.get_capability(BOOTSTRAP_ROOT)

    @bootstrap_root.setter
    def bootstrap_root(self, value: str) -> None:
        """
        Set the full path to WebDriverAgentMac root folder where Xcode project
        of the server sources lives. By default, this project is located in
        the same folder where the corresponding driver Node.js module lives.
        """
        self.set_capability(BOOTSTRAP_ROOT, value)
