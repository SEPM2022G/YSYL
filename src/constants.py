from enum import Enum

DIM = 5  # The dimension of the board, i.e. 5x5


class Notification(Enum):
    NORMAL = "Keep it up. You are playing like a there is no tomorrow!"
    ERROR = "A error occurred"
    INVALID_MOVE = "The move is not valid, try again"
    AI_THINKING = "The ai is thinking..."
    VICTORY = "You won :), press q to quit"
    LOSS = "You lost :(, press q to quit"


class Turn(Enum):
    WHITE = "White"
    BLACK = "Black"


class PlayerType(Enum):
    AI = "AI"
    PLAYER1 = "Player 1"
    PLAYER2 = "Player 2"


class Piece(Enum):
    BS =  "\U0001F537" # "⯊"  # BLACK_STANDING
    WS =  "\U0001F536" # "◠"  # WHITE_STANDING
    BL =  "\U0001F535" # "▬"  # BLACK_LYING
    WL =  "\U0001F7E0" # "▭"  # WHITE_LYING


class SelectedOption(Enum):
    lying = "Place a laying piece"
    standing = "Place a standing piece"
    rotate = "Rotate a piece"
    stack = "Move a stack"
    move = "Move a piece"
