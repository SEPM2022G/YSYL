import subprocess
from textual.app import App
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.board.board import Board
from src.info.info import Info
from src.constants import PlayerType
from src.GameEngine.Components.IOProcessor import IOProcessor

class YSYLApp(App):

    def set_player_color(self,color):
        self.color = color;

    async def on_load(self) -> None:
        """Sent before going in to application mode."""
        # Bind our basic keys
        await self.bind("q", "quit", "Quit")

    async def on_mount(self) -> None:
        self.info = Info()
        self.board = Board(self.info)
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
    def dispatch(self, event):
        if event.event_type != 'modified' or event.is_directory:
            return
        try:
            # Do something here when the ai outputs a move
            move = io.readOutput()
            print(move)
        except Exception as e:
            print(e)
            return


input_path = 'src/input/in.json'
out_path = 'src/output/out.json'
io = IOProcessor(input_path, out_path)

difficulty = int(input("Enter difficulty (1-3): "))
if difficulty > 3 or difficulty < 1:
    print("invalid difficulty")
    exit();

ai_color = '';
color = input("Enter your color (black/white): ").lower()
if color == 'white':
    ai_color = 'black'
elif color == 'black':
    ai_color = 'white'
else:
    print("invalid color")
    exit();

input_event = Event()
observer = Observer()

observer.schedule(input_event, out_path)
observer.start()

ai = subprocess.Popen(['python', '-m', 'src.GameEngine.GameAI', '--color='
                       + ai_color ,'--diff=' + str(difficulty), input_path,
                       out_path], close_fds=True)
app = YSYLApp()
app.set_player_color(color)
app.run(log="textual.log")

observer.stop()
observer.join()
ai.terminate()

