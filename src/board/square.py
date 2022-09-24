from textual.widget import Widget
from textual.reactive import Reactive
from rich.panel import Panel
from rich.console import RenderableType
from src.constants import Piece


class Square(Widget):
    """ A square contains the pieces that has been placed on it """
    # When mouse_over or pieces changes the view will update
    mouse_over: Reactive[RenderableType] = Reactive(False)
    pieces: Reactive[RenderableType] = Reactive([])

    def __init__(self, x: int, y: int, parent) -> None:
        """
        Create empty square and sets the squares cordinets (x, y).

        :param x: Which column the square is in.
        :param y: Which row the square is in.
        :param parent: The board.
        :param move_handler: A function that moves/lay a piece.
        """
        super().__init__()
        self.x = x
        self.y = y
        self.reset()

    def render(self) -> Panel:
        return Panel(self.render_pieces(),
                     style=("on green" if self.mouse_over else ""))

    def render_pieces(self) -> str:
        # This is a ugly solution and requres a constant row of 7.
        # This can be improved but will work for now. I wrote this
        # late and it took me hours to get it to work. Be careful!
        # 7 rows but for some reason there is 8 elements?
        pieces_array = [[""], [""], [""], [""], [""], [""], [""], [""]]
        pieces_str = ""
        r = 0
        c = 0

        # first insert
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

    def on_click(self) -> None:
        # TODO: add piece depending on option and color
        self.parent.set_coords(self.x, self.y)
        self.parent.move_handler()

    def get_pieces(self) -> list(Piece):
        return self.pieces

    def add_piece(self, piece: Piece) -> None:
        _pieces = self.pieces.copy()  # Will cause bugs if not copy
        _pieces.insert(0, piece)
        self.set_pieces(_pieces)

    def remove_piece(self) -> Piece:
        if (len(self.pieces) != 0):
            return self.pieces.pop(0)  # the last piece is the bottom piece

    def rotate(self) -> None:
        if (not len(self.pieces)):
            return

        _pieces = self.pieces.copy()  # Will cause bugs if not copy
        _piece = _pieces.pop(0)  # remove the top piece

        match _piece:
            case Piece.WL:
                _piece = Piece.WS
            case Piece.BL:
                _piece = Piece.BS
            case Piece.WS:
                _piece = Piece.WL
            case Piece.BS:
                _piece = Piece.BL

        _pieces.insert(0, _piece)
        self.set_pieces(_pieces)

    def set_pieces(self, pieces: list(Piece)) -> None:
        self.pieces = pieces

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def reset(self) -> None:
        self.pieces = []  # The stack of pieces per square
