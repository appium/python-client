from typing import Optional, Union
from datetime import timedelta

def transform_duration_get(value: Optional[int]) -> Optional[timedelta]:
    """Transfroms the value into timedelta"""
    return None if value is None else timedelta(milliseconds=value)
    
def transform_duration_set(value: Union[timedelta, int]) -> int:
    return int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value
