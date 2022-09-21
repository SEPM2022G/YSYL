from enum import Enum


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
