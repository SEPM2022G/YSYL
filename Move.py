from Enums import Orientation, Color

class Position: 
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y

class Source:
    def __init__(self, position : Position, stackAmount = 1):
        self.position = position
        self.stackAmount = stackAmount

class Destination:
    def __init__(self, position : Position, orientation: Orientation):
        self.position = position
        self.orientation = orientation 

class Move:
    def __init__(self, 
                source : Source, 
                destination : Destination, 
                color : Color, 
                isFirstMove = False):
        self.source = source 
        self.destination = destination 
        # This is determined in the input/output component
        # depending on which player has made the move
        self.color = color
        # Boolean if the move is the first turn
        self.isFirstMove = isFirstMove


Move(Source(Position(1,2), 1), Destination(Position(1,2), Orientation.FLAT), Color.WHITE, False)