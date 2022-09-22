from textual.views import GridView
from src.board.square import Square
from src.constants import Piece, Turn

DIM = 5

class Board(GridView):
    def __init__(self, update_turn) -> None:
        super().__init__()
        self.squares = [[Square([], x, y, self, self.move_piece) for x in range(DIM)] for y in range(DIM)]
        self.to = []
        self.start = []
        self.update_turn = update_turn

        #self.squares = []  # All the pices are located here
        #for i in range(25):  # A 5x5 gives 25 squares
        #    self.squares.append(Square([]))

    async def on_mount(self) -> None:
        # The width of the squre
        width = 9

        # A board has 5(columns)x5(rows) hence repeat=5
        self.grid.add_column("column", repeat=5, size=(width*2))
        self.grid.add_row("row", repeat=5, size=width)

        # Populate squares with square widgets
        for x in self.squares:
            for n in x:
                self.grid.add_widget(n)

        # TODO: This i is just a example so delete later
        #self.move_piece(1, [Piece.WS])
        #mp = [Piece.BS, Piece.BL, Piece.BL, Piece.WL, Piece.BL,
        #      Piece.WL, Piece.BL, Piece.WL]
        #self.move_piece(8, mp)
        #self.move_piece(11, [Piece.WS, Piece.BL])

        #self.move_piece(WHITE, 0, 2)

    def set_click(self, x: int, y: int) -> None:
        if(len(self.start) == 0): # TODO: read options and see if we want to move a piece
            self.start.append(x)
            self.start.append(y)
        elif(len(self.to) == 0):
            self.to.append(x)
            self.to.append(y)

            # TODO: send request to API
            self.move_piece(self.to[0], self.to[1], self.start[0], self.start[1])
            self.to = self.start = []

    def move_piece(self, x_end: int, y_end: int, x_start = -1, y_start = -1) -> int:
        turn = self.update_turn()
        piece = (Piece.WL, Piece.BL)[turn == Turn.BLACK]

        if (True):#(x_start == -1) and (y_end == -1)):
            self.squares[y_end][x_end].add_piece(piece)
        else:
            piece = self.squares[x_start][y_start].remove_piece()
            self.squares[x_end][y_end].add_piece(piece)

        return 0

    #def move_piece(self, x: int, y: int, pieces: Piece) -> None:
    #    self.squares[x][y].set_pieces([pieces])
