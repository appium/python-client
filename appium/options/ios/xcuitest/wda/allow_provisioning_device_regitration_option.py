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

ALLOW_PROVISIONING_DEVICE_REGISTRATION = 'allowProvisioningDeviceRegistration'


class AllowProvisioningDeviceRegistrationOption(SupportsCapabilities):
    @property
    def allow_provisioning_device_registration(self) -> Optional[bool]:
        """
        Whether to allow xcodebuild to register your destination device on the developer portal.
        """
        return self.get_capability(ALLOW_PROVISIONING_DEVICE_REGISTRATION)

    @allow_provisioning_device_registration.setter
    def allow_provisioning_device_registration(self, value: bool) -> None:
        """
        Allow xcodebuild to register your destination device on the developer portal
        if necessary. Requires a developer account to have been added in Xcode's Accounts
        preference pane. Defaults to false.
        """
        self.set_capability(ALLOW_PROVISIONING_DEVICE_REGISTRATION, value)
