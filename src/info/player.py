from textual.widget import Widget
from textual.reactive import Reactive
from rich.panel import Panel
from rich.markdown import Markdown
from rich.console import RenderableType
from src.constants import Piece, Turn


class Player(Widget):
    """ Information about the turn and how many pices """
    # When turn, n_black_pieces, or n_white_pices
    # changes the view will update
    turn: Reactive[RenderableType] = Reactive(Turn.BLACK)
    n_black_pieces: Reactive[RenderableType] = Reactive("")
    n_white_pieces: Reactive[RenderableType] = Reactive("")

    def __init__(self) -> None:
        """
        Set turn to black and 21 pices to each player
        """
        super().__init__()
        self.reset()

    def render(self) -> Panel:
        MARKDOWN = "## Player info\n"
        MARKDOWN += f"It is **{self.turn.value}'s** turn\n\n"
        MARKDOWN += f"{self.n_black_pieces} black pieces "
        MARKDOWN += f"( {Piece.BS.value} and {Piece.BL.value} )\n\n"
        MARKDOWN += f"{self.n_white_pieces} white pieces "
        MARKDOWN += f"( {Piece.WS.value} and {Piece.WL.value} ) "
        return Markdown(MARKDOWN)

    def set_turn(self, turn: Turn) -> Turn:
        self.turn = turn
        return turn

    def get_turn(self) -> Turn:
        return self.turn

    def turn_black(self) -> Turn:
        return self.set_turn(Turn.BLACK)

    def turn_white(self) -> Turn:
        return self.set_turn(Turn.WHITE)

    def next_turn(self) -> Turn:
        if self.turn == Turn.WHITE:
            return self.turn_black()
        elif self.turn == Turn.BLACK:
            return self.turn_white()

    def set_n_black_pieces(self, n_black_pieces: int) -> None:
        self.n_black_pieces = n_black_pieces

    def set_n_white_pieces(self, n_white_pieces: int) -> None:
        self.n_white_pieces = n_white_pieces

    def reset(self) -> None:
        self.turn = Turn.BLACK  # Black is alwase the one who starts
        self.n_black_pieces = 21  # Initaly black has 21 pieces
        self.n_white_pieces = 21  # Initaly white has 21 pieces
