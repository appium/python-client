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

EXTRACT_CHROME_ANDROID_PACKAGE_FROM_CONTEXT_NAME = 'extractChromeAndroidPackageFromContextName'


class ExtractChromeAndroidPackageFromContextNameOption(SupportsCapabilities):
    @property
    def extract_chrome_android_package_from_context_name(self) -> Optional[bool]:
        """
        Whether to use the android package identifier associated with the context name.
        """
        return self.get_capability(EXTRACT_CHROME_ANDROID_PACKAGE_FROM_CONTEXT_NAME)

    @extract_chrome_android_package_from_context_name.setter
    def extract_chrome_android_package_from_context_name(self, value: bool) -> None:
        """
        If set to true, tell chromedriver to attach to the android package we have associated
        with the context name, rather than the package of the application under test.
        false by default.
        """
        self.set_capability(EXTRACT_CHROME_ANDROID_PACKAGE_FROM_CONTEXT_NAME, value)
