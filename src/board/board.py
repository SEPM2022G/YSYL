from textual.views import GridView
from src.board.square import Square
from src.constants import BS, WS, BL, WL


class Board(GridView):
    def __init__(self) -> None:
        super().__init__()
        self.squares = []  # All the pices are located here
        for i in range(25):  # A 5x5 gives 25 squares
            self.squares.append(Square(""))

    async def on_mount(self) -> None:
        # The width of the squre
        width = 9

        # A board has 5(columns)x5(rows) hence repeat=5
        self.grid.add_column("column", repeat=5, size=(width*2))
        self.grid.add_row("row", repeat=5, size=width)

        # Populate squares with square widgets
        for x in self.squares:
            self.grid.add_widget(x)

        # TODO: This i is just a example so delete later
        self.move_piece(1, f"{WS}")
        mp = f"{BS} {BL}\n{BL}\n{WL}\n{BL}\n{WL}\n{BL}\n{WL}"
        self.move_piece(8, mp)
        self.move_piece(11, f"{WS}\n{BL}")

    def move_piece(self, square: int, pieces: str) -> None:
        self.squares[square].set_pieces(pieces)
