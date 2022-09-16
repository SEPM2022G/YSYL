from textual.app import App
from textual.widgets import Placeholder
from textual.widget import Widget
from textual.reactive import Reactive
from rich.panel import Panel
from textual.views import GridView
from datetime import datetime
from rich.align import Align
from rich.console import RenderableType


class Title(Widget):
    def render(self) -> Panel:
        return Panel("PrettyGame")


class Tournament(Widget):
    def on_mount(self):
        self.score = "Your losing the tournament by 10"
        self.set_interval(1, self.refresh)

    def render(self) -> Panel:
        return Panel(self.score)

    def set_on_click(self, func):
        self.func = func

    def on_click(self):
        self.func()


class Player(Widget):
    def render(self) -> Panel:
        return Panel("Hennessy player")


class Square(Widget):
    mouse_over: Reactive[RenderableType] = Reactive(False)
    text: Reactive[RenderableType] = Reactive("")

    def __init__(self, text: str):
        super().__init__(text)
        self.text = text

    def render(self) -> Panel:
        return Panel(self.text, style=("on green" if self.mouse_over else ""))

    def on_click(self) -> None:
        if (self.text == "click"):
            self.text = ""
        else:
            self.text = "click"

    def update(self, text: str):
        self.text = text

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False


class Board(GridView):
    def __init__(self):
        super().__init__()
        self.squares = []

        for i in range(25):
            self.squares.append(Square(""))

    async def on_mount(self) -> None:
        # The width of the squre
        width = 10

        # A board has 5x5 (5 columns and 5 rows) hence repeat=5
        self.grid.add_column("column", repeat=5, size=(width*2))
        self.grid.add_row("row", repeat=5, size=width)

        # A 5x5 gives 25 squares
        for x in self.squares:
            self.grid.add_widget(x)

        self.move_pice(1, "help")

    def move_pice(self, square: int, text: str) -> None:
        self.squares[square].update(text)


class Info(GridView):
    def __init__(self):
        super().__init__()
        self.title_widget = Title()
        self.tournament_widget = Tournament()
        self.player1_widget = Player()
        self.player2_widget = Player()

    async def on_mount(self) -> None:
        self.grid.add_column("column", repeat=1)
        self.grid.add_row("row", repeat=4)

        self.grid.add_widget(self.title_widget)
        self.grid.add_widget(self.tournament_widget)
        self.grid.add_widget(self.player1_widget)
        self.grid.add_widget(self.player2_widget)


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

        self.info.tournament_widget.set_on_click(lambda: self.board.move_pice(2, "impresive"))


PrettyGameApp.run(log="textual.log")
