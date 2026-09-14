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

XCODE_ORG_ID = 'xcodeOrgId'


class XcodeOrgIdOption(SupportsCapabilities):
    @property
    def xcode_org_id(self) -> Optional[str]:
        """
        Signing certificate organization id for WebDriverAgent compilation.
        """
        return self.get_capability(XCODE_ORG_ID)

    @xcode_org_id.setter
    def xcode_org_id(self, value: str) -> None:
        """
        Provides a signing certificate organization id for WebDriverAgent compilation.
        If signing id is not provided then it defaults to "iPhone Developer"
        """
        self.set_capability(XCODE_ORG_ID, value)
