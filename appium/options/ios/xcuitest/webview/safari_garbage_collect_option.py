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

SAFARI_GARBAGE_COLLECT = 'safariGarbageCollect'


class SafariGarbageCollectOption(SupportsCapabilities):
    @property
    def safari_garbage_collect(self) -> Optional[bool]:
        """
        Whether to turn on garbage collection when executing scripts on Safari.
        """
        return self.get_capability(SAFARI_GARBAGE_COLLECT)

    @safari_garbage_collect.setter
    def safari_garbage_collect(self, value: bool) -> None:
        """
        Turns on/off Web Inspector garbage collection when executing scripts on Safari.
        Turning on may improve performance. Defaults to false.
        """
        self.set_capability(SAFARI_GARBAGE_COLLECT, value)
