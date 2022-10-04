import os
from src.GameEngine.Objects.Enums import Color, Orientation
from src.GameEngine.Components.IOProcessor import IOProcessor


IOP = IOProcessor()

# Init
def test_init():
    pass

def test_read_diff_from_file():
    result = IOP.readDifficulty(False)
    assert (result == 1)

def test_write_to_file():
    move = {
            "src": {
                "pile": True,
                "pos_x": 5,
                "pos_y": 4,
            },
            "des": {
                "pos_x": 2,
                "pos_y": 3,
                "orientation": Orientation.FLAT
            },
            "pieces": 1,
            "color": Color.WHITE,
            "first_turn": False
            }
    
    result = IOP.writeOutput(move)
    assert (result == 1)

def test_read_from_file():
    result = IOP.readInput()
    assert (type(result) is dict)
