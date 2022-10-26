import subprocess
from textual.app import App
from src.board.board import Board
from src.info.info import Info
from src.constants import PlayerType

class PrettyGameApp(App):
    async def on_load(self) -> None:
        """Sent before going in to application mode."""
        # Bind our basic keys
        await self.bind("q", "quit", "Quit")

    async def on_mount(self) -> None:
        self.info = Info()
        self.board = Board(self.info.player_widget.next_turn,
                           self.info.get_option,
                           self.info.player_widget.get_turn,
                           self.info.picked_up_stack_widget.set_pieces,
                           self.info.picked_up_stack_widget.remove)
        await self.view.dock(self.board, edge="left", size=100)
        await self.view.dock(self.info, edge="top")

        self.info.tournament_widget.set_score((1, 1))
        self.info.tournament_widget.set_n_games(1)
        self.info.player_widget.next_turn()
        self.info.player_widget.set_n_white_pieces(16)
        self.info.player_widget.set_n_black_pieces(15)
        self.info.player_widget.set_player_color(PlayerType.PLAYER1, PlayerType.AI)
        self.reset()

    def reset(self):
        self.info.reset()
        self.board.reset()

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


ai = subprocess.Popen(['python', '-m', 'src.GameEngine.GameAI', '--color=' + ai_color
                ,'--diff=' + str(difficulty), 'src/input/in.json',
                'src/output/out.json'], close_fds=True)

PrettyGameApp.run(log="textual.log")
ai.terminate()
