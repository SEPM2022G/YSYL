from textual.widget import Widget
from textual.widgets import Button
from textual.reactive import Reactive
from rich.console import RenderableType
from src.constants import SelectedOption


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

    def get_selected(self) -> bool:
        return self.selected

    def on_click(self) -> None:
        self.func(self.option)
