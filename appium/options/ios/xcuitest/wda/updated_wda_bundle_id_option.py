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

UPDATED_WDA_BUNDLE_ID = 'updatedWDABundleId'


class UpdatedWdaBundleIdOption(SupportsCapabilities):
    @property
    def updated_wda_bundle_id(self) -> Optional[str]:
        """
        WDA bundle identifier.
        """
        return self.get_capability(UPDATED_WDA_BUNDLE_ID)

    @updated_wda_bundle_id.setter
    def updated_wda_bundle_id(self, value: str) -> None:
        """
        Bundle id to update WDA to before building and launching on real devices.
        This bundle id must be associated with a valid provisioning profile.
        """
        self.set_capability(UPDATED_WDA_BUNDLE_ID, value)
