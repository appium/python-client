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

from typing import Any, Dict, Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

WEBKIT_WEBRTC = 'webkit:WebRTC'


class WebkitWebrtcOption(SupportsCapabilities):
    @property
    def webkit_webrtc(self) -> Optional[Dict[str, Any]]:
        """
        WebRTC policies.
        """
        return self.get_capability(WEBKIT_WEBRTC)

    @webkit_webrtc.setter
    def webkit_webrtc(self, value: Dict[str, Any]) -> None:
        """
        This option allows a test to temporarily change Safari's policies
        for WebRTC and Media Capture.
        The following dictionary values are supported:
        - DisableInsecureMediaCapture: Boolean value.
        Normally, Safari refuses to allow media capture over insecure connections.
        This restriction is relaxed by default for WebDriver sessions for testing
        purposes (for example, a test web server not configured for HTTPS). When
        this capability is specified, Safari will revert to the normal behavior of
        preventing media capture over insecure connections.
        - DisableICECandidateFiltering: Boolean value.
        To protect a user's privacy, Safari normally filters out WebRTC
        ICE candidates that correspond to internal network addresses when
        capture devices are not in use. This capability suppresses ICE candidate
        filtering so that both internal and external network addresses are
        always sent as ICE candidates.
        """
        self.set_capability(WEBKIT_WEBRTC, value)
