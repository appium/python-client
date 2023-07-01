from typing import Any, TypeVar, Generic, Type, Callable, Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

RT = TypeVar("RT")
VT = TypeVar("VT")
C = TypeVar('C', bound='SupportsCapabilities')

class OptionsDescriptor(Generic[RT, VT]):
    """Generic Descriptor class which calls get_capability and set_capability:
    without transforming the values

    If transformation method is passed, get_capability and set_capability:
    method will be called with transformed value
    """
    def __init__(self, name: str, 
                 tget: Optional[Callable[[Any], RT]] = None, 
                 tset: Optional[Callable[[VT], Any]] = None) -> None:
        self.name = name
        self.tget = tget
        self.tset = tset

    def __get__(self, obj: C, cls: Type[C]) -> RT:
        value = obj.get_capability(self.name)
        if self.tget:
            # transform the value and then return
            return self.tget(obj, value)
        return value

    def __set__(self, obj: C, value: VT) -> None:
        if self.tset:
            # transform the value before setting
            transformed_value = self.tset(obj, value)
        obj.set_capability(self.name, transformed_value)