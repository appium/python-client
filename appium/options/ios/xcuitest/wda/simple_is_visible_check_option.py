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

SIMPLE_IS_VISIBLE_CHECK = 'simpleIsVisibleCheck'


class SimpleIsVisibleCheckOption(SupportsCapabilities):
    @property
    def simple_is_visible_check(self) -> Optional[bool]:
        """
        Whether to use native methods for determining visibility of elements.
        """
        return self.get_capability(SIMPLE_IS_VISIBLE_CHECK)

    @simple_is_visible_check.setter
    def simple_is_visible_check(self, value: bool) -> None:
        """
        Use native methods for determining visibility of elements.
        In some cases this takes a long time. Setting this capability to false will
        cause the system to use the position and size of elements to make sure they
        are visible on the screen. This can, however, lead to false results in some
        situations. Defaults to false, except iOS 9.3, where it defaults to true.
        """
        self.set_capability(SIMPLE_IS_VISIBLE_CHECK, value)
