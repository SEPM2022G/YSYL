# This class represents a 'Move' object that can be passed between components

class Move:
    isPile = None
    srcPos_x = None
    srcPos_y = None
    destPos_x = None
    destPos_y = None
    destOrientation = None
    pieces = None
    color = None
    first_turn = None

    def __init__(self) -> None:
        pass
