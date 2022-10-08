import numpy as np
from src.GameEngine.Objects.Enums import Orientation, Color
from src.GameEngine.Objects.Piece import Piece

# This class represents the 'StateManager' component in our component diagram

class StateManager:
    def __init__(self, 
                white_pieces_pile = 21, 
                black_pieces_pile = 21, 
                board_x = 5,
                board_y = 5):

        self.white_pieces_pile = white_pieces_pile
        self.black_pieces_pile = black_pieces_pile
        self.board = np.zeros(shape=(board_x, board_y, white_pieces_pile+black_pieces_pile),  dtype=object)
    
    def print_state(self):
        print()
        print("White pieces in pile: ", self.white_pieces_pile)
        print("Black pieces in pile: ", self.black_pieces_pile)

        print("------------------------------------------------------------------------------")

        for y in range(self.board.shape[1]):
            print("|",end="")
            for x in range(self.board.shape[0]):
                piece = self._find_top_piece(self.board[x][y])
                if piece == 0:
                    print(" 0 ",end="")
                else: 
                    print(piece,end="")
                
            print("|")

        print("------------------------------------------------------------------------------")
        print()

    def get_state(self):
        state = {
            "white_pieces_pile":self.white_pieces_pile,
            "black_pieces_pile":self.black_pieces_pile,
            "board": self.board
        }

        return state

    def set_state(self, state):
        self.white_pieces_pile = state['white_pieces_pile']
        self.black_pieces_pile = state['black_pieces_pile']
        self.board = state['board']


    def getWhitePiles(self):
        return self.white_pieces_pile
    
    def getBlackPiles(self):
        return self.black_pieces_pile
    
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
                self.black_pieces_pile -= 1 
            else:
                opponent_color = Color.WHITE
                self.white_pieces_pile -= 1

            for i in range(0, des_z.size):
                if des_z[i] == 0:
                    des_z[i] = Piece(ori, opponent_color)
                    break

        elif move["src"]["pile"]:
            for i in range(0, des_z.size):
                if des_z[i] == 0:
                    des_z[i] = Piece(ori, color)
                    if Color.WHITE.value == color.value:
                        self.white_pieces_pile -= 1
                    else:
                        self.black_pieces_pile -= 1

                    break
        else:
            ###Add pieces to new destination
            pieces = move["pieces"]

            for i in range(0, des_z.size):
                if des_z[i] == 0:
                    for j in range(0, pieces-1):
                        #All the pieces beneath the one on the top are flat
                        des_z[i+j] = Piece(Orientation.FLAT, color)
                    
                    des_z[i+pieces-1] = Piece(ori, color)
                    break
            
            ###Remove where the pieces were 
            src_z = self.board[src_x, src_y]

            for i in range(0, src_z.size):
                if src_z[i] == 0:
                    for j in range(0, pieces):
                        src_z[i-j-1] = 0
                    break

        return self.get_state()
    
    def board_evaluation(self, color, depth):
        standing_color = 0
        standing_opposite = 0

        row_color = 0
        row_opposite = 0

        around_color = 0
        around_opposite = 0

        for y in range(0, self.board.shape[1]):
            count_row_color = 0
            count_row_opposite = 0
            for x in range(0, self.board.shape[0]):
                piece = self._find_top_piece(self.board[x][y])
                if piece != 0:
                    isColor = piece.get_color().value == color.value

                    #Standing
                    if isColor and piece.get_orientation().value == Orientation.STANDING.value:
                        standing_color += 1
                    else: 
                        standing_opposite += 1
                    
                    #Longest row
                    if isColor:
                        count_row_color += 1
                    else:
                        count_row_opposite += 1

                    #Around color
                    if (y-1) > 0:
                        piece = self._find_top_piece(self.board[x][y-1])
                        if piece != 0:
                            if piece.get_color().value == color.value:
                                around_color += 1
                            else:
                                around_opposite += 1
                        
                    #Around color
                    if (y+1) < self.board.shape[1]:
                        piece = self._find_top_piece(self.board[x][y+1])
                        if piece != 0:
                            if piece.get_color().value == color.value:
                                around_color += 1
                            else:
                                around_opposite += 1
         

            #Longest row
            if count_row_color > row_color:
                row_color = count_row_color
            
            if count_row_opposite > row_opposite:
                row_opposite = count_row_opposite
    
        return (standing_opposite-standing_color)*4 + (row_opposite-row_color)*10 + (around_opposite-around_color)*2 + (depth*15) 

    def _find_top_piece(self, arr):
        '''
        Helper function for getting the top piece in a stack
        '''
        if arr[0] == 0:
            return 0
    
        for i, elem in enumerate(arr):

            if elem == 0:
                return arr[i-1]
        
        return arr[arr.shape[0]-1]

