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

from appium.options.common.supports_capabilities import SupportsCapabilities

SMOOTH_POINTER_MOVE = 'smoothPointerMove'


class SmoothPointerMoveOption(SupportsCapabilities):
    @property
    def smooth_pointer_move(self) -> str | None:
        """
        Easing curve used for mouse pointer moves.
        """
        return self.get_capability(SMOOTH_POINTER_MOVE)

    @smooth_pointer_move.setter
    def smooth_pointer_move(self, value: str) -> None:
        """
        Set the easing curve for mouse pointer moves, such as 'linear', 'ease',
        'ease-in', 'ease-out', 'ease-in-out', or 'cubic-bezier(x1,y1,x2,y2)'.
        """
        self.set_capability(SMOOTH_POINTER_MOVE, value)
