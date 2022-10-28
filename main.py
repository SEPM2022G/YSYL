import subprocess
import time
from textual.app import App
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.board.board import Board
from src.info.info import Info
from src.constants import PlayerType, SelectedOption
from src.GameEngine.Components.IOProcessor import IOProcessor

input_path = 'src/input/in.json'
out_path = 'src/output/out.json'

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
            self.info.player_widget.set_player_color(PlayerType.PLAYER1, PlayerType.AI)
        elif color == 'black':
            self.info.player_widget.set_player_color(PlayerType.AI, PlayerType.PLAYER1)
        self.reset()

    def reset(self):
        self.info.reset()
        self.board.reset()

class Event(FileSystemEventHandler):
    prev_move_id = ''
    def dispatch(self, event):
        if event.event_type != 'modified' or event.is_directory:
            return

        move = app.io.readOutput()
        if move['id'] == self.prev_move_id:
            return

        app.board.perform_ai_move(move)


difficulty = int(input("Enter difficulty (1-3): "))
if difficulty > 3 or difficulty < 1:
    print("invalid difficulty")
    exit();

ai_color = 'black';
color = 'white'
# color = input("Enter your color (black/white): ").lower()
# if color == 'white':
#     ai_color = 'black'
# elif color == 'black':
#     ai_color = 'white'
# else:
#     print("invalid color")
#     exit();

app = YSYLApp()
observer = Observer()
input_event = Event()
observer.schedule(input_event, out_path)
observer.start()


# ai = subprocess.Popen(['python', '-m', 'src.GameEngine.GameAI', '--color='
#                        + ai_color ,'--diff=' + str(difficulty), input_path,
#                        out_path], close_fds=True)

app.set_player_color(color)
app.run(log="textual.log")


observer.stop()
observer.join()
# ai.terminate()
