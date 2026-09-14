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

NATIVE_WEB_SCREENSHOT = 'nativeWebScreenshot'


class NativeWebScreenshotOption(SupportsCapabilities):
    @property
    def native_web_screenshot(self) -> Optional[bool]:
        """
        Whether to use native screenshots in web view context.
        """
        return self.get_capability(NATIVE_WEB_SCREENSHOT)

    @native_web_screenshot.setter
    def native_web_screenshot(self, value: bool) -> None:
        """
        Whether to use screenshoting endpoint provided by UiAutomator framework (true)
        rather than the one provided by chromedriver (false, the default value).
        Use it when you experience issues with the latter.
        """
        self.set_capability(NATIVE_WEB_SCREENSHOT, value)
