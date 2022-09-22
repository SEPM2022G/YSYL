import numpy as np
from src.GameEngine.Components.Validator import Validator
from src.GameEngine.Objects.Piece import Piece
from src.GameEngine.Objects.Outcome import Outcome
from src.GameEngine.Objects.Enums import Orientation, Color
v = Validator()

# Init
def test_init():
    oldstate = { "board": np.zeros(shape=(5,5,42), dtype=object) }
    newstate = { "board": np.zeros(shape=(5,5,42), dtype=object) }
    result = v.check(oldstate, newstate)
    assert(result == Outcome.VALID)

# Tests different win conditions
def win_straight(color, orientation, outcome):
    boards = {}
    for n in range(0,5):
        boards[n] = np.zeros(shape=(5,5,42), dtype=object) 
        for x in range(0,5):
            boards[n][x][n][0] = Piece(orientation, color)
        result = v.win_check(boards[n])
        assert( result == outcome )

def test_win_straight_white_standing():
    win_straight(Color.WHITE, Orientation.STANDING, Outcome.WIN_WHITE)

def test_win_straight_white_flat():
    win_straight(Color.WHITE, Orientation.FLAT, Outcome.WIN_WHITE)

def test_win_straight_black_standing():
    win_straight(Color.BLACK, Orientation.STANDING, Outcome.WIN_BLACK)

def test_win_straight_black_flat():
    win_straight(Color.BLACK, Orientation.FLAT, Outcome.WIN_BLACK)
