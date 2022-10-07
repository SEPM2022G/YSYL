# This class represents the 'IOProcessor' component in our component diagram

import os
import json


class IOProcessor:
    def __init__(self, read_path, write_path, config_path = '' ) -> None:
        self.write_path = write_path
        self.read_path = read_path
        self.conf_path = config_path

    def loadConfig(self):
        with open(self.conf_path, encoding='utf-8') as conf:
            return json.load(conf)

    def readDifficulty(self, readFromConsole):
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
            conf = self.loadConfig()
            try:
                difficulty = conf['difficulty']
            except:
                print("No difficulty in ", path)

        return difficulty

    def readInput(self):
        with open(self.read_path, encoding='utf-8') as f:
            obj = json.load(f)

        return obj

    def writeOutput(self, data):
        obj = json.dumps(data, indent=4)

        with open(self.write_path, "w") as outfile:
            outfile.write(obj)

        return 1
