#Main program
import sys
import time
import getopt
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from src.GameEngine.Components.IOProcessor import IOProcessor
from src.GameEngine.Components.MoveController import MoveController
from src.GameEngine.Components.StateManager import StateManager
from src.GameEngine.Components.Validator import Validator

#Read inputs
argv = sys.argv[1:]
opts, args = getopt.getopt(argv, 'd:')

if len(args) != 2:
    print('Usage: python -m src.GameEngine.GameAI [OPTION] [INPUT FILE] [OUTPUT FILE]')
    print('Options: ')
    print('     -d : a difficulty level from 1 to 3')
    exit(1)

input_path = args[0]
output_path = args[1]
difficulty = 1

for opt in opts:
    if opt[0] == '-d': 
        difficulty = opt[1]

io = IOProcessor(input_path, output_path)
val = Validator()
sm = StateManager(difficulty)
mc = MoveController()

class Event(FileSystemEventHandler):
    def dispatch(self, event):
        print('changed')

def main():
    ## Watch untill input file is updated
    input_event = Event()
    observer = Observer()

    observer.schedule(input_event, input_path)
    observer.start()

    try:
        while True: 
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()




if __name__ == "__main__":
    main()
