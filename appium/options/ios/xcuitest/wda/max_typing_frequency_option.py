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

MAX_TYPING_FREQUENCY = 'maxTypingFrequency'


class MaxTypingFrequencyOption(SupportsCapabilities):
    @property
    def max_typing_frequency(self) -> Optional[int]:
        """
        The number of keystrokes per minute.
        """
        return self.get_capability(MAX_TYPING_FREQUENCY)

    @max_typing_frequency.setter
    def max_typing_frequency(self, value: int) -> None:
        """
        Maximum frequency of keystrokes for typing and clear. If your tests
        are failing because of typing errors, you may want to adjust this.
        Defaults to 60 keystrokes per minute.
        """
        self.set_capability(MAX_TYPING_FREQUENCY, value)
