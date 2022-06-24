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

SCALE_FACTOR = 'scaleFactor'


class ScaleFactorOption(SupportsCapabilities):
    @property
    def scale_factor(self) -> Optional[str]:
        """
        Simulator scale factor.
        """
        return self.get_capability(SCALE_FACTOR)

    @scale_factor.setter
    def scale_factor(self, value: str) -> None:
        """
        Simulator scale factor. This is useful to have if the default resolution
        of simulated device is greater than the actual display resolution.
        So you can scale the simulator to see the whole device screen without scrolling.
        Acceptable values for simulators running Xcode SDK 8 and older are: '1.0',
        '0.75', '0.5', '0.33' and '0.25', where '1.0' means 100% scale.
        For simulators running Xcode SDK 9 and above the value could be any valid
        positive float number.
        """
        self.set_capability(SCALE_FACTOR, value)
