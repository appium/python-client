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
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied.  See the License for the specific
# language governing permissions and limitations
# under the License.

from typing import Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

PREBUILT_WDA_PATH = 'prebuiltWDAPath'


class PrebuiltWdaPathOption(SupportsCapabilities):
    @property
    def prebuilt_wda_path(self) -> Optional[str]:
        """
        The path to the prebuilt WebDriverAgent.
        """
        return self.get_capability(PREBUILT_WDA_PATH)

    @prebuilt_wda_path.setter
    def prebuilt_wda_path(self, value: str) -> None:
        """
        The path to the prebuilt WebDriverAgent. This should be the path to the
        WebDriverAgent.xcarchive file or the WebDriverAgent.app bundle.
        """
        self.set_capability(PREBUILT_WDA_PATH, value)
