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

from .supports_capabilities import SupportsCapabilities

SKIP_LOG_CAPTURE = 'skipLogCapture'


class SkipLogCaptureOption(SupportsCapabilities):
    @property
    def skip_log_capture(self) -> Optional[bool]:
        """
        Whether the driver should not record device logs.
        """
        return self.get_capability(SKIP_LOG_CAPTURE)

    @skip_log_capture.setter
    def skip_log_capture(self, value: bool) -> None:
        """
        Set whether the driver should not record device logs.
        """
        self.set_capability(SKIP_LOG_CAPTURE, value)
