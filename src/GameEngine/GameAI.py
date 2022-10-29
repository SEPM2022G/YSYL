# Main program
import sys
import time
import getopt
import uuid
import copy
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from src.GameEngine.Components.IOProcessor import IOProcessor
from src.GameEngine.Components.MoveController import MoveController
from src.GameEngine.Components.StateManager import StateManager
from src.GameEngine.Components.Validator import Validator
from src.GameEngine.Objects.Outcome import Outcome
from src.GameEngine.Objects.Enums import Color, Difficulty

# Read inputs
argv = sys.argv[1:]
opts, args = getopt.getopt(argv, '', ['diff=', 'color=', 'config='])

if len(args) != 2:
    print(
        'Usage: python -m src.GameEngine.GameAI [OPTION] [INPUT FILE] [OUTPUT FILE]')
    print('Options: ')
    print('     --diff : a difficulty level from 1 to 3')
    print('     --color : the color for the AI (black or white)')
    print('     --config : the file path to a config')
    exit(1)

input_path = args[0]
output_path = args[1]
difficulty = Difficulty.MEDIUM
ai_color = Color.BLACK
config_path = ''

for opt in opts:
    if opt[0] == '--diff' and int(opt[1]) < 4 and int(opt[1]) > 0:
        difficulty = Difficulty(int(opt[1]) - 1)
    if opt[0] == '--color':
        if opt[1] == 'black':
            ai_color = Color.BLACK
        elif opt[1] == 'white':
            ai_color = Color.WHITE
        else:
            print('invalid color')
            exit(1)
    if opt[0] == '--config':
        config_path = opt[1]


io = IOProcessor(input_path, output_path, config_path)
val = Validator()
sm = StateManager()
mc = MoveController(sm, difficulty, ai_color)

class Event(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.prev_move_id = ''

    def dispatch(self, event):
        if event.event_type != 'modified' or event.is_directory:
            return

        move = io.readInput()
        if move['id'] == self.prev_move_id: return
        else: self.prev_move_id = move['id']

        move_id = uuid.uuid4()

        if len(config_path) > 0:
            print('Reading diff from config')
            mc.set_difficulty(Difficulty(io.readDifficulty(False)))

        old_state = copy.deepcopy(sm.get_state())
        new_state = sm.update_state(move)

        outcome = val.check(move, old_state, new_state)
        output = { 'outcome': outcome.value , 'id': str(move_id) }

        print('---------------INPUT MOVE-------------------')
        print('Player move:', move)
        print('Outcome: ', outcome)
        sm.print_state()

        if outcome == Outcome.INVALID:
            sm.set_state(old_state)

        elif outcome == Outcome.VALID:
            new_move = mc.move()

            sm.update_state(new_move)
            output['move'] = new_move

            ai_outcome = val._win_check(sm.get_state()['board'])
            if ai_outcome != Outcome.CONT: output['outcome'] = ai_outcome.value

        else: 
            sm.__init__()

        print('\n---------------OUTPUT MOVE-------------------\n')
        sm.print_state()
        print(output)
        print('\n##########################################\n')

        io.writeOutput(output)
        return


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
