from enum import Enum

class ScrollDirection(Enum):
    UP = 'up'
    DOWN = 'down'
    
    def as_string(self) -> str:
        return str(self.value)