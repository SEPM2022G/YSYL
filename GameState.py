import numpy as np
from Enums import Orientation, Color

class Position: 
    def __init__(self, x : int, y : int, z : int):
        self.x = x
        self.y = y
        self.z = z

class Piece:
    def __init__(self, position : Position , direction, color):
        self.position = position
        self.direction = direction
        self.color = color
    
    def get_position(self):
        return self.position
    
    def set_position(self,x,y,z):
        self.position.x = x
        self.position.y = y
        self.position.z = z
    
    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction
    
    def get_color(self):
        return self.color

    
class GameState:
    def __init__(self, 
                piecesPlayer1 = 21, 
                piecesPlayer2 = 21, 
                board = np.zeros(shape=(5,5,42))):
        self.piecesPlayer1 = piecesPlayer1
        self.piecesPlayer2 = piecesPlayer2
        self.board = board
    
    def printState(self):
        print(self.board)
    


GameState().printState()
