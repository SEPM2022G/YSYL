from textual.widget import Widget
from rich.panel import Panel


class Rules(Widget):
    """ The rules of the game """

    def render(self) -> Panel:
        rules = '1. The game is played in turns. \n'
        rules += '2. Each player starts with 21 pieces \n'
        rules += '3. The game begins with each player placing one of their opponents pieces on the board\n'
        rules += '4. Any square that has the player’s color is "owned" by that player. \n'
        rules += '5. In a turn, a player can: \n'
        rules += '- Change a lying piece on an owned square to the standing position. \n'
        rules += '- Place a new piece from their own pile, in any position, on any empty square or a square owned by the player with no standing piece . \n'
        rules += '- Move an "owned" stack of pieces, the bottom pieces stays on the square \n'
        rules += '- Move a single piece on the board to an owned or empty square with no standing piece\n'
        rules += '6. When a player connects the horizontal sides of the board with the same top pieces, with 1 turn allowed, they win. \n '
        return Panel(rules, title="Rules")
