# This is the game class that can be used to create a new game. Collection of all components in our component diagram

from cmath import pi
import time
import random
from wsgiref.validate import validator

from GameEngine.Components.Controller import Controller
from GameEngine.Components.IOProcessor import IOProcessor
from GameEngine.Components.Validator import Validator
from GameEngine.Components.StateManager import StateManager
from GameEngine.Components.MoveController import MoveController
from GameEngine.Objects.Enums import Orientation, Color
from GameEngine.Objects.Outcome import Outcome

class GameAI:
    def __init__(self, difficulty) -> None:
        self.difficulty = difficulty
        self.controller = Controller()
        self.ioProcessor = IOProcessor()
        self.validator = Validator()
        self.stateManager = StateManager()
        self.moveController = MoveController()
        self.stopGame = False
        self.fromPile = True
    
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
    
    def _create_move(pile : bool, src_x : int, src_y : int, des_x : int, des_y : int, 
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
    
    def _pieces_of_same_color_in_row(list, top_index, color):
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
    def _create_moves_that_player_can_make(self, color):        
        state = self.stateManager().get_state()
        moves = []

        #All the possible moves when moving a piece or pieces on the board
        #yxi kaksi kolme (It looks nicer this way than encapsulting it in functions in my opinon :))) )
        for src_x in range(0, 5):
            for src_y in range(0, 5):
                    list_z = state["board"][src_x][src_y]
                    if list_z[0] == 0:
                        continue  
                    else:
                        for i in range(0, 42):
                            if list_z[i] == 0:
                                count = self._pieces_of_same_color_in_row(list_z, i, color)
                                for pieces in range(0, count):
                                    for des_x in range(0, 5):
                                        for des_y in range(0, 5):
                                                #Flat
                                                move = self._create_move(False, src_x, src_y, des_x, des_y, Orientation.FLAT, pieces, color, False)
                                                if self._valid_move(move, state):
                                                    moves.append(move)

                                                #Standing
                                                move = self._create_move(False, src_x, src_y, des_x, des_y, Orientation.STANDING, pieces, color, False)
                                                if self._valid_move(move, state):
                                                    moves.append(move)
        
        #All the possible moves when taken from the pile
        for x in range(0, 5):
            for y in range(0, 5):
                if state[f"{color.name.lower()}_pieces_pile"] > 0:
                    #Standing
                    move = self._create_move(True, 0, 0, x, y, Orientation.STANDING, 1, color, False)
                    if self._valid_move(move, state):
                        moves.append(move)

                    #Flat
                    move = self._create_move(True, 0, 0, x, y, Orientation.FLAT, 1, color, False)
                    if self._valid_move(move, state):
                        moves.append(move)

        
        return moves

    def evaluation(self):
        return 42
    
    def minimax(self, depth, maximazing_player):   
        state = self.stateManager.get_state()

        if depth == 0:
            return #evaluation

        valid_moves = self._create_moves_that_player_can_make(Color.WHITE)

        if maximazing_player: 
            maxEval = float('inf')
            for child in valid_moves:
                eval = self.minimax(depth-1, False)
                maxEval = max(maxEval, eval)
        else:
            minEval = float('-inf')
            for child in valid_moves:
                eval = self.minimax(depth-1, False)
                minEval = max(minEval, eval)
