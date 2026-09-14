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

from typing import List, Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

ADDITIONAL_WEBVIEW_BUNDLE_IDS = 'additionalWebviewBundleIds'


class AdditionalWebviewBundleIdsOption(SupportsCapabilities):
    @property
    def additional_webview_bundle_ids(self) -> Optional[List[str]]:
        """
        Array of possible bundle identifiers for webviews.
        """
        return self.get_capability(ADDITIONAL_WEBVIEW_BUNDLE_IDS)

    @additional_webview_bundle_ids.setter
    def additional_webview_bundle_ids(self, value: List[str]) -> None:
        """
        Array of possible bundle identifiers for webviews. This is sometimes
        necessary if the Web Inspector is found to be returning a modified
        bundle identifier for the app. Defaults to [].
        """
        self.set_capability(ADDITIONAL_WEBVIEW_BUNDLE_IDS, value)
