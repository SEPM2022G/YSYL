# This class represents the 'IOProcessor' component in our component diagram

import json

class IOProcessor:
    def __init__(self) -> None:
        pass

    def loadConfig(self, path="conf.json"):
        with open("config.json", encoding = 'utf-8') as conf:
            return json.load(conf)

    def readDifficulty(self, readFromConsole):
        difficulty = -1
        # it is configurable to read difficulty from a file or read from console
        if ( readFromConsole ) :
            print("1 -> Easy")
            print("2 -> Medium")
            print("3 -> Hard")
            validInput = False
            while (not validInput):
                try:
                    difficulty = int(input("Enter valid difficulty: "))
                    if (difficulty > 0 and difficulty < 4):
                        validInput = True
                except:
                    print("Invalid input for difficulty")
        else:
            with open("input/init.json", encoding = 'utf-8') as init:
                initialize = json.load(init)
                difficulty = initialize['difficulty']
        
        return difficulty

    def readInput(self, path="input/in.json") -> any:
        with open(path, encoding = 'utf-8') as f:
            fileData = json.load(f)

        return fileData

    def writeOutput(self, path="output/out.json"):
        print("write to file")

    #def inputToMove(self) -> Move:
    #    print("convert file data to Move object")
    #    return Move()

