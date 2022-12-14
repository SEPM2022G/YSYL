from src.GameEngine.Components.StateManager import StateManager
from src.GameEngine.Objects.Piece import Piece
from src.GameEngine.Objects.Enums import Orientation, Color


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


sm = StateManager()


def test_1_init_condition():
    state = sm.get_state()
    assert state["white_pieces_pile"] == 21
    assert state["black_pieces_pile"] == 21

def test_2_piece_from_pile():
    state = sm.update_state(move)
    x = move["des"]["pos_x"]
    y = move["des"]["pos_y"]
    assert state["board"][x][y][0] == Piece(Orientation.FLAT, Color.WHITE)

def test_3_piece_on_piece():
    state = sm.update_state(move)
    state = sm.update_state(move)
    x = move["des"]["pos_x"]
    y = move["des"]["pos_y"]
    assert state["board"][x][y][0] == Piece(Orientation.FLAT, Color.WHITE)
    assert state["board"][x][y][1] == Piece(Orientation.FLAT, Color.WHITE)

def test_4_first_turn():
    x = move["des"]["pos_x"] = 1 
    y = move["des"]["pos_y"] = 1
    move["first_turn"] = True
    state = sm.update_state(move)
    assert state["board"][x][y][0] == Piece(Orientation.FLAT, Color.BLACK)
    move["color"] = Color.BLACK
    state = sm.update_state(move)
    assert state["board"][x][y][1] == Piece(Orientation.FLAT, Color.WHITE)
    move["first_turn"] = False

def test_5_move_stack():
    move["des"]["pos_x"] = 0
    move["des"]["pos_y"] = 1
    move["color"] = Color.WHITE
    state = sm.update_state(move)
    state = sm.update_state(move)
    state = sm.update_state(move)

    move["src"]["pile"] = False
    move["pieces"] = 2
    src_x = move["src"]["pos_x"] = 0
    src_y = move["src"]["pos_y"] = 1
    des_x = move["des"]["pos_x"] = 0
    des_y = move["des"]["pos_y"] = 2
    state = sm.update_state(move)

    assert state["board"][des_x][des_y][0] == Piece(Orientation.FLAT, Color.WHITE)
    assert state["board"][des_x][des_y][1] == Piece(Orientation.FLAT, Color.WHITE)
    assert state["board"][src_x][src_y][0] == Piece(Orientation.FLAT, Color.WHITE)
    assert state["board"][src_x][src_y][1] == 0
    assert state["board"][src_x][src_y][2] == 0

