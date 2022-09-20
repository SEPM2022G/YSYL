from textual.app import App
from src.board.board import Board
from src.info.info import Info


class PrettyGameApp(App):
    async def on_load(self) -> None:
        """Sent before going in to application mode."""

        # Bind our basic keys
        await self.bind("q", "quit", "Quit")

    async def on_mount(self) -> None:
        self.board = Board()
        self.info = Info()
        await self.view.dock(self.board, edge="left", size=100)
        await self.view.dock(self.info, edge="top")

        self.info.tournament_widget.set_score((1, 1))
        self.info.tournament_widget.set_n_games(1)
        self.info.player_widget.next_turn()
        self.info.player_widget.set_n_white_pieces(16)
        self.info.player_widget.set_n_black_pieces(15)


PrettyGameApp.run(log="textual.log")
