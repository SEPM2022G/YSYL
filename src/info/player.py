from textual.widget import Widget
from textual.reactive import Reactive
from rich.panel import Panel
from rich.markdown import Markdown
from rich.console import RenderableType
from src.constants import Piece, Turn, PlayerType


class Player(Widget):
    """ Information about the turn and how many pices """
    # When turn, n_black_pieces, or n_white_pices
    # changes the view will update
    turn: Reactive[RenderableType] = Reactive(Turn.BLACK)
    player1: Reactive[RenderableType] = Reactive(PlayerType.PLAYER1)
    player2: Reactive[RenderableType] = Reactive(PlayerType.PLAYER2)
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
        MARKDOWN += f"( {Piece.BS.value} and {Piece.BL.value} ) - {self.player1.value}\n\n"
        MARKDOWN += f"{self.n_white_pieces} white pieces "
        MARKDOWN += f"( {Piece.WS.value} and {Piece.WL.value} ) - {self.player2.value}"
        return Markdown(MARKDOWN)

    def set_turn(self, turn: Turn) -> Turn:
        self.turn = turn
        return turn

    def get_turn(self) -> Turn:
        return self.turn

    def next_turn(self, decrease: bool = False, first_turn: bool = False) -> Turn:
        if self.turn == Turn.WHITE:
            if (not first_turn) and decrease: self.decrease_n_white_pieces()
            elif first_turn and decrease_n_white_pieces: self.decrease_n_black_pieces()
            self.set_turn(Turn.BLACK)
        elif self.turn == Turn.BLACK:
            if (not first_turn) and decrease: self.decrease_n_black_pieces()
            elif first_turn and decrease_n_white_pieces: self.decrease_n_white_pieces()
            self.set_turn(Turn.WHITE)

    def set_n_black_pieces(self, n_black_pieces: int) -> None:
        self.n_black_pieces = n_black_pieces

    def set_n_white_pieces(self, n_white_pieces: int) -> None:
        self.n_white_pieces = n_white_pieces

    def get_n_black_pieces(self) -> int:
        return self.n_black_pieces

    def get_n_white_pieces(self) -> int:
        return self.n_white_pieces

    def decrease_n_black_pieces(self) -> None:
        self.n_black_pieces -= 1

    def decrease_n_white_pieces(self) -> None:
        self.n_white_pieces -= 1

    def set_player_color(self, player1: PlayerType, player2: PlayerType) -> None:
        self.player1 = player1
        self.player2 = player2

    def reset(self) -> None:
        self.turn = Turn.WHITE  # Black is alwase the one who starts
        self.n_black_pieces = 21  # Initaly black has 21 pieces
        self.n_white_pieces = 21  # Initaly white has 21 pieces
