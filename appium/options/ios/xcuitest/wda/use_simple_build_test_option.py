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

USE_SIMPLE_BUILD_TEST = 'useSimpleBuildTest'


class UseSimpleBuildTestOption(SupportsCapabilities):
    @property
    def use_simple_build_test(self) -> Optional[bool]:
        """
        Whether to enforce app termination on session quit.
        """
        return self.get_capability(USE_SIMPLE_BUILD_TEST)

    @use_simple_build_test.setter
    def use_simple_build_test(self, value: bool) -> None:
        """
        Build with 'build' and run test with 'test' in xcodebuild for all Xcode versions if
        this is true, or build with 'build-for-testing' and run tests with
        'test-without-building' for over Xcode 8 if this is false. Defaults to false.
        """
        self.set_capability(USE_SIMPLE_BUILD_TEST, value)
