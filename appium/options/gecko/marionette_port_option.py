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

MARIONETTE_PORT = 'marionettePort'


class MarionettePortOption(SupportsCapabilities):
    @property
    def marionette_port(self) -> Optional[int]:
        """
        The number of the port for the Marionette server to listen on.
        """
        return self.get_capability(MARIONETTE_PORT)

    @marionette_port.setter
    def marionette_port(self, value: int) -> None:
        """
        Selects the port for Geckodriver’s connection to the Marionette
        remote protocol. The existing Firefox instance must have Marionette
        enabled. To enable the remote protocol in Firefox, you can pass the
        -marionette flag. Unless the marionette.port preference has been
        user-set, Marionette will listen on port 2828, which is the default
        value for this capability.
        """
        self.set_capability(MARIONETTE_PORT, value)
