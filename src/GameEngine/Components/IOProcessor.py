# This class represents the 'IOProcessor' component in our component diagram

import json

from GameEngine.Objects.Move import Move

class IOProcessor:
    def __init__(self) -> None:
        pass

    def readInput(self, path="input/in.json") -> any:
        with open(path, encoding = 'utf-8') as f:
            fileData = json.load(f)

        return fileData

    def writeOutput(self, path="output/out.json"):
        print("write to file")

    def inputToMove(self) -> Move:
        moveJson = self.readInput()
        move = Move()
        move.moveNumber = moveJson['moveNo']
        move.player = moveJson['player']
        move.colour = moveJson['colour']
        move.board = moveJson['board']
        return move
