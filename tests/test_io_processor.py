import os
from src.GameEngine.Components.IOProcessor import IOProcessor


IOP = IOProcessor()

# Init
def test_init():
    pass

def test_write_win_to_file():
    win = {
            "winner": 0
        }
    result = IOP.writeWin(win, os.path.join(os.path.dirname(os.path.abspath(".gitignore")), "src", "output", "win.json"))
    assert (result == 1)

def test_read_diff_from_file():
    result = IOP.readDifficulty(False, os.path.join(os.path.dirname(os.path.abspath(".gitignore")), "src", "input", "init.json"))
    assert (result == 1)