from textual.views import GridView
from src.board.square import Square
from src.constants import Piece, Turn, DIM, SelectedOption


class Board(GridView):
    """ The right view containging all squares """

    def __init__(self, update_turn, get_option) -> None:
        """
        Create empty squares whith defined cordinets (x, y).

        :param update_turn: A function that updates the turn in info.
        :param get_option: A function that returns
                           option laying, rotate, and stack
        """
        super().__init__()
        self.update_turn = update_turn
        self.get_option = get_option
        self.x = 0
        self.y = 0
        self.x_from = 0
        self.y_from = 0
        self.hold = False
        self.reset()

    async def on_mount(self) -> None:
        # The width of the squre
        width = 9

        # A board has 5(columns)x5(rows) hence repeat=5
        self.grid.add_column("column", repeat=DIM, size=(width*2))
        self.grid.add_row("row", repeat=DIM, size=width)

        # Populate squares with square widgets
        for x in self.squares:
            for n in x:
                self.grid.add_widget(n)

    def set_from_coords(self, x, y) -> None:
        self.x_from = x
        self.y_from = y

    def get_from_coords(self) -> int:
        return self.x_from, self.y_from

    def set_coords(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_coords(self) -> int:
        return self.x, self.y

    def move_piece(self, x_end: int, y_end: int,
                   x_start: int = -1, y_start: int = -1) -> int:
        turn = self.update_turn()
        piece = (Piece.WL, Piece.BL)[turn == Turn.BLACK]

        if (x_start == -1 and y_start == -1):
            self.squares[y_end][x_end].add_piece(piece)
        else:
            piece = self.squares[y_start][x_start].remove_piece()
            if piece:
                self.squares[y_end][x_end].add_piece(piece)
        # TODO: error handling?
        return 0

    def rotate_piece(self, x: int, y: int) -> None:
        self.squares[y][x].rotate()

    def move_handler(self) -> None:
        # fetch coordinates, i.e. x and y position of a square
        x, y = self.get_coords()
        x_from, y_from = self.get_from_coords()

        match self.get_option():
            case SelectedOption.lying:
                # place a lying piece
                self.move_piece(x, y)
            case SelectedOption.standing:
                # rotate a piece
                self.rotate_piece(x, y)
            case SelectedOption.stack:
                # move a stack
                pass
            case SelectedOption.move:
                # move a piece
                if not self.hold:
                    self.move_piece(x, y, x_from, y_from)

    def reset(self) -> None:
        self.squares = [[Square(x, y, self)
                         for x in range(DIM)] for y in range(DIM)]
        self.to = []
        self.start = []
