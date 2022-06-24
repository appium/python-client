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

INCLUDE_SAFARI_IN_WEBVIEWS = 'includeSafariInWebviews'


class IncludeSafariInWebviewsOption(SupportsCapabilities):
    @property
    def include_safari_in_webviews(self) -> Optional[bool]:
        """
        Whether to add Safari web views to the list of contexts available
        during a native/webview app test.
        """
        return self.get_capability(INCLUDE_SAFARI_IN_WEBVIEWS)

    @include_safari_in_webviews.setter
    def include_safari_in_webviews(self, value: bool) -> None:
        """
        Add Safari web contexts to the list of contexts available during a
        native/webview app test. This is useful if the test opens Safari and
        needs to be able to interact with it. Defaults to false.
        """
        self.set_capability(INCLUDE_SAFARI_IN_WEBVIEWS, value)
