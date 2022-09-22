# This is the game class that can be used to create a new game. Collection of all components in our component diagram

from cmath import pi
import time
import random

from GameEngine.Components.Controller import Controller
from GameEngine.Components.IOProcessor import IOProcessor
from GameEngine.Components.Validator import Validator
from GameEngine.Components.StateManager import StateManager
from GameEngine.Components.MoveController import MoveController
from YSYL.src.GameEngine.Objects.Enums import Orientation


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

        move = self.stateManager.create_move(pile=self.fromPile,des_x=x,des_y=y,orientatiton=orientation, color=0, first_turn=False)

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