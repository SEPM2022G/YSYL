# This is the game class that can be used to create a new game. Collection of all components in our component diagram

import time

from GameEngine.Components.Controller import Controller
from GameEngine.Components.IOProcessor import IOProcessor
from GameEngine.Components.Validator import Validator
from GameEngine.Components.StateManager import StateManager
from GameEngine.Components.MoveController import MoveController


class GameAI:
    def __init__(self, difficulty) -> None:
        self.difficulty = difficulty
        self.controller = Controller()
        self.ioProcessor = IOProcessor()
        self.validator = Validator()
        self.stateManager = StateManager()
        self.moveController = MoveController()
        self.stopGame = False
    

    def start(self):
        print(f"{self.difficulty} Game Started")

        while (not self.stopGame):
            print(self.ioProcessor.readInput())
            print("this is printing from GameAI.py -> start() function")
            time.sleep(2)