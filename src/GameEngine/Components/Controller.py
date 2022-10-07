# This class represents the 'Controller' component in our component diagram

from src.GameEngine.Components.IOProcessor import IOProcessor


class Controller:
    def __init__(self) -> None:
        self.ioProcessor = IOProcessor()
        self.config = self.ioProcessor.loadConfig()
        self.difficulty = self.ioProcessor.readDifficulty(self.config['readFromConsole'])
        print(self.difficulty)