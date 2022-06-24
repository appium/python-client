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

WDA_BASE_URL = 'wdaBaseUrl'


class WdaBaseUrlOption(SupportsCapabilities):
    @property
    def wda_base_url(self) -> Optional[str]:
        """
        Prefix to build a custom WebDriverAgent URL.
        """
        return self.get_capability(WDA_BASE_URL)

    @wda_base_url.setter
    def wda_base_url(self, value: str) -> None:
        """
        This value, if specified, will be used as a prefix to build a custom
        WebDriverAgent url. It is different from webDriverAgentUrl, because
        if the latter is set then it expects WebDriverAgent to be already
        listening and skips the building phase. Defaults to http://localhost.
        """
        self.set_capability(WDA_BASE_URL, value)
