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

NO_SIGN = 'noSign'


class NoSignOption(SupportsCapabilities):
    @property
    def no_sign(self) -> Optional[bool]:
        """
        Whether to skip application signing.
        """
        return self.get_capability(NO_SIGN)

    @no_sign.setter
    def no_sign(self, value: bool) -> None:
        """
        Set it to true in order to skip application signing. By default
        all apps are always signed with the default Appium debug signature
        if they don't have any. This capability cancels all the signing checks
        and makes the driver to use the application package as is. This option
        does not affect .apks packages as these are expected to be already signed.
        """
        self.set_capability(NO_SIGN, value)
