from enum import Enum

class Orientation(Enum):
    FLAT = 0
    STANDING = 1

class Color(Enum):
    WHITE = 0
    BLACK = 1

    def isWhite(self, obj): {
        self.WHITE.value == obj.value
    }