from textual.app import App
from textual.widget import Widget
from textual.reactive import Reactive
from rich.panel import Panel
from textual.views import GridView
from rich.console import RenderableType
from rich.markdown import Markdown
from textual.widgets import Button
from enum import Enum

BS = "⯊"  # BLACK_STANDING
WS = "◠"  # WHITE_STANDING
BL = "▬"  # BLACK_LYING
WL = "▭"  # WHITE_LYING


class SelectedOption(Enum):
    lying = "Layout lying piece"
    standing = "Layout standing piece"
    stack = "Move stack"


class Title(Widget):
    def render(self) -> Markdown:
        MARKDOWN_TITLE = "# PrettyGame\n"
        MARKDOWN_TITLE += "Click on one of the squares to lay out"
        MARKDOWN_TITLE += "a piece. You can click on option menue\n\n"
        MARKDOWN_TITLE += "wheter you want the piece standing or move"
        MARKDOWN_TITLE += "a stack. To move a stack you click on\n\n"
        MARKDOWN_TITLE += "a stack then click on the square you want"
        MARKDOWN_TITLE += "the botom piece to be."
        return Markdown(MARKDOWN_TITLE)


class Tournament(Widget):
    # When score changes the view will update
    score: Reactive[RenderableType] = Reactive("Black 0/ White 0")

    def __init__(self) -> None:
        super().__init__()
        self.score
        self.n_games = ""
        self.set_score((0, 0))

    def render(self) -> Markdown:
        MARKDOWN = "## Tournament score\n"
        MARKDOWN += f"The score is *{self.score}*\n\n"
        MARKDOWN += f"You are plaing *{self.n_games}* games"
        return Markdown(MARKDOWN)

    def set_score(self, score: (int, int)) -> None:
        self.score = f"(Black {score[0]}/ White {score[0]})"

    def set_n_games(self, n_games: int) -> None:
        self.n_games = n_games

    def on_click(self) -> None:
        self.func()


class Player(Widget):
    # When turn, n_black_pieces, or n_white_pices
    # changes the view will update
    turn: Reactive[RenderableType] = Reactive("")
    n_black_pieces: Reactive[RenderableType] = Reactive("")
    n_white_pieces: Reactive[RenderableType] = Reactive("")

    def __init__(self) -> None:
        super().__init__()
        self.turn = "Black"  # Black is alwase the one who starts
        self.n_black_pieces = 21  # Initaly black has 21 pieces
        self.n_white_pieces = 21  # Initaly white has 21 pieces

    def render(self) -> Panel:
        MARKDOWN = "## Player info\n"
        MARKDOWN += f"It is **{self.turn}'s** turn\n\n"
        MARKDOWN += f"{BS} {self.n_black_pieces} black pieces\n\n"
        MARKDOWN += f"{WS} {self.n_white_pieces} white pieces"
        return Markdown(MARKDOWN)

    def set_turn(self, turn: str) -> None:
        self.turn = turn

    def set_n_black_pieces(self, n_black_pieces: int) -> None:
        self.n_black_pieces = n_black_pieces

    def set_n_white_pieces(self, n_white_pieces: int) -> None:
        self.n_white_pieces = n_white_pieces


class Options(Widget):
    # When selected changes the view will update
    selected: Reactive[RenderableType] = Reactive(False)

    def __init__(self, option: SelectedOption, func) -> None:
        super().__init__()
        self.option = option
        self.func = func

    def render(self) -> Button:
        return Button(self.option.value,
                      style=("on blue" if self.selected else ""))

    def set_selected(self, selected: bool) -> None:
        self.selected = selected

    def on_click(self) -> None:
        self.func(self.option)


class Square(Widget):
    # When mouse_over or pieces changes the view will update
    mouse_over: Reactive[RenderableType] = Reactive(False)
    pieces: Reactive[RenderableType] = Reactive("")

    def __init__(self, pieces: str) -> None:
        super().__init__()
        self.pieces = pieces

    def render(self) -> Panel:
        return Panel(self.pieces,
                     style=("on green" if self.mouse_over else ""))

    def on_click(self) -> None:
        # TODO: add piece depending on option and color
        self.pieces = f"{BS}\n{BL}\n{WL}\n{BL}\n{WL}\n{BL}\n{WL}"

    def get_pieces(self) -> str:
        return self.pieces

    def set_pieces(self, pieces: str) -> None:
        self.pieces = pieces

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False


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

    def move_piece(self, square: int, pieces: str) -> None:
        self.squares[square].set_pieces(pieces)


class Info(GridView):
    def __init__(self) -> None:
        super().__init__()
        self.title_widget = Title()
        self.tournament_widget = Tournament()
        self.player_widget = Player()
        self.option_lying_widget = Options(SelectedOption.lying,
                                           self.select_option)
        self.option_standing_widget = Options(SelectedOption.standing,
                                              self.select_option)
        self.option_stack_widget = Options(SelectedOption.stack,
                                           self.select_option)

    async def on_mount(self) -> None:
        self.grid.add_column("col", repeat=3)
        self.grid.add_row("row", repeat=4)
        self.grid.add_areas(
            title="col1-start|col3-end,row1",
            tournament="col1-start|col3-end,row2",
            player="col1-start|col3-end,row3",
            lying="col1,row4",
            standing="col2,row4",
            stack="col3,row4",
        )

        self.grid.place(title=self.title_widget,
                        tournament=self.tournament_widget,
                        player=self.player_widget,
                        lying=self.option_lying_widget,
                        standing=self.option_standing_widget,
                        stack=self.option_stack_widget)

        self.option_lying_widget.set_selected(True)

    def select_option(self, option) -> None:
        # Unselect all buttons
        self.option_lying_widget.set_selected(False)
        self.option_standing_widget.set_selected(False)
        self.option_stack_widget.set_selected(False)

        # Set selected to true for the correct option
        if (option == SelectedOption.lying):
            self.option_lying_widget.set_selected(True)
        elif (option == SelectedOption.standing):
            self.option_standing_widget.set_selected(True)
        elif (option == SelectedOption.stack):
            self.option_stack_widget.set_selected(True)
        else:  # sanity check
            print(f"No such option {option}")


class PrettyGameApp(App):
    async def on_load(self) -> None:
        """Sent before going in to application mode."""

        # Bind our basic keys
        await self.bind("q", "quit", "Quit")

    async def on_mount(self) -> None:
        self.board = Board()
        self.info = Info()
        await self.view.dock(self.board, edge="left", size=100)
        await self.view.dock(self.info, edge="top")

        self.info.tournament_widget.set_score((1, 1))
        self.info.tournament_widget.set_n_games(1)
        self.info.player_widget.set_turn("White")
        self.info.player_widget.set_n_white_pieces(20)
        self.info.player_widget.set_n_black_pieces(18)


PrettyGameApp.run(log="textual.log")
