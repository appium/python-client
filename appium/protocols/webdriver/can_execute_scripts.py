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

from typing import Any, List, Optional, Protocol


class CanExecuteScripts(Protocol):
    def pin_script(self, script: str, script_key: Optional[Any] = None) -> Any: ...

    def unpin(self, script_key: Any) -> None: ...

    def get_pinned_scripts(self) -> List[str]: ...

    def execute_script(self, script: str, *args: Any) -> Any: ...

    def execute_async_script(self, script: str, *args: Any) -> Any: ...
