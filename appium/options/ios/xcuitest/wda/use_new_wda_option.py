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

USE_NEW_WDA = 'useNewWDA'


class UseNewWdaOption(SupportsCapabilities):
    @property
    def use_new_wda(self) -> Optional[bool]:
        """
        Whether whether to uninstall of any existing WebDriverAgent app
        on the device under test.
        """
        return self.get_capability(USE_NEW_WDA)

    @use_new_wda.setter
    def use_new_wda(self, value: bool) -> None:
        """
        If true, forces uninstall of any existing WebDriverAgent app on device.
        Set it to true if you want to apply different startup options for WebDriverAgent
        for each session. Although, it is only guaranteed to work stable on Simulator.
        Real devices require WebDriverAgent client to run for as long as possible without
        reinstall/restart to avoid issues like
        https://github.com/facebook/WebDriverAgent/issues/507. The false value
        (the default behaviour since driver version 2.35.0) will try to
        detect currently running WDA listener executed by previous testing session(s)
        and reuse it if possible, which is highly recommended for real device testing
        and to speed up suites of multiple tests in general. A new WDA session will be
        triggered at the default URL (http://localhost:8100) if WDA is not listening and
        webDriverAgentUrl capability is not set. The negative/unset value of useNewWDA
        capability has no effect prior to xcuitest driver version 2.35.0.
        """
        self.set_capability(USE_NEW_WDA, value)
