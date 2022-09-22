import numpy as np
from src.GameEngine.Components.Validator import Validator
from src.GameEngine.Objects.Piece import Piece
from src.GameEngine.Objects.Outcome import Outcome
from src.GameEngine.Objects.Enums import Orientation, Color
v = Validator()


# Init
def test_init():
    state = {"white_pieces_pile": 21, "black_pieces_pile": 21,
             "board": np.zeros(shape=(5, 5, 42), dtype=object)}
    move = {
        "src": {
            "pile": True,
            "pos_x": 1,
            "pos_y": 1,
        },
        "des": {
            "pos_x": 1,
            "pos_y": 1,
            "orientation": Orientation.FLAT
        },
        "pieces": 1,
        "color": Color.WHITE,
        "first_turn": False
    }
    result = v.check(move, state, state)
    assert (result == Outcome.VALID)


def test_out_of_bounds():
    state = {"white_pieces_pile": 21, "black_pieces_pile": 21,
             "board": np.zeros(shape=(5, 5, 42), dtype=object)}
    move1 = {
        "src": {
            "pile": False,
            "pos_x": 0,
            "pos_y": 0,
        },
        "des": {
            "pos_x": 1,
            "pos_y": 1,
            "orientation": Orientation.FLAT
        },
        "pieces": 1,
        "color": Color.WHITE,
        "first_turn": False
    }
    result = v.check(move1, state, state)
    assert (result == Outcome.INVALID)

    move2 = {
        "src": {
            "pile": False,
            "pos_x": 6,
            "pos_y": 5,
        },
        "des": {
            "pos_x": 1,
            "pos_y": 1,
            "orientation": Orientation.FLAT
        },
        "pieces": 1,
        "color": Color.WHITE,
        "first_turn": False
    }
    result = v.check(move2, state, state)
    assert (result == Outcome.INVALID)

    move3 = {
        "src": {
            "pile": False,
            "pos_x": 1,
            "pos_y": 1,
        },
        "des": {
            "pos_x": 6,
            "pos_y": 6,
            "orientation": Orientation.FLAT
        },
        "pieces": 1,
        "color": Color.WHITE,
        "first_turn": False
    }
    result = v.check(move3, state, state)
    assert (result == Outcome.INVALID)

    move4 = {
        "src": {
            "pile": False,
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
    result = v.check(move4, state, state)
    assert (result == Outcome.INVALID)


def test_invalid_n_pieces():
    state = {"white_pieces_pile": 21, "black_pieces_pile": 21,
             "board": np.zeros(shape=(5, 5, 42), dtype=object)}
    move = {
        "src": {
            "pile": True,
            "pos_x": 1,
            "pos_y": 1,
        },
        "des": {
            "pos_x": 1,
            "pos_y": 1,
            "orientation": Orientation.FLAT
        },
        "pieces": 0,
        "color": Color.WHITE,
        "first_turn": False
    }
    result = v.check(move, state, state)
    assert (result == Outcome.INVALID)


def test_first_turn():
    state = {"white_pieces_pile": 21, "black_pieces_pile": 21,
             "board": np.zeros(shape=(5, 5, 42), dtype=object)}
    move1 = {
        "src": {
            "pile": True,
            "pos_x": 1,
            "pos_y": 1,
        },
        "des": {
            "pos_x": 1,
            "pos_y": 1,
            "orientation": Orientation.FLAT
        },
        "pieces": 1,
        "color": Color.WHITE,
        "first_turn": True
    }
    result = v.check(move1, state, state)
    assert (result == Outcome.INVALID)
    move2 = {
        "src": {
            "pile": False,
            "pos_x": 1,
            "pos_y": 1,
        },
        "des": {
            "pos_x": 1,
            "pos_y": 1,
            "orientation": Orientation.FLAT
        },
        "pieces": 1,
        "color": Color.WHITE,
        "first_turn": True
    }
    result = v.check(move1, state, state)
    assert (result == Outcome.INVALID)
    move3 = {
        "src": {
            "pile": True,
            "pos_x": 1,
            "pos_y": 1,
        },
        "des": {
            "pos_x": 1,
            "pos_y": 1,
            "orientation": Orientation.FLAT
        },
        "pieces": 2,
        "color": Color.WHITE,
        "first_turn": True
    }
    result = v.check(move1, state, state)
    assert (result == Outcome.INVALID)


def test_place_on_wrong_color():
    state = {"white_pieces_pile": 21, "black_pieces_pile": 21,
             "board": np.zeros(shape=(5, 5, 42), dtype=object)}
    state["board"][1][1][0] = Piece(Orientation.FLAT, Color.BLACK)
    move1 = {
        "src": {
            "pile": True,
            "pos_x": 1,
            "pos_y": 1,
        },
        "des": {
            "pos_x": 1,
            "pos_y": 1,
            "orientation": Orientation.FLAT
        },
        "pieces": 1,
        "color": Color.WHITE,
        "first_turn": False
    }
    result = v.check(move1, state, state)
    assert (result == Outcome.INVALID)


def test_place_on_right_color():
    state = {"white_pieces_pile": 21, "black_pieces_pile": 21,
             "board": np.zeros(shape=(5, 5, 42), dtype=object)}
    state["board"][1][1][0] = Piece(Orientation.FLAT, Color.BLACK)
    move1 = {
        "src": {
            "pile": True,
            "pos_x": 1,
            "pos_y": 1,
        },
        "des": {
            "pos_x": 1,
            "pos_y": 1,
            "orientation": Orientation.FLAT
        },
        "pieces": 1,
        "color": Color.BLACK,
        "first_turn": False
    }
    result = v.check(move1, state, state)
    assert (result == Outcome.VALID)


def test_place_on_standing():
    state = {"white_pieces_pile": 21, "black_pieces_pile": 21,
             "board": np.zeros(shape=(5, 5, 42), dtype=object)}
    state["board"][1][1][0] = Piece(Orientation.STANDING, Color.BLACK)
    move1 = {
        "src": {
            "pile": True,
            "pos_x": 1,
            "pos_y": 1,
        },
        "des": {
            "pos_x": 1,
            "pos_y": 1,
            "orientation": Orientation.FLAT
        },
        "pieces": 1,
        "color": Color.BLACK,
        "first_turn": False
    }
    result = v.check(move1, state, state)
    assert (result == Outcome.INVALID)


def test_too_many_pieces():
    state = {"white_pieces_pile": 21, "black_pieces_pile": 1,
             "board": np.zeros(shape=(5, 5, 42), dtype=object)}
    state["board"][1][1][0] = Piece(Orientation.FLAT, Color.BLACK)
    move1 = {
        "src": {
            "pile": True,
            "pos_x": 1,
            "pos_y": 1,
        },
        "des": {
            "pos_x": 1,
            "pos_y": 1,
            "orientation": Orientation.FLAT
        },
        "pieces": 2,
        "color": Color.BLACK,
        "first_turn": False
    }
    result = v.check(move1, state, state)
    assert (result == Outcome.INVALID)


def test_move_stack():
    state = {"white_pieces_pile": 21, "black_pieces_pile": 21,
             "board": np.zeros(shape=(5, 5, 42), dtype=object)}
    state["board"][1][1][0] = Piece(Orientation.FLAT, Color.BLACK)
    state["board"][1][1][1] = Piece(Orientation.FLAT, Color.BLACK)
    state["board"][1][1][2] = Piece(Orientation.FLAT, Color.BLACK)
    move1 = {
        "src": {
            "pile": False,
            "pos_x": 1,
            "pos_y": 1,
        },
        "des": {
            "pos_x": 2,
            "pos_y": 2,
            "orientation": Orientation.FLAT
        },
        "pieces": 3,
        "color": Color.BLACK,
        "first_turn": False
    }
    result = v.check(move1, state, state)
    assert (result == Outcome.VALID)


def test_move_invalid_stack():
    state = {"white_pieces_pile": 21, "black_pieces_pile": 21,
             "board": np.zeros(shape=(5, 5, 42), dtype=object)}
    state["board"][1][1][0] = Piece(Orientation.FLAT, Color.BLACK)
    state["board"][1][1][1] = Piece(Orientation.FLAT, Color.WHITE)
    state["board"][1][1][2] = Piece(Orientation.FLAT, Color.BLACK)
    move1 = {
        "src": {
            "pile": False,
            "pos_x": 1,
            "pos_y": 1,
        },
        "des": {
            "pos_x": 2,
            "pos_y": 2,
            "orientation": Orientation.FLAT
        },
        "pieces": 3,
        "color": Color.BLACK,
        "first_turn": False
    }
    result = v.check(move1, state, state)
    assert (result == Outcome.INVALID)


def test_idle_move():
    state = {"white_pieces_pile": 21, "black_pieces_pile": 21,
             "board": np.zeros(shape=(5, 5, 42), dtype=object)}
    state["board"][1][1][0] = Piece(Orientation.FLAT, Color.BLACK)
    move1 = {
        "src": {
            "pile": False,
            "pos_x": 1,
            "pos_y": 1,
        },
        "des": {
            "pos_x": 1,
            "pos_y": 1,
            "orientation": Orientation.FLAT
        },
        "pieces": 1,
        "color": Color.BLACK,
        "first_turn": False
    }
    result = v.check(move1, state, state)
    assert (result == Outcome.INVALID)


def test_find():
    arr = np.zeros(5, dtype=object)
    assert v._find_top(arr) == -1
    arr[0] = Piece(Orientation.STANDING, Color.BLACK)
    assert v._find_top(arr) == Piece(Orientation.STANDING, Color.BLACK)
    arr[1] = Piece(Orientation.STANDING, Color.WHITE)
    assert v._find_top(arr) == Piece(Orientation.STANDING, Color.WHITE)
    arr[2] = Piece(Orientation.FLAT, Color.WHITE)
    assert v._find_top(arr) == Piece(Orientation.FLAT, Color.WHITE)

# Tests different win conditions


def win_straight(color, orientation, outcome):
    boards = {}
    for n in range(0, 5):
        boards[n] = np.zeros(shape=(5, 5, 42), dtype=object)
        for x in range(0, 5):
            boards[n][x][n][0] = Piece(orientation, color)
        result = v._win_check(boards[n])
        assert (result == outcome)

# Tests turns


def cont_turns(color, orientation):
    boards = []

    board0 = np.zeros(shape=(5, 5, 42), dtype=object)
    boards.append(board0)

    board1 = np.zeros(shape=(5, 5, 42), dtype=object)
    board1[0][0][0] = Piece(orientation, color)
    board1[1][0][0] = Piece(orientation, color)
    board1[2][0][0] = Piece(orientation, color)
    board1[2][1][0] = Piece(orientation, color)
    board1[2][2][0] = Piece(orientation, color)
    board1[3][2][0] = Piece(orientation, color)
    board1[4][2][0] = Piece(orientation, color)
    boards.append(board1)

    board2 = np.zeros(shape=(5, 5, 42), dtype=object)
    board2[0][0][0] = Piece(orientation, color)
    board2[1][0][0] = Piece(orientation, color)
    board2[2][0][0] = Piece(orientation, color)
    board2[2][1][0] = Piece(orientation, color)
    board2[2][2][0] = Piece(orientation, color)
    board2[3][2][0] = Piece(orientation, color)
    board2[4][2][0] = Piece(orientation, color)
    boards.append(board2)

    board3 = np.zeros(shape=(5, 5, 42), dtype=object)
    board3[0][3][0] = Piece(orientation, color)
    board3[1][3][0] = Piece(orientation, color)
    board3[2][2][0] = Piece(orientation, color)
    board3[2][1][0] = Piece(orientation, color)
    board3[2][0][0] = Piece(orientation, color)
    board3[3][0][0] = Piece(orientation, color)
    board3[4][0][0] = Piece(orientation, color)
    boards.append(board3)

    for board in boards:
        result = v._win_check(board)
        assert (result == Outcome.CONT)


def win_turns(color, orientation, outcome):
    boards = []

    board1 = np.zeros(shape=(5, 5, 42), dtype=object)
    board1[0][0][0] = Piece(orientation, color)
    board1[1][0][0] = Piece(orientation, color)
    board1[1][1][0] = Piece(orientation, color)
    board1[2][1][0] = Piece(orientation, color)
    board1[3][1][0] = Piece(orientation, color)
    board1[4][1][0] = Piece(orientation, color)
    boards.append(board1)

    board2 = np.zeros(shape=(5, 5, 42), dtype=object)
    board2[0][4][0] = Piece(orientation, color)
    board2[1][4][0] = Piece(orientation, color)
    board2[1][3][0] = Piece(orientation, color)
    board2[2][3][0] = Piece(orientation, color)
    board2[3][3][0] = Piece(orientation, color)
    board2[4][3][0] = Piece(orientation, color)
    boards.append(board2)

    board3 = np.zeros(shape=(5, 5, 42), dtype=object)
    board3[0][3][0] = Piece(orientation, color)
    board3[1][3][0] = Piece(orientation, color)
    board3[2][4][0] = Piece(orientation, color)
    board3[1][4][0] = Piece(orientation, color)
    board3[3][4][0] = Piece(orientation, color)
    board3[4][4][0] = Piece(orientation, color)
    boards.append(board3)

    for board in boards:
        result = v._win_check(board)
        assert (result == outcome)


def test_win_straight_white_standing():
    win_straight(Color.WHITE, Orientation.STANDING, Outcome.WIN_WHITE)


def test_win_straight_white_flat():
    win_straight(Color.WHITE, Orientation.FLAT, Outcome.WIN_WHITE)


def test_win_straight_black_standing():
    win_straight(Color.BLACK, Orientation.STANDING, Outcome.WIN_BLACK)


def test_win_straight_black_flat():
    win_straight(Color.BLACK, Orientation.FLAT, Outcome.WIN_BLACK)


def test_win_turns_white_standing():
    win_turns(Color.WHITE, Orientation.STANDING, Outcome.WIN_WHITE)


def test_win_turns_white_flat():
    win_turns(Color.WHITE, Orientation.FLAT, Outcome.WIN_WHITE)


def test_win_turns_black_standing():
    win_turns(Color.BLACK, Orientation.STANDING, Outcome.WIN_BLACK)


def test_win_turns_black_flat():
    win_turns(Color.BLACK, Orientation.FLAT, Outcome.WIN_BLACK)


def test_cont_turns_black_flat():
    cont_turns(Color.BLACK, Orientation.FLAT)


def test_cont_turns_black_standing():
    cont_turns(Color.BLACK, Orientation.STANDING)


def test_cont_turns_white_standing():
    cont_turns(Color.WHITE, Orientation.STANDING)


def test_cont_turns_white_flat():
    cont_turns(Color.WHITE, Orientation.FLAT)


def test_cont_mixed_1():
    outcome = Outcome.CONT

    board = np.zeros(shape=(5, 5, 42), dtype=object)
    board[0][0][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][0][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][0][1] = Piece(Orientation.STANDING, Color.BLACK)
    board[2][0][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[3][0][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[4][0][0] = Piece(Orientation.FLAT, Color.BLACK)

    result = v._win_check(board)
    assert (result == outcome)


def test_cont_mixed_2():
    outcome = Outcome.CONT

    board = np.zeros(shape=(5, 5, 42), dtype=object)
    board[0][0][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][0][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][0][1] = Piece(Orientation.FLAT, Color.WHITE)
    board[2][0][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[3][0][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[4][0][0] = Piece(Orientation.FLAT, Color.BLACK)

    result = v._win_check(board)
    assert (result == outcome)


def test_cont_mixed_3():
    outcome = Outcome.CONT
    board = np.zeros(shape=(5, 5, 42), dtype=object)
    board[0][0][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][0][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][0][1] = Piece(Orientation.STANDING, Color.WHITE)
    board[2][0][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[3][0][0] = Piece(Orientation.STANDING, Color.BLACK)
    board[4][0][0] = Piece(Orientation.FLAT, Color.BLACK)
    result = v._win_check(board)
    assert (result == outcome)


def test_cont_diagonal_1():
    outcome = Outcome.CONT

    board = np.zeros(shape=(5, 5, 42), dtype=object)
    board[0][0][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][1][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[2][2][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[3][3][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[4][4][0] = Piece(Orientation.FLAT, Color.BLACK)
    result = v._win_check(board)
    assert (result == outcome)


def test_win_mixed_1():
    outcome = Outcome.WIN_BLACK
    board = np.zeros(shape=(5, 5, 42), dtype=object)

    board[0][4][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][4][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][3][0] = Piece(Orientation.FLAT, Color.WHITE)
    board[1][3][1] = Piece(Orientation.FLAT, Color.BLACK)
    board[2][3][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[3][3][0] = Piece(Orientation.STANDING, Color.BLACK)
    board[3][3][1] = Piece(Orientation.FLAT, Color.BLACK)
    board[4][3][0] = Piece(Orientation.FLAT, Color.BLACK)

    result = v._win_check(board)
    assert (result == outcome)


def test_win_mixed_2():
    outcome = Outcome.WIN_BLACK
    board = np.zeros(shape=(5, 5, 42), dtype=object)

    board[0][4][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][4][0] = Piece(Orientation.STANDING, Color.BLACK)
    board[1][4][1] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][3][0] = Piece(Orientation.FLAT, Color.WHITE)
    board[1][3][1] = Piece(Orientation.STANDING, Color.BLACK)
    board[1][3][2] = Piece(Orientation.FLAT, Color.BLACK)
    board[2][3][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[3][3][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[4][3][0] = Piece(Orientation.FLAT, Color.BLACK)

    result = v._win_check(board)
    assert (result == outcome)


def test_win_multiple_turns_1():
    outcome = Outcome.WIN_BLACK
    board = np.zeros(shape=(5, 5, 42), dtype=object)

    board[0][2][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][2][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][3][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[2][3][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[3][3][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][1][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[2][1][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[3][1][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[4][1][0] = Piece(Orientation.FLAT, Color.BLACK)

    result = v._win_check(board)
    assert (result == outcome)


def test_win_multiple_turns_2():
    outcome = Outcome.WIN_BLACK
    board = np.zeros(shape=(5, 5, 42), dtype=object)

    board[0][2][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][2][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][3][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[2][3][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[3][3][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[4][3][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[1][1][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[2][1][0] = Piece(Orientation.FLAT, Color.BLACK)
    board[3][1][0] = Piece(Orientation.FLAT, Color.BLACK)

    result = v._win_check(board)
    assert (result == outcome)
