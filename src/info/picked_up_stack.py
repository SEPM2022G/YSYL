from textual.widget import Widget
from textual.reactive import Reactive
from rich.panel import Panel
from rich.console import RenderableType
from src.constants import Piece


class PickedUpStack(Widget):
    """ Shows the stack that is picked up """
    # When selected changes the view will update
    pieces: Reactive[RenderableType] = Reactive([])

    def __init__(self) -> None:
        super().__init__()
        self.reset()

    def render(self) -> Panel:
        return Panel(self.render_pieces(), title="Picked up stack")

    def render_pieces(self) -> str:
        # pieces_array = [[""], [""], [""], [""], [""], [""], [""], [""]]
        pieces_array = [[""] for _ in range(9)]
        pieces_str = ""
        r = 0
        c = 0

        # Create a two demensional array from pieces
        for i in range(len(self.pieces)):
            if r == len(pieces_array)-1:
                c += 1  # populate new column new
                r = 0  # new column starts with row 0

            if c >= 0:
                pieces_array[r].append("")  # new column

            pieces_array[r][c] = self.pieces[i].value  # a string
            r += 1  # populate next element in pieces_array

        for piece_row in pieces_array:
            for piece in piece_row:
                pieces_str += piece + " "

            pieces_str += "\n"  # New row

        return pieces_str

    def remove(self) -> Piece:
        if (len(self.pieces) != 0):
            return self.pieces.pop(0)  # the last piece is the bottom piece

    def get_pieces(self) -> list(Piece):
        return self.pieces

    def set_pieces(self, pieces: list(Piece)) -> None:
        self.pieces = pieces

    def reset(self) -> None:
        self.pieces = []
