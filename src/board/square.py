from textual.widget import Widget
from textual.reactive import Reactive
from rich.panel import Panel
from rich.console import RenderableType
from src.constants import WL


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
        self.pieces = f"{WL}"

    def get_pieces(self) -> str:
        return self.pieces

    def set_pieces(self, pieces: str) -> None:
        self.pieces = pieces

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False
