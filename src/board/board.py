from textual.views import GridView
from src.board.square import Square
from src.constants import Piece, Turn, DIM, SelectedOption


class Board(GridView):
    """ The right view containging all squares """

    def __init__(self, info) -> None:
        """
        Create empty squares whith defined cordinets (x, y).

        :param info: Info component
        """
        super().__init__()
        self.info = info
        self.update_turn = info.player_widget.next_turn
        self.get_option = info.get_option
        self.get_turn = info.player_widget.get_turn
        self.set_stack = info.picked_up_stack_widget.set_pieces
        self.pop_stack = info.picked_up_stack_widget.remove
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

    def set_from_coords(self, x: int, y: int) -> None:
        self.x_from = x
        self.y_from = y

    def get_from_coords(self) -> int:
        return self.x_from, self.y_from

    def set_coords(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def get_coords(self) -> int:
        return self.x, self.y

    def move_piece(self, piece : Piece,x_end: int, y_end: int,
                   x_start: int = -1, y_start: int = -1) -> bool:

        if (x_start == -1 and y_start == -1):
            self.squares[y_end][x_end].add_piece(piece)
        else:
            piece = self.squares[y_start][x_start].remove_piece()
            if piece: self.squares[y_end][x_end].add_piece(piece)
        # TODO: error handling?
        return True

    def drop_piece(self, x: int, y: int) -> bool:
        piece = self.pop_stack()
        if piece is None:
            self.hold = False
            return False
        else:
            self.squares[y][x].add_piece(piece)
            return True

    def rotate_piece(self, x: int, y: int) -> bool:
        return self.squares[y][x].rotate()

    def move_handler(self) -> None:
        # fetch coordinates, i.e. x and y position of a square
        x, y = self.get_coords()
        x_from, y_from = self.get_from_coords()

        valid_move = True
        decrease = False

        turn = self.get_turn()

        match self.get_option():

            case SelectedOption.lying:
                if turn == Turn.BLACK: valid_move = self.move_piece(Piece.WL, x, y)
                elif turn == Turn.WHITE: valid_move = self.move_piece(Piece.BL, x, y)
                decrease = True

            case SelectedOption.standing:
                if turn == Turn.BLACK: valid_move = self.move_piece(Piece.WS, x, y)
                elif turn == Turn.WHITE: valid_move = self.move_piece(Piece.BS, x, y)
                decrease = True

            case SelectedOption.stack:
                # move a stack
                if not self.hold:
                    stack = self.squares[y][x].pick_up_stack()
                    self.set_stack(stack)
                    if (len(stack) == 0):
                        valid_move = False
                else:
                    self.drop_piece(x, y)

            case SelectedOption.move:
                # move a piece
                if not self.hold:
                    valid_move = self.move_piece(None, x, y, x_from, y_from)

            case SelectedOption.rotate:
                valid_move = self.rotate_piece(x, y)

        if (not self.hold) and valid_move:
            self.update_turn(decrease)

    def reset(self) -> None:
        self.squares = [[Square(x, y, self)
                         for x in range(DIM)] for y in range(DIM)]
        self.x = 0
        self.y = 0
        self.x_from = 0
        self.y_from = 0
        self.hold = False
        self.info.reset()
