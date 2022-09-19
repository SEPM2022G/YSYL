from textual.widget import Widget
from textual.reactive import Reactive
from rich.panel import Panel
from rich.markdown import Markdown
from rich.console import RenderableType
from src.constants import Piece


class Player(Widget):
    # When turn, n_black_pieces, or n_white_pices
    # changes the view will update
    turn: Reactive[RenderableType] = Reactive("")
    n_black_pieces: Reactive[RenderableType] = Reactive("")
    n_white_pieces: Reactive[RenderableType] = Reactive("")

    def __init__(self) -> None:
        super().__init__()
        self.turn = "Black"  # Black is alwase the one who starts
        self.n_black_pieces = 21  # Initaly black has 21 pieces
        self.n_white_pieces = 21  # Initaly white has 21 pieces

    def render(self) -> Panel:
        MARKDOWN = "## Player info\n"
        MARKDOWN += f"It is **{self.turn}'s** turn\n\n"
        MARKDOWN += f"{Piece.BS.value} {self.n_black_pieces} black pieces\n\n"
        MARKDOWN += f"{Piece.WS.value} {self.n_white_pieces} white pieces"
        return Markdown(MARKDOWN)

    def set_turn(self, turn: str) -> None:
        self.turn = turn

    def set_n_black_pieces(self, n_black_pieces: int) -> None:
        self.n_black_pieces = n_black_pieces

    def set_n_white_pieces(self, n_white_pieces: int) -> None:
        self.n_white_pieces = n_white_pieces
