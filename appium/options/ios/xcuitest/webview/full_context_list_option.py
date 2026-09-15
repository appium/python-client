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

FULL_CONTEXT_LIST = 'fullContextList'


class FullContextListOption(SupportsCapabilities):
    @property
    def full_context_list(self) -> Optional[bool]:
        """
        Whether to return the detailed information on contexts for the get available
        context command.
        """
        return self.get_capability(FULL_CONTEXT_LIST)

    @full_context_list.setter
    def full_context_list(self, value: bool) -> None:
        """
        Sets to return the detailed information on contexts for the get available
        context command. If this capability is enabled, then each item in the returned
        contexts list would additionally include WebView title, full URL and the bundle
        identifier. Defaults to false.
        """
        self.set_capability(FULL_CONTEXT_LIST, value)
