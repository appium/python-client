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

MJPEG_SCREENSHOT_URL = 'mjpegScreenshotUrl'


class MjpegScreenshotUrlOption(SupportsCapabilities):
    @property
    def mjpeg_screenshot_url(self) -> Optional[str]:
        """
        URL of a service that provides realtime device screenshots in MJPEG format.
        """
        return self.get_capability(MJPEG_SCREENSHOT_URL)

    @mjpeg_screenshot_url.setter
    def mjpeg_screenshot_url(self, value: str) -> None:
        """
        The URL of a service that provides realtime device screenshots in MJPEG format.
        If provided then the actual command to retrieve a screenshot will be
        requesting pictures from this service rather than directly from the server.
        """
        self.set_capability(MJPEG_SCREENSHOT_URL, value)
