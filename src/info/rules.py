from textual.widget import Widget
from rich.panel import Panel


class Rules(Widget):
    """ The rules of the game """

    def render(self) -> Panel:
        rules = '1. The game is played in turns. '
        rules += '2. The player with black pieces starts. '
        rules += '3. Any square that has the player’s color on top is "owned" by that player. '
        rules += '4. In a turn, a player can '
        rules += '4.1. Change a lying piece on an owned square to the standing position. '
        rules += '4.2. Place a new piece, in lying position, on any square with no standing piece. '
        rules += '4.3. Move an "owned" stack of pieces in any of the cardinal directions. The stack cannot skip squares, and has to leave behind an owned stack any time it moves to the next square. Standing pieces block movement. '
        rules += '5. When a player connects two opposite sides of the board with squares owned by them, they win. '
        rules += '6. If a player runs out of pieces and noone has won yet, the player who owns the most stacks wins. If both own an equal amount, it is a draw. '
        return Panel(rules, title="Rules")