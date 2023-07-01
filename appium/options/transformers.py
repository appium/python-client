from datetime import timedelta
from typing import Any, TypeVar

RT = TypeVar("RT")
VT = TypeVar("VT")

class DurationTransformer:
    @staticmethod
    def transform_duration_get(value: Any) -> RT:
        """Transfroms the value into timedelta"""
        return None if value is None else timedelta(milliseconds=value)
    
    @staticmethod
    def transform_duration_set(value: VT) -> Any:
        return int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value