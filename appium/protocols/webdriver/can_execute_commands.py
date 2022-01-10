from selenium.webdriver.remote.remote_connection import RemoteConnection

from ..protocol import Protocol


class CanExecuteCommands(Protocol):
    command_executor: RemoteConnection

    def execute(self, driver_command: str, params: dict = None) -> dict:
        ...
