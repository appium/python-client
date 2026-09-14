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

SCREENSHOT_QUALITY = 'screenshotQuality'


class ScreenshotQualityOption(SupportsCapabilities):
    @property
    def screenshot_quality(self) -> Optional[int]:
        """
        Screenshot quality value.
        """
        return self.get_capability(SCREENSHOT_QUALITY)

    @screenshot_quality.setter
    def screenshot_quality(self, value: int) -> None:
        """
        Changes the quality of phone display screenshots following
        xctest/xctimagequality Default value is 1. 0 is the highest and
        2 is the lowest quality. You can also change it via settings
        command. 0 might cause OutOfMemory crash on high-resolution
        devices like iPad Pro.
        """
        self.set_capability(SCREENSHOT_QUALITY, value)
