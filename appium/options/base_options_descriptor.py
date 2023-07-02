from typing import Any, TypeVar, Generic, Type, Callable, Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

R = TypeVar('R')
V = TypeVar('V')
C = TypeVar('C', bound='SupportsCapabilities')

class OptionsDescriptor(Generic[R, V]):
    """Generic Descriptor class which calls get_capability and set_capability:
    without transforming the values

    If transformation method is passed, get_capability and set_capability:
    method will be called with transformed value.
    """
    def __init__(self, name: str,
                 tget: Optional[Callable[[Any], R]] = None, 
                 tset: Optional[Callable[[V], Any]] = None) -> None:
        self.name = name
        self.tget = tget
        self.tset = tset

    def __get__(self, obj: C, cls: Type[C]) -> R:
        value = obj.get_capability(self.name)
        if not self.tget is None:
            # transform the value and then return
            return self.tget(value)
        return value

    def __set__(self, obj: C, value: V) -> None:
        if not self.tset is None:
            # transform the value before setting
            transformed_value = self.tset(value)
        obj.set_capability(self.name, transformed_value)