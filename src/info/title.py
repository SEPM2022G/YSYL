from textual.widget import Widget
from rich.markdown import Markdown


class Title(Widget):
    def render(self) -> Markdown:
        MARKDOWN_TITLE = "# PrettyGame\n"
        MARKDOWN_TITLE += "Click on one of the squares to lay out"
        MARKDOWN_TITLE += "a piece. You can click on one of the\n\n"
        MARKDOWN_TITLE += "options wheter you want the piece standing"
        MARKDOWN_TITLE += "or move stack. To move a stack you\n\n"
        MARKDOWN_TITLE += "click on a stack then click on the square"
        MARKDOWN_TITLE += "you want the botom piece to be."
        return Markdown(MARKDOWN_TITLE)
