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

DERIVED_DATA_PATH = 'derivedDataPath'


class DerivedDataPathOption(SupportsCapabilities):
    @property
    def derived_data_path(self) -> Optional[str]:
        """
        Path to the derived data WDA folder.
        """
        return self.get_capability(DERIVED_DATA_PATH)

    @derived_data_path.setter
    def derived_data_path(self, value: str) -> None:
        """
        Use along with usePrebuiltWDA capability and choose where to search for the existing WDA app.
        If the capability is not set then Xcode will store the derived data in the default root
        taken from preferences.
        It also makes sense to choose different folders for parallel WDA sessions.
        """
        self.set_capability(DERIVED_DATA_PATH, value)
