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

import json
from typing import Dict, Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

PERMISSIONS = 'permissions'


class PermissionsOption(SupportsCapabilities):
    @property
    def permissions(self) -> Optional[Dict[str, Dict[str, str]]]:
        """
        Get Simulator permissions.
        """
        value = self.get_capability(PERMISSIONS)
        return None if value is None else json.loads(value)

    @permissions.setter
    def permissions(self, value: Dict[str, Dict[str, str]]) -> None:
        """
        Allows setting of permissions for the specified application bundle on
        Simulator only.

        Since Xcode SDK 11.4 Apple provides native APIs to interact with
        application settings. Check the output of `xcrun simctl privacy booted`
        command to get the list of available permission names. Use yes, no
        and unset as values in order to grant, revoke or reset the corresponding
        permission. Below Xcode SDK 11.4 it is required that applesimutils package
        is installed and available in PATH. The list of available service names
        and statuses can be found at https://github.com/wix/AppleSimulatorUtils.
        For example: {"com.apple.mobilecal": {"calendar": "YES"}}
        """
        self.set_capability(PERMISSIONS, json.dumps(value, ensure_ascii=False))
