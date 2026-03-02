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

from typing import Any, List, Optional, Protocol, TYPE_CHECKING
from warnings import deprecated


class CanExecuteScripts(Protocol):
    def execute_script(self, script: str, *args: Any) -> Any: ...

    # TODO: remove `if not TYPE_CHECKING` guard after properly implement them
    # The use of these methods will produce DeprecationWarnings at runtime
    if not TYPE_CHECKING:
        @deprecated("pin_script is deprecated for removal")
        def pin_script(self, script: str, script_key: Optional[Any] = None) -> Any: ...

        @deprecated("unpin is deprecated for removal")
        def unpin(self, script_key: Any) -> None: ...

        @deprecated("get_pinned_scripts is deprecated for removal")
        def get_pinned_scripts(self) -> List[str]: ...

        @deprecated("execute_async_script is deprecated for removal")
        def execute_async_script(self, script: str, *args: Any) -> Any: ...
