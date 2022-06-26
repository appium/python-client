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

MOCK_LOCATION_APP = 'mockLocationApp'


class MockLocationAppOption(SupportsCapabilities):
    @property
    def mock_location_app(self) -> Optional[str]:
        """
        Identifier of the app, which is used as a system mock location provider.
        """
        return self.get_capability(MOCK_LOCATION_APP)

    @mock_location_app.setter
    def mock_location_app(self, value: str) -> None:
        """
        Sets the package identifier of the app, which is used as a system mock location
        provider since Appium 1.18.0+. This capability has no effect on emulators.
        If the value is set to null or an empty string, then Appium will skip the mocked
        location provider setup procedure. Defaults to Appium Setting package
        identifier (io.appium.settings).
        """
        self.set_capability(MOCK_LOCATION_APP, value)
