# This class represents the 'IOProcessor' component in our component diagram

import json


class IOProcessor:
    def __init__(self) -> None:
        pass

    def loadConfig(self, path="config.json"):
        with open(path, encoding='utf-8') as conf:
            return json.load(conf)

    def readDifficulty(self, readFromConsole, path="config.json"):
        difficulty = -1
        # it is configurable to read difficulty from a file or read from console
        if (readFromConsole):
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
            conf = self.loadConfig(path)
            try:
                difficulty = conf['difficulty']
            except:
                print("No difficulty in ", path)

        return difficulty

    def readInput(self, path="input/in.json"):
        with open(path, encoding='utf-8') as f:
            obj = json.load(f)

        return obj

    def writeOutput(self, data, path="output/out.json"):
        obj = json.dumps(data, indent=4)

        with open(path, "w") as outfile:
            outfile.write(obj)

        return 1
