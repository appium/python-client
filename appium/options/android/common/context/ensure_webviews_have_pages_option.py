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

ENSURE_WEBVIEWS_HAVE_PAGES = 'ensureWebviewsHavePages'


class EnsureWebviewsHavePagesOption(SupportsCapabilities):
    @property
    def ensure_webviews_have_pages(self) -> Optional[bool]:
        """
        Whether to ensure if web views have pages.
        """
        return self.get_capability(ENSURE_WEBVIEWS_HAVE_PAGES)

    @ensure_webviews_have_pages.setter
    def ensure_webviews_have_pages(self, value: bool) -> None:
        """
        Whether to skip web views that have no pages from being shown in getContexts
        output. The driver uses devtools connection to retrieve the information about
        existing pages. true by default since Appium 1.19.0, false if lower than 1.19.0.
        """
        self.set_capability(ENSURE_WEBVIEWS_HAVE_PAGES, value)
