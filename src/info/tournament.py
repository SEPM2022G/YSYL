from textual.widget import Widget
from textual.reactive import Reactive
from rich.markdown import Markdown
from rich.console import RenderableType


class Tournament(Widget):
    # When score changes the view will update
    score: Reactive[RenderableType] = Reactive("Black 0/ White 0")

    def __init__(self) -> None:
        """
        Set the tournament score to 0 for black and 0 for white
        """
        super().__init__()
        self.reset()

    def render(self) -> Markdown:
        MARKDOWN = "## Tournament score\n"
        MARKDOWN += f"The score is *{self.score}*\n\n"
        MARKDOWN += f"You are playing *{self.n_games}* games"
        return Markdown(MARKDOWN)

    def set_score(self, score: (int, int)) -> None:
        self.score = f"(Black {score[0]}/ White {score[0]})"

    def set_n_games(self, n_games: int) -> None:
        self.n_games = n_games

    def reset(self) -> None:
        self.set_score((0, 0))
