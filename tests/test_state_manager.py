import sys
sys.path.append("..") # Adds higher directory to python modules path.
from src.GameEngine.Components import StateManager as SM
from src.GameEngine.Enums import Orientation, Color

move = {
    "src": {
        "pile": True,
        "pos_x": 1,
        "pos_y": 1,
    },
    "des": {
        "pos_x": 0,
        "pos_y": 0,
        "orientation": Orientation.FLAT
    },
    "pieces": 1,
    "color": Color.WHITE,
    "first_turn": False
}



sm = SM.StateManager()

###initial state condition
state = sm.get_state()
assert(state["black_pieces"] == 21)
assert(state["white_pieces"] == 21)
#sm.print_state()

###Move piece from pile
state = sm.update_state(move)
x = move["des"]["pos_x"]
y = move["des"]["pos_y"]
assert(state["board"][x][y][0] != 0)
#sm.print_state()

###Piece on piece
x = move["des"]["pos_x"]
y = move["des"]["pos_y"]
assert(state["board"][x][y][1] != 0)
#sm.print_state()

###First turn
move["des"]["pos_x"] = 1
move["des"]["pos_y"] = 1
move["color"] = 1



sm.update_state(move)
sm.print_state()

