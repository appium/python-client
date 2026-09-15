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

SIMULATOR_PASTEBOARD_AUTOMATIC_SYNC = 'simulatorPasteboardAutomaticSync'


class SimulatorPasteboardAutomaticSyncOption(SupportsCapabilities):
    @property
    def simulator_pasteboard_automatic_sync(self) -> Optional[bool]:
        """
        Pasteboard automation sync state.
        """
        return self.get_capability(SIMULATOR_PASTEBOARD_AUTOMATIC_SYNC)

    @simulator_pasteboard_automatic_sync.setter
    def simulator_pasteboard_automatic_sync(self, value: bool) -> None:
        """
        Handle the -PasteboardAutomaticSync flag when simulator process launches.
        It could improve launching simulator performance not to sync pasteboard with
        the system when this value is off. on forces the flag enabled. system does
        not provide the flag to the launching command. on, off, or system is available.
        They are case-insensitive. Defaults to off.
        """
        self.set_capability(SIMULATOR_PASTEBOARD_AUTOMATIC_SYNC, value)
