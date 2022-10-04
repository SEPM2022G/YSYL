# Main program
import sys
import time
import getopt
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from src.GameEngine.Components.IOProcessor import IOProcessor
from src.GameEngine.Components.MoveController import MoveController
from src.GameEngine.Components.StateManager import StateManager
from src.GameEngine.Components.Validator import Validator
from src.GameEngine.Objects.Outcome import Outcome
from src.GameEngine.Objects.Enums import Color

# Read inputs
argv = sys.argv[1:]
opts, args = getopt.getopt(argv, 'd:')

if len(args) != 2:
    print(
        'Usage: python -m src.GameEngine.GameAI [OPTION] [INPUT FILE] [OUTPUT FILE]')
    print('Options: ')
    print('     -d : a difficulty level from 1 to 3')
    print('     -c : the color for the AI (black or white)')
    exit(1)

input_path = args[0]
output_path = args[1]
difficulty = 1
ai_color = Color.BLACK

for opt in opts:
    if opt[0] == '-d':
        difficulty = opt[1]
    if opt[0] == '-c':
        if opt[1] == 'black':
            ai_color = Color.BLACK
        elif opt[1] == 'white':
            ai_color = Color.WHITE
        else:
            print('invalid color')
            exit(1)


io = IOProcessor(input_path, output_path)
val = Validator()
sm = StateManager(difficulty)
mc = MoveController()


class Event(FileSystemEventHandler):
    def dispatch(self, event):
        if event.event_type != 'modified' or event.is_directory:
            return
        try:
            move = io.readInput()
        except:
            print("Invalid Json in ", input_path)
            return

        old_state = sm.get_state()
        new_state = sm.update_state(move)

        outcome = val.check(move, old_state, new_state)
        new_move = {'outcome': outcome}
        # revert state
        if outcome == Outcome.INVALID:
            sm.set_state(old_state)
        # Reset the Game
        elif outcome != Outcome.CONT:
            sm.__init__()
        # Play a move
        else:
            new_move = mc.MoveController(sm, difficulty, ai_color)
            sm.update_state(new_move)
            new_move['outcome'] = outcome

        io.writeOutput(new_move)


def main():
    # Watch untill input file is updated

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
