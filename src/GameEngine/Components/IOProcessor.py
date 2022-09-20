# This class represents the 'IOProcessor' component in our component diagram

import json

class IOProcessor:
    def __init__(self) -> None:
        pass

    def readInput(self, path="input/in.json") -> any:
        with open(path, encoding = 'utf-8') as f:
            fileData = json.load(f)

        return fileData

    def writeOutput(self, path="output/out.json"):
        print("write to file")

    #def inputToMove(self) -> Move:
    #    print("convert file data to Move object")
    #    return Move()