# This is the game class that can be used to create a new game. Collection of all components in our component diagram
import random
from copy import deepcopy

from src.GameEngine.Components.Controller import Controller
from src.GameEngine.Components.IOProcessor import IOProcessor
from src.GameEngine.Components.Validator import Validator
from src.GameEngine.Components.StateManager import StateManager
from src.GameEngine.Components.MoveController import MoveController
from src.GameEngine.Objects.Enums import Orientation, Color, Difficulty
from src.GameEngine.Objects.Outcome import Outcome

#Magic
class GameAI:
    def __init__(self, state_manager : StateManager, difficulty : Difficulty, ai_color : Color) -> None:
        self.validator = Validator()
        self.state_manager = state_manager
        self.difficulty = difficulty
        self.color = ai_color
        self.best_move = None
        self.init_depth = 0
    
    def _easy_move(self, state_manager):
        moves = self._create_moves_that_player_can_make(state_manager.get_state(), self.color)
        self.best_move = moves[random.randint(0, len(moves)-1)]

    def move(self):
        print(f"AI {self.difficulty}")

        if self.difficulty.value == Difficulty.EASY.value:
            self._easy_move(self.state_manager)
        elif self.difficulty.value == Difficulty.MEDIUM.value:
            self.init_depth = 1
            self._minimax(self.init_depth, self.color, self.state_manager)
        else:
            self.init_depth = 2
            self._minimax(self.init_depth, self.color, self.state_manager)

        return self.best_move

    
    def _create_move(self, pile : bool, src_x : int, src_y : int, des_x : int, des_y : int, 
                orientatiton : Orientation, pieces : int, color : Color, first_turn : bool):
        move = {
            "src": {
                "pile": pile,
                "pos_x": src_x,
                "pos_y": src_y,
            },
            "des": {
                "pos_x": des_x,
                "pos_y": des_y,
                "orientation": orientatiton
            },
            "pieces": pieces,
            "color": color,
            "first_turn": first_turn
        }
        return move
    
    def _pieces_of_same_color_in_row(self, list, top_index, color):
        count = 0
        for i in reversed(range(0, top_index)):
            if list[i].get_color().value == color.value:
                count += 1
            else:
                break

        return count

    def _valid_move(self, move, state):
        result = self.validator.check(move, state, state)

        if result == Outcome.VALID:
            return True
        else:
            return False
    
    #TODO must handle the first turn so the AI makes the best move
    def _create_moves_that_player_can_make(self, state, color):        
        valid_moves = []

        #All the possible moves when moving a piece or pieces on the board
        #yxi kaksi kolme (It looks nicer this way than encapsulting it in functions in my opinon :))) )
        for src_x in range(0, state["board"].shape[0]):
            for src_y in range(0, state["board"].shape[1]):
                    list_z = state["board"][src_x][src_y]
                    if list_z[0] == 0:
                        continue  
                    else:
                        for i in range(1, state["board"].shape[2]):
                            if list_z[i] == 0:
                                count = self._pieces_of_same_color_in_row(list_z, i, color)
                                for pieces in range(0, count):
                                    for des_x in range(0, state["board"].shape[0]):
                                        for des_y in range(0, state["board"].shape[1]):
                                                #Flat
                                                move = self._create_move(False, src_x, src_y, des_x, des_y, Orientation.FLAT, pieces, color, False)
                                                if self._valid_move(move, state):
                                                    valid_moves.append(move)

                                                #Standing
                                                move = self._create_move(False, src_x, src_y, des_x, des_y, Orientation.STANDING, pieces, color, False)
                                                if self._valid_move(move, state):
                                                    valid_moves.append(move)
                                break
        
        #All the possible moves when taken from the pile
        for des_x in range(0, state["board"].shape[0]):
            for des_y in range(0, state["board"].shape[1]):
                if state[f"{color.name.lower()}_pieces_pile"] > 0:
                    #Standing
                    move = self._create_move(True, 0, 0, des_x, des_y, Orientation.STANDING, 1, color, False)
                    if self._valid_move(move, state):
                        valid_moves.append(move)

                    #Flat
                    move = self._create_move(True, 0, 0, des_x, des_y, Orientation.FLAT, 1, color, False)
                    if self._valid_move(move, state):
                        valid_moves.append(move)

        
        return valid_moves

    def _game_over(self, board):
        o = self.validator._win_check(board)
        if o == Outcome.WIN_BLACK or o == Outcome.WIN_WHITE:
            return True

        return False
    
    def _minimax(self, depth, color, state_manager, alpha=float("-inf"), beta=float("inf")):   
        
        state = state_manager.get_state()

        if depth == 0 or self._game_over(state["board"]):
            return state_manager.board_evaluation(color)
        
        if color.value == Color.WHITE.value: 
            valid_moves = self._create_moves_that_player_can_make(state, Color.WHITE)
            maxEval = float('-inf')
            for move in valid_moves:
                state_manager_copy = deepcopy(state_manager)
                state_manager_copy.update_state(move)
                eval = self._minimax(depth-1, Color.BLACK, state_manager_copy, alpha, beta)
                maxEval = max(maxEval, eval)

                if eval >= maxEval:
                    if depth == self.init_depth:
                        self.best_move = move
                        print("####MAX#####")
                        print(move)
                        print(eval)

                alpha = max(alpha, eval)
                if beta <= alpha:
                    break

            return maxEval
        else:
            valid_moves = self._create_moves_that_player_can_make(state, Color.BLACK)
            minEval = float('inf')
            for move in valid_moves:
                state_manager_copy = deepcopy(state_manager)
                state_manager_copy.update_state(move)
                eval = self._minimax(depth-1, Color.WHITE, state_manager_copy, alpha, beta)
                minEval = min(minEval, eval)

                if eval <= minEval:
                    if depth == self.init_depth:
                        print("####MIN#####")
                        print(move)
                        print(eval)
                        self.best_move = move
                
                beta = min(beta, eval)
                if beta <= alpha:
                    break

            return minEval
    


