from datetime import timedelta
from typing import Any, TypeVar, Generic, Type

from appium.options.common.supports_capabilities import SupportsCapabilities

T = TypeVar('T')
C = TypeVar('C', bound='SupportsCapabilities')

class OptionsDescriptor(Generic[T]):
    """Generic Descriptor class which calls get_capability and set_capability:
    without transforming the values

    If transformation method is passed, get_capability and set_capability:
    method will be called with transformed value
    """
    def __init__(self, name: str, tget=None, tset=None) -> None:
        self.name = name
        self.tget = tget
        self.tset = tset

    def __get__(self, obj: C, cls: Type[C]) -> Any:
        value = obj.get_capability(self.name)
        if self.tget:
            # transform the value and then return
            return self.tget(obj, value)
        return value

    def __set__(self, obj: C, value: Any) -> None:
        if self.tset:
            # transform the value before setting
            value = self.tset(obj, value)
        obj.set_capability(self.name, value)

def transform_get(self, value):
    """Transfroms the value into timedelta"""
    return None if value is None else timedelta(milliseconds=value)

def transform_set(self, value):
    return int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value