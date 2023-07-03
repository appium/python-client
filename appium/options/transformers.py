from datetime import timedelta
from typing import Optional, Union


def transform_duration_get(value: Optional[int]) -> Optional[timedelta]:
    """Transfroms the value into timedelta"""
    return None if value is None else timedelta(milliseconds=value)


def transform_duration_set(value: Union[timedelta, int]) -> int:
    return int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value


def transform_duration_in_seconds_get(value: Optional[float]) -> Optional[timedelta]:
    return None if value is None else timedelta(seconds=value)


def transform_duration_in_seconds_set(value: Union[timedelta, float]) -> Union[int, float]:
    return value.total_seconds() if isinstance(value, timedelta) else value
