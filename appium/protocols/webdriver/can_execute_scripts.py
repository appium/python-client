from typing import Any, List, Optional

from ..protocol import Protocol


class CanExecuteScripts(Protocol):
    def pin_script(self, script: str, script_key: Optional[Any] = None) -> Any:
        ...

    def unpin(self, script_key: Any) -> None:
        ...

    def get_pinned_scripts(self) -> List[str]:
        ...

    def execute_script(self, script: str, *args: Any) -> Any:
        ...

    def execute_async_script(self, script: str, *args: Any) -> Any:
        ...
