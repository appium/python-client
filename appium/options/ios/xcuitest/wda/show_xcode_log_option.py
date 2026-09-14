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

SHOW_XCODE_LOG = 'showXcodeLog'


class ShowXcodeLogOption(SupportsCapabilities):
    @property
    def show_xcode_log(self) -> Optional[bool]:
        """
        Whether to display the output of the Xcode command used to run the tests.
        """
        return self.get_capability(SHOW_XCODE_LOG)

    @show_xcode_log.setter
    def show_xcode_log(self, value: bool) -> None:
        """
        Whether to display the output of the Xcode command used to run the tests in
        server logs. If this is true, there will be lots of extra logging at startup.
        Defaults to false.
        """
        self.set_capability(SHOW_XCODE_LOG, value)
