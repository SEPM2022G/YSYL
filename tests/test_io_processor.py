from src.GameEngine.Components.IOProcessor import IOProcessor


IOP = IOProcessor()

# Init
def test_init():
    pass

def test_read_diff_from_file():
    result = IOP.readDifficulty(False)
    assert (result == 1)