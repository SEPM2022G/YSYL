# This is the game class that can be used to create a new game. Collection of all components in our component diagram
import random
from copy import deepcopy

from src.GameEngine.Components.Validator import Validator
from src.GameEngine.Components.StateManager import StateManager
from src.GameEngine.Objects.Enums import Orientation, Color, Difficulty
from src.GameEngine.Objects.Outcome import Outcome

#Magic
class MoveController:
    def __init__(self, state_manager : StateManager, difficulty : Difficulty, ai_color : Color) -> None:
        self.validator = Validator()
        self.state_manager = state_manager
        self.difficulty = difficulty
        self.color = ai_color
        self.best_moves = []
        self.init_depth = 0
        self.medium_hard_move = False

    def set_difficulty(difficulty : Difficulty):
        self.difficulty = difficulty
    
    def _easy_move(self, state_manager):
        moves = self._create_moves_that_player_can_make(state_manager.get_state(), self.color)
        self.best_moves.append((moves[random.randint(0, len(moves)-1)], 0))

    def move(self):
        print(f"AI {self.difficulty}")

        if self.difficulty.value == Difficulty.EASY.value:
            self._easy_move(self.state_manager)
        elif self.difficulty.value == Difficulty.MEDIUM.value:
            self.init_depth = 4
            if self.medium_hard_move:
                self._minimax(self.init_depth, self.color, self.state_manager)
                self.medium_hard_move = False 
            else:
                self._easy_move(self.state_manager)
                self.medium_hard_move = True
        else:
            self.init_depth = 4
            self._minimax(self.init_depth, self.color, self.state_manager)

        best_move = self.best_moves[random.randint(0, len(self.best_moves))-1][0]
        #remove the best moves from previous turn
        self.best_moves = []

        return best_move

    
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
                "orientation": orientatiton.value
            },
            "pieces": pieces,
            "color": color.value,
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
        if o == Outcome.WIN_BLACK:
            return True, -1
        elif o == Outcome.WIN_WHITE:
            return True, 1 

        return False, 0
    
    def _minimax(self, depth, color, state_manager, alpha=float("-inf"), beta=float("inf")):   
        
        state = state_manager.get_state()

        game_over, who_won = self._game_over(state["board"])

        if depth == 0 or game_over:
            return state_manager.board_evaluation(color, who_won*depth)
        
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
                        #best_moves has always the same eval score inside it
                        if self.best_moves:
                            if eval > self.best_moves[0][1]: 
                                self.best_moves = []

                        self.best_moves.append((move, eval))
                        #print("####MAX#####")
                        #print(self.best_moves)

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
                        if self.best_moves:
                            if eval > self.best_moves[0][1]: 
                                self.best_moves = []

                        self.best_moves.append((move, eval))
                        #print("####MIN#####")
                        #print(self.best_moves)
                
                beta = min(beta, eval)
                if beta <= alpha:
                    break

            return minEval
    
