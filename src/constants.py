from enum import Enum


class Notification(Enum):
    NORMAL = "Keep it up. You playing like a there is no tomorrow!"
    ERROR = "A error occurred"
    INVALID_MOVE = "The move is not valid, try again"
    VICTORY = "You won :)"
    LOSS = "You lost :("


class Turn(Enum):
    WHITE = "White"
    BLACK = "Black"


class Piece(Enum):
    BS = "⯊"  # BLACK_STANDING
    WS = "◠"  # WHITE_STANDING
    BL = "▬"  # BLACK_LYING
    WL = "▭"  # WHITE_LYING


class SelectedOption(Enum):
    lying = "Layout lying piece"
    standing = "Layout standing piece"
    stack = "Move stack"
