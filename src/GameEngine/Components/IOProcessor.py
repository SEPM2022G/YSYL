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
        move.isPile = moveJson['src']['pile']
        move.srcPos_x = moveJson['src']['pos_x']
        move.srcPos_y = moveJson['src']['pos_y']
        move.destPos_x = moveJson['des']['pos_x']
        move.destPos_y = moveJson['des']['pos_y']
        move.destOrientation = moveJson['des']['orientation']
        move.pieces = moveJson['pieces']
        move.color = moveJson['color']
        move.first_turn = moveJson['first_turn']
        return move
