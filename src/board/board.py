import uuid
from src.GameEngine.Components.Validator import Validator
from src.info.info import Info
from src.info.player import Player
from textual.views import GridView
from src.board.square import Square
from src.constants import Piece, Turn, DIM, SelectedOption, Notification


class Board(GridView):
    """ The right view containging all squares """

    def __init__(self, info, io) -> None:
        """
        Create empty squares whith defined cordinets (x, y).

        :param info: Info component
        """
        super().__init__()
        self.io = io
        self.info = info
        self.move_count = 0;
        self.freezed = False;
        self.update_turn = info.player_widget.next_turn
        self.get_option = info.get_option
        self.get_turn = info.player_widget.get_turn
        self.set_stack = info.picked_up_stack_widget.set_pieces
        self.pop_stack = info.picked_up_stack_widget.remove
        self.old_state = { 'squares': [], 'white_pieces': 0, 'black_pieces': 0}
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

    def save_board(self):
        self.old_state = { 'squares': [], 'white_pieces': 0, 'black_pieces': 0}
        self.old_state['white_pieces'] = self.info.player_widget.n_white_pieces
        self.old_state['black_pieces'] = self.info.player_widget.n_black_pieces
        for i,x in enumerate(self.squares):
            self.old_state['squares'].append([])
            for j,n in enumerate(x):
                self.old_state['squares'][i].append(n.get_pieces().copy())

    def undo_board(self):
        self.update_turn(False)
        self.info.player_widget.n_white_pieces =  self.old_state['white_pieces']
        self.info.player_widget.n_black_pieces = self.old_state['black_pieces']
        for i,x in enumerate(self.squares):
            for j,n in enumerate(x):
                n.set_pieces(self.old_state['squares'][i][j].copy())
    

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
            if piece: 
                self.squares[y_end][x_end].add_piece(piece)
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

    def move_handler(self, opt = None) -> None:
        if opt == None: opt = self.get_option()

        # fetch coordinates, i.e. x and y position of a square
        x, y = self.get_coords()
        x_from, y_from = self.get_from_coords()

        valid_move = True
        decrease = False

        turn = self.get_turn()

        match opt:

            case SelectedOption.lying:
                if turn == Turn.BLACK and self.move_count <= 2:
                    valid_move = self.move_piece(Piece.BL, x, y)
                elif turn == Turn.WHITE and self.move_count <= 2:
                    valid_move = self.move_piece(Piece.WL, x, y)
                elif turn == Turn.BLACK:
                    valid_move = self.move_piece(Piece.WL, x, y)
                elif turn == Turn.WHITE:
                    valid_move = self.move_piece(Piece.BL, x, y)
                decrease = True

            case SelectedOption.standing:
                if turn == Turn.BLACK and self.move_count <= 2:
                    valid_move = self.move_piece(Piece.BS, x, y)
                elif turn == Turn.WHITE and self.move_count <= 2:
                    valid_move = self.move_piece(Piece.WS, x, y)
                elif turn == Turn.BLACK:
                    valid_move = self.move_piece(Piece.WS, x, y)
                elif turn == Turn.WHITE:
                    valid_move = self.move_piece(Piece.BS, x, y)
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
                    valid_move = self.move_piece(None,x, y, x_from, y_from)

            case SelectedOption.rotate:
                valid_move = self.rotate_piece(x, y)

        if (not self.hold) and valid_move:
            first_turn = (self.move_count <= 2)
            self.update_turn(decrease, first_turn)

    def perform_player_move(self):
        if self.freezed: return
        self.move_count = self.move_count + 1

        move = self.move_to_json()
        if move == None: return

        self.move_handler()
        self.io.writeInput(move)
        self.info.notification_widget.set_notification(Notification.AI_THINKING)
        self.freezed = True


    def perform_ai_move(self, move):
        self.move_count = self.move_count + 1
        self.info.notification_widget.set_notification(Notification.NORMAL)

        if int(move['outcome']) == 1:
            self.json_to_move(move['move'])
            self.save_board()
            self.freezed = False
        elif int(move['outcome']) == 2:
            self.info.notification_widget.set_notification(Notification.VICTORY)
        elif int(move['outcome']) == 3:
            self.json_to_move(move['move'])
            self.info.notification_widget.set_notification(Notification.LOSS)
        else:
            self.undo_board()
            self.info.notification_widget.set_notification(Notification.INVALID_MOVE)
            self.freezed = False

    def move_to_json(self): 
        first_turn = (self.move_count <= 2)
        move = {
            "src": {
            },
            "des": {
            },
            "pieces": 1,
            "first_turn": first_turn
        }

        move['id'] = str(uuid.uuid4())

        if self.get_turn() == Turn.WHITE:
            move['color'] = 0

        if self.get_turn() == Turn.BLACK:
            move['color'] = 1

        move['des']['pos_x'], move['des']['pos_y'] = self.get_coords()
        opt = self.get_option()

        x, y = self.get_coords()
        pieces = self.squares[y][x].get_pieces()

        if opt == SelectedOption.standing:
            move['src']['pos_x'] = -1
            move['src']['pos_y'] = -1
            move['des']['orientation'] = 1
            move['src']['pile'] = True

        if opt == SelectedOption.lying:
            move['src']['pos_x'] = -1
            move['src']['pos_y'] = -1
            move['des']['orientation'] = 0
            move['src']['pile'] = True

        if opt == SelectedOption.move:
            if len(pieces) > 0:
                curr_orientation = pieces[0]
            else: 
                return None
            move['src']['pos_x'], move['src']['pos_y'] = self.get_from_coords()
            move['des']['orientation'] = 0
            move['src']['pile'] = False
            if curr_orientation == Piece.BL or curr_orientation == Piece.WL:
                move['des']['orientation'] = 0
            if curr_orientation == Piece.BS or curr_orientation == Piece.WS:
                move['des']['orientation'] = 1

        #TODO: Correct stack behaviour
        if opt == SelectedOption.stack:
            move['src']['pos_x'], move['src']['pos_y'] = self.get_from_coords()
            move['src']['pile'] = False

        if opt == SelectedOption.rotate:
            if len(pieces) > 0:
                curr_orientation = pieces[0]
            else: return

            move['src']['pos_x'] = x
            move['src']['pos_y'] = y
            move['src']['pile'] = False

            if curr_orientation == Piece.BL or curr_orientation == Piece.WL:
                move['des']['orientation'] = 1
            if curr_orientation == Piece.BS or curr_orientation == Piece.WS:
                move['des']['orientation'] = 0

        return move

    def json_to_move(self,move):
        x = int(move['des']['pos_x'])
        y = int(move['des']['pos_y'])
        self.set_coords(x, y)
        if not move['src']['pile']:
            self.set_from_coords(move['src']['pos_x'], move['src']['pos_y'])
        else: self.set_from_coords(-1,-1)

        if int(move['des']['orientation']) == 1:
            self.move_handler(SelectedOption.standing)
        else:
            self.move_handler(SelectedOption.lying)

    def reset(self) -> None:
        self.squares = [[Square(x, y, self)
                         for x in range(DIM)] for y in range(DIM)]
        self.x = 0
        self.y = 0
        self.x_from = 0
        self.y_from = 0
        self.hold = False
        self.info.reset()
