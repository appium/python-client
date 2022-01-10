from typing import TYPE_CHECKING, Dict, List, Union

from ..protocol import Protocol

if TYPE_CHECKING:
    from appium.webdriver.webelement import WebElement


class CanFindElements(Protocol):
    def find_element(self, by: str, value: Union[str, Dict] = None) -> 'WebElement':
        ...

    def find_elements(self, by: str, value: Union[str, Dict] = None) -> List['WebElement']:
        ...
