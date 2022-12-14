import sys
import getopt
import subprocess
import os
from textual.app import App
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.board.board import Board
from src.info.info import Info
from src.constants import PlayerType, SelectedOption, Notification
from src.GameEngine.Components.IOProcessor import IOProcessor

input_path = os.path.abspath("src/input/in.json")
out_path = os.path.abspath("src/output/out.json")

ui_only = False
argv = sys.argv[1:]
opts, args = getopt.getopt(argv, '', ['ui'])


for opt in opts:
    if opt[0] == '--ui': ui_only = True

class YSYLApp(App):
    io = IOProcessor(input_path, out_path)
    info = Info()
    board = Board(info,io) 

    def set_player_color(self,color):
        self.color = color;
    
    async def on_load(self) -> None:
        """Sent before going in to application mode."""
        # Bind our basic keys
        await self.bind("q", "quit", "Quit")

    async def on_mount(self) -> None:


        await self.view.dock(self.board, edge="left", size=100)
        await self.view.dock(self.info, edge="top")

        self.info.player_widget.next_turn()
        self.info.player_widget.set_n_white_pieces(16)
        self.info.player_widget.set_n_black_pieces(15)

        if color == 'white':
            self.info.player_widget.set_player_color(PlayerType.AI, PlayerType.PLAYER1)
        elif color == 'black':
            self.info.player_widget.set_player_color(PlayerType.PLAYER1, PlayerType.AI)
        self.reset()

    def reset(self):
        self.info.reset()
        self.board.reset()

class Event(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.prev_move_id = ''

    def dispatch(self, event):
        if event.event_type != 'modified' or event.is_directory or (not event.src_path.endswith("out.json")):
            return

        try:
            move = app.io.readOutput()
        except:
            return

        if move['id'] == self.prev_move_id: return

        self.prev_move_id = move['id']
        app.board.perform_ai_move(move)


difficulty = int(input("Enter difficulty (1-3): "))
if difficulty > 3 or difficulty < 1:
    print("invalid difficulty")
    exit();

ai_color = 'black';
color = 'white'

app = YSYLApp()
observer = Observer()
input_event = Event()

observer.schedule(input_event, ".", recursive=True)

observer.start()


if not ui_only:
    ai = subprocess.Popen(['python', '-m', 'src.GameEngine.GameAI', '--color='
                           + ai_color ,'--diff=' + str(difficulty), input_path,
                           out_path], stdout=subprocess.PIPE)

app.set_player_color(color)
app.run(log="textual.log")


observer.stop()
observer.join()

if not ui_only: ai.terminate()
