from textual.widget import Widget
from textual.reactive import Reactive
from rich.panel import Panel
from rich.markdown import Markdown
from rich.console import RenderableType
from src.constants import Piece, Turn


class Player(Widget):
    # When turn, n_black_pieces, or n_white_pices
    # changes the view will update
    turn: Reactive[RenderableType] = Reactive(Turn.BLACK)
    n_black_pieces: Reactive[RenderableType] = Reactive("")
    n_white_pieces: Reactive[RenderableType] = Reactive("")

    def __init__(self) -> None:
        super().__init__()
        self.turn = Turn.BLACK  # Black is alwase the one who starts
        self.n_black_pieces = 21  # Initaly black has 21 pieces
        self.n_white_pieces = 21  # Initaly white has 21 pieces

    def render(self) -> Panel:
        MARKDOWN = "## Player info\n"
        MARKDOWN += f"It is **{self.turn.value}'s** turn\n\n"
        MARKDOWN += f"{Piece.BS.value} {self.n_black_pieces} black pieces\n\n"
        MARKDOWN += f"{Piece.WS.value} {self.n_white_pieces} white pieces"
        return Markdown(MARKDOWN)

    def set_turn(self, turn: Turn) -> None:
        self.turn = turn

    def turn_black(self) -> None:
        self.set_turn(Turn.BLACK)

    def turn_white(self) -> None:
        self.set_turn(Turn.WHITE)

    def set_n_black_pieces(self, n_black_pieces: int) -> None:
        self.n_black_pieces = n_black_pieces

    def set_n_white_pieces(self, n_white_pieces: int) -> None:
        self.n_white_pieces = n_white_pieces
