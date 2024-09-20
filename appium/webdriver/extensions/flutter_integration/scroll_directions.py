from enum import Enum

class ScrollDirection(Enum):
    UP = 'up'
    DOWN = 'down'
    
    def as_string(self):
        return str(self.value)