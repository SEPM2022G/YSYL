import numpy as np
from Enums import Orientation, Color

class Piece:
    def __init__(self, direction, color):
        self.direction = direction
        self.color = color
    
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
