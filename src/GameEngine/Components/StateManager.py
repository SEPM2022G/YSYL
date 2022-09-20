import numpy as np
from ..Enums import Orientation, Color
from ..Objects.Piece import Piece

# This class represents the 'StateManager' component in our component diagram

class StateManager:
    def __init__(self, 
                white_pieces = 21, 
                black_pieces = 21, 
                board = np.zeros(shape=(5,5,42), dtype=object)):
        self.white_pieces = white_pieces
        self.black_pieces = black_pieces
        self.board = board
    
    def print_state(self):
        print("White pieces: ", self.white_pieces)
        print("Black pieces: ", self.black_pieces)
        print(self.board)
    
    def get_state(self):
        state = {
            "white_pieces":self.white_pieces,
            "black_pieces":self.black_pieces,
            "board": self.board
        }

        return state

    def update_state(self, move):
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
                self.black_pieces -= 1 
            else:
                opponent_color = Color.WHITE
                self.white_pieces -= 1

            for i in range(0, des_z.size):
                if des_z[i] == 0:
                    des_z[i] = Piece(ori, opponent_color)
                    break

        elif move["src"]["pile"]:
            for i in range(0, des_z.size):
                if des_z[i] == 0:
                    des_z[i] = Piece(ori, color)
                    if Color.WHITE.value == color.value:
                        self.white_pieces -= 1
                    else:
                        self.black_pieces -= 1

                    break
        else:
            ###Add pieces to new destination
            pieces = move["pieces"]

            for i in range(0, des_z.size):
                if des_z[i] == 0:
                    for j in range(0, pieces-1):
                        #All the pieces beneath the one on the top are flat
                        des_z[i+j] = Piece(Orientation.FLAT, color)
                    
                    des_z[i+pieces] = Piece(ori, color)
                    break
            
            ###Remove where the pieces were 
            src_z = self.board[src_x, src_y]

            for i in range(0, src_z.size):
                if src_z[i] == 0:
                    for j in range(0, pieces):
                        src_z[i-j-1] = 0
                    break

        return self.get_state()


