from textual.views import GridView
from src.board.square import Square
from src.constants import Piece, Turn, DIM


class Board(GridView):
    """ The right view containging all squares """

    def __init__(self, update_turn) -> None:
        """
        Create empty squares whith defined cordinets (x, y).

        :param update_turn: A function that updates the turn in info.
        """
        super().__init__()
        self.update_turn = update_turn
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

    def set_click(self, x: int, y: int) -> None:
        if(len(self.start) == 0):  # TODO: read options and see if we want to move a piece
            self.start.append(x)
            self.start.append(y)
        elif(len(self.to) == 0):
            self.to.append(x)
            self.to.append(y)

            # TODO: send request to API
            self.move_piece(self.to[0], self.to[1],
                            self.start[0], self.start[1])
            self.to = self.start = []

    def move_piece(self, x_end: int, y_end: int,
                   x_start: int = -1, y_start: int = -1) -> int:
        turn = self.update_turn()
        piece = (Piece.WL, Piece.BL)[turn == Turn.BLACK]

        if (True):  # FIXME: (x_start == -1) and (y_end == -1)):
            self.squares[y_end][x_end].add_piece(piece)
        else:
            piece = self.squares[x_start][y_start].remove_piece()
            self.squares[x_end][y_end].add_piece(piece)

        return 0

    def reset(self) -> None:
        self.squares = [[Square(x, y, self.move_piece)
                         for x in range(DIM)] for y in range(DIM)]
        self.to = []
        self.start = []
