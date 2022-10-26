from enum import Enum

DIM = 5  # The dimension of the board, i.e. 5x5


class Notification(Enum):
    NORMAL = "Keep it up. You are playing like a there is no tomorrow!"
    ERROR = "A error occurred"
    INVALID_MOVE = "The move is not valid, try again"
    AI_THINKING = "The ai is thinking..."
    VICTORY = "You won :)"
    LOSS = "You lost :("


class Turn(Enum):
    WHITE = "White"
    BLACK = "Black"


class PlayerType(Enum):
    AI = "AI"
    PLAYER1 = "Player 1"
    PLAYER2 = "Player 2"


class Piece(Enum):
    BS = "⯊"  # BLACK_STANDING
    WS = "◠"  # WHITE_STANDING
    BL = "▬"  # BLACK_LYING
    WL = "▭"  # WHITE_LYING


class SelectedOption(Enum):
    # TODO: should be capital letters
    lying = "Place a laying piece"
    standing = "Place a standing piece"
    rotate = "Rotate a piece"
    stack = "Move a stack"
    move = "Move a piece"
