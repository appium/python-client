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

CHROMEDRIVER_PORT = 'chromedriverPort'


class ChromedriverPortOption(SupportsCapabilities):
    @property
    def chromedriver_port(self) -> Optional[int]:
        """
        Local port number to use for Chromedriver communication.
        """
        return self.get_capability(CHROMEDRIVER_PORT)

    @chromedriver_port.setter
    def chromedriver_port(self, value: int) -> None:
        """
        The port number to use for Chromedriver communication.
        Any free port number is selected by default if unset.
        """
        self.set_capability(CHROMEDRIVER_PORT, value)
