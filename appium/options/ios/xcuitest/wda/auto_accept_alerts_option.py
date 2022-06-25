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

AUTO_ACCEPT_ALERTS = 'autoAcceptAlerts'


class AutoAcceptAlertsOption(SupportsCapabilities):
    @property
    def auto_accept_alerts(self) -> Optional[bool]:
        """
        Whether to accept all alerts automatically.
        """
        return self.get_capability(AUTO_ACCEPT_ALERTS)

    @auto_accept_alerts.setter
    def auto_accept_alerts(self, value: bool) -> None:
        """
        Accept all iOS alerts automatically if they pop up. This includes privacy
        access permission alerts (e.g., location, contacts, photos). Default is false.
        """
        self.set_capability(AUTO_ACCEPT_ALERTS, value)
