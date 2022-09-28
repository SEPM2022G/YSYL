# This is the game class that can be used to create a new game. Collection of all components in our component diagram

import time

from GameEngine.Components.Controller import Controller


class GameAI:
    def __init__(self) -> None:
        self.controller = Controller()
        self.stopGame = False
    

    def start(self):
        print("Game Started")