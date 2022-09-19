import numpy as np
from Enums import Orientation, Color

class Position: 
    def __init__(self, x : int, y : int, z : int):
        self.x = x
        self.y = y
        self.z = z

class Piece:
    def __init__(self, position : Position , orientation : Orientation, color : Color):
        self.position = position
        self.orientation = orientation
        self.color = color
    
    def get_position(self):
        return self.position
    
    def get_orientation(self):
        return self.orientation

    def get_color(self):
        return self.color
    
    def __repr__(self):
        return self.color.name

    def __str__(self):
        return self.color.name

    
class GameState:
    def __init__(self, 
                piecesPlayer1 = 21, 
                piecesPlayer2 = 21, 
                board = np.zeros(shape=(5,5,42), dtype=object)):
        self.piecesPlayer1 = piecesPlayer1
        self.piecesPlayer2 = piecesPlayer2
        self.board = board
    
    def print_state(self):
        print(self.board)
    
    def update(self, move):
        src_x = move["src"]["pos_x"]
        src_y = move["src"]["pos_y"]

        des_x = move["des"]["pos_x"]
        des_y = move["des"]["pos_y"]

        color = move["color"]
        ori = move["des"]["orientation"]

        des_z = self.board[des_x][des_y]

        if move["first_turn"]:
            if Color.WHITE.value == color.value: 
                opponent_color = Color.BLACK
            else:
                opponent_color = Color.WHITE

            for i in range(0, des_z.size):
                if des_z[i] == 0:
                    des_z[i] = Piece(Position(des_x, des_y, i), ori, opponent_color)
                    break

        elif move["src"]["pile"]:
            for i in range(0, des_z.size):
                if des_z[i] == 0:
                    des_z[i] = Piece(Position(des_x, des_y, i), ori, color)
                    break
        else:
            ###Add pieces to new destination
            pieces = move["pieces"]

            for i in range(0, des_z.size):
                if des_z[i] == 0:
                    for j in range(0, pieces-1):
                        #All the pieces beneath the one on the top are flat
                        des_z[j+i] = Piece(Position(des_x, des_y, j+i), Orientation.FLAT, color)
                    
                    des_z[j+pieces] = Piece(Position(des_x, des_y, j+i), ori, color)
                    break
            
            ###Remove where the pieces were 
            src_z = self.board[src_x, src_y]

            for i in range(0, src_z.size):
                if src_z[i] == 0:
                    for j in range(0, pieces):
                        src_z[i-j-1] = 0
                    break

move = {
    "src": {
        "pile": True,
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



game = GameState()
game.update(move)
game.update(move)
game.print_state()


move["des"]["pos_x"] = 0
move["des"]["pos_y"] = 0