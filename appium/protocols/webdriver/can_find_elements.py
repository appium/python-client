#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import TYPE_CHECKING, Dict, List, Union

from ..protocol import Protocol

if TYPE_CHECKING:
    from appium.webdriver.webelement import WebElement


class CanFindElements(Protocol):
    def find_element(self, by: str, value: Union[str, Dict, None] = None) -> 'WebElement':
        ...

    def find_elements(self, by: str, value: Union[str, Dict, None] = None) -> List['WebElement']:
        ...
