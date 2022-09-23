from src.GameEngine.Objects.Enums import Orientation, Color

class Piece:
    def __init__(self, orientation : Orientation, color : Color):
        self.orientation = orientation
        self.color = color
   
    def get_orientation(self):
        return self.orientation

    def get_color(self):
        return self.color
    
    def __repr__(self):
        return f"({self.color.name}, {self.orientation.name})"

    def __str__(self):
        return f"({self.color.name}, {self.orientation.name})"

    def __eq__(self, other):
        if type(self) != type(other): return False
        return self.color == other.color and self.orientation == other.orientation

    def __neq__(self, other):
        if type(self) != type(other): return True
        return self.color != other.color or self.orientation != other.orientation

