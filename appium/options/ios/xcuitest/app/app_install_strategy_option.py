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

APP_INSTALL_STRATEGY = 'appInstallStrategy'


class AppInstallStrategyOption(SupportsCapabilities):
    @property
    def app_install_strategy(self) -> Optional[str]:
        """
        App install strategy.
        """
        return self.get_capability(APP_INSTALL_STRATEGY)

    @app_install_strategy.setter
    def app_install_strategy(self, value: str) -> None:
        """
        Select application installation strategy for real devices. The following
        strategies are supported:
        * serial (default) - pushes app files to the device in a sequential order;
        this is the least performant strategy, although the most reliable;
        * parallel - pushes app files simultaneously; this is usually the
        most performant strategy, but sometimes could not be very stable;
        * ios-deploy - tells the driver to use a third-party tool ios-deploy to
        install the app; obviously the tool must be installed separately
        first and must be present in PATH before it could be used.
        """
        self.set_capability(APP_INSTALL_STRATEGY, value)
