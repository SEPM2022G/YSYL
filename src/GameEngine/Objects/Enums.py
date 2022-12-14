from enum import Enum

class Orientation(int, Enum):
    FLAT = 0
    STANDING = 1

class Color(int, Enum):
    WHITE = 0
    BLACK = 1

class Difficulty(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2