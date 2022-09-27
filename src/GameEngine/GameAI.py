# This is the game class that can be used to create a new game. Collection of all components in our component diagram

from cmath import pi
import time
import random
from copy import deepcopy

from src.GameEngine.Components.Controller import Controller
from src.GameEngine.Components.IOProcessor import IOProcessor
from src.GameEngine.Components.Validator import Validator
from src.GameEngine.Components.StateManager import StateManager
from src.GameEngine.Components.MoveController import MoveController
from src.GameEngine.Objects.Enums import Orientation, Color
from src.GameEngine.Objects.Outcome import Outcome

class GameAI:
    def __init__(self, difficulty) -> None:
        self.difficulty = difficulty
        self.validator = Validator()
        self.stopGame = False
        self.fromPile = True
        self.best_move = None
    
# OBS HÅRDKODAD FÖR VIT GLÖM EJ

    #Find plave for piece
    def randMoveEasy(self):
        piece = self.piece
        state = self.stateManager.get_state()
        board = self.stateManager.board
        #hitta possble places to put piece
        
        x = random.randint(0,4)
        y = random.randint(0,4)
        orientation = random.randint(0,1)

        move = self.create_move(pile=self.fromPile,des_x=x,des_y=y,orientatiton=orientation, color=0, first_turn=False)

        if self.validator.validMove(move):
            self.stateManager.update_state(self, move)

    #Only used on level easy since it will not be random on other levels.
    def randPieceEasy(self):
        if self.difficulty != "easy":
            pass

        pile = self.StateManager.getWhitePiles

        if pile > 0:
            self.fromPile = True #med vit från sidan
        
        else:
            self.fromPile = False

        self.randMoveEasy()
    

    def start(self):
        print(f"{self.difficulty} Game Started")

        while (not self.stopGame):
            print(self.ioProcessor.readInput())
            print("this is printing from GameAI.py -> start() function")
            time.sleep(2)
    
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
        for src_x in range(0, state["board"].shape[1]):
            for src_y in range(0, state["board"].shape[0]):
                    list_z = state["board"][src_x][src_y]
                    if list_z[0] == 0:
                        continue  
                    else:
                        for i in range(0, state["board"].shape[2]):
                            if list_z[i] == 0:
                                count = self._pieces_of_same_color_in_row(list_z, i, color)
                                for pieces in range(0, count):
                                    for des_x in range(0, state["board"].shape[1]):
                                        for des_y in range(0, state["board"].shape[0]):
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
        for des_x in range(0, state["board"].shape[1]):
            for des_y in range(0, state["board"].shape[0]):
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
    
    def minimax(self, depth, color, state_manager):   
        state = state_manager.get_state()

        if depth == 0 or self._game_over(state["board"]):
            return state_manager.board_evaluation()
        
        if color.value == Color.WHITE.value: 
            valid_moves = self._create_moves_that_player_can_make(state, Color.WHITE)
            maxEval = float('-inf')
            for move in valid_moves:
                state_manager_copy = deepcopy(state_manager)
                state_manager_copy.update_state(move)
                eval = self.minimax(depth-1, Color.BLACK, state_manager_copy)
                maxEval = max(maxEval, eval)

                if eval >= maxEval:
                    self.best_move = move

            return maxEval
        else:
            valid_moves = self._create_moves_that_player_can_make(state, Color.BLACK)
            minEval = float('inf')
            for move in valid_moves:
                state_manager_copy = deepcopy(state_manager)
                state_manager_copy.update_state(move)
                eval = self.minimax(depth-1, Color.WHITE, state_manager_copy)
                minEval = min(minEval, eval)

                if eval <= minEval:
                    self.best_move = move

            return minEval


