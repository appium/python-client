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

ALLOW_TEST_PACKAGES = 'allowTestPackages'


class AllowTestPackagesOption(SupportsCapabilities):
    @property
    def allow_test_packages(self) -> Optional[bool]:
        """
        Whether it is possible to use packages built with the test flag for
        the automated testing (literally adds -t flag to the adb install command).
        """
        return self.get_capability(ALLOW_TEST_PACKAGES)

    @allow_test_packages.setter
    def allow_test_packages(self, value: bool) -> None:
        """
        If set to true then it would be possible to use packages built with the test flag for
        the automated testing (literally adds -t flag to the adb install command). false by default.
        """
        self.set_capability(ALLOW_TEST_PACKAGES, value)
