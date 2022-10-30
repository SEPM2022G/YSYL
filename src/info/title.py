from textual.widget import Widget
from rich.markdown import Markdown


class Title(Widget):
    def render(self) -> Markdown:
        MARKDOWN_TITLE = "# You stack You lose\n"
        MARKDOWN_TITLE += "Click on one of the squares to place a piece"
        MARKDOWN_TITLE += "a piece. You can click on one of the "
        MARKDOWN_TITLE += "options to change if you want to rotate a piece "
        MARKDOWN_TITLE += "or move stack. To move a stack you "
        MARKDOWN_TITLE += "click on a stack then click on the square "
        MARKDOWN_TITLE += "you want to move the pieces to"
        return Markdown(MARKDOWN_TITLE)