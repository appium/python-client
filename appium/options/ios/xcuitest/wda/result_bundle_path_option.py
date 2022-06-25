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

RESULT_BUNDLE_PATH = 'resultBundlePath'


class ResultBundlePathOption(SupportsCapabilities):
    @property
    def result_bundle_path(self) -> Optional[str]:
        """
        Path where the resulting XCTest bundle should be stored.
        """
        return self.get_capability(RESULT_BUNDLE_PATH)

    @result_bundle_path.setter
    def result_bundle_path(self, value: str) -> None:
        """
        Specify the path to the result bundle path as xcodebuild argument for
        WebDriverAgent build under a security flag. WebDriverAgent process must
        start/stop every time to pick up changed value of this property.
        Specifying useNewWDA to true may help there. Please read 'man xcodebuild'
        for more details.
        """
        self.set_capability(RESULT_BUNDLE_PATH, value)
