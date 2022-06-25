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

ABSOLUTE_WEB_LOCATIONS = 'absoluteWebLocations'


class AbsoluteWebLocationsOption(SupportsCapabilities):
    @property
    def absolute_web_locations(self) -> Optional[bool]:
        """
        Whether Get Element Location returns coordinates
        relative to the page origin for web view elements.
        """
        return self.get_capability(ABSOLUTE_WEB_LOCATIONS)

    @absolute_web_locations.setter
    def absolute_web_locations(self, value: bool) -> None:
        """
        This capability will direct the Get Element Location command, when used
        within webviews, to return coordinates which are relative to the origin of
        the page, rather than relative to the current scroll offset. This capability
        has no effect outside of webviews. Defaults to  false.
        """
        self.set_capability(ABSOLUTE_WEB_LOCATIONS, value)
