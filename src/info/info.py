from textual.views import GridView
from textual.widgets import ScrollView
from src.constants import SelectedOption, Piece
from src.info.title import Title
from src.info.rules import Rules
from src.info.player import Player
from src.info.options import Options
from src.info.notifications import Notifications
from src.info.picked_up_stack import PickedUpStack
from rich.panel import Panel


class Info(GridView):
    """ This is the right view showing information about the game """

    def __init__(self) -> None:
        """
        Initialize all the widgets on the right side.
        """
        super().__init__()
        self.title_widget = Title()
        self.player_widget = Player()
        self.rules_widget = ScrollView(contents=Rules())
        self.picked_up_stack_widget = PickedUpStack()  # TODO: change to proper widget
        self.option_rotate_widget = Options(SelectedOption.rotate,
                                              self.select_option)
        self.option_lying_widget = Options(SelectedOption.lying,
                                           self.select_option)
        self.option_standing_widget = Options(SelectedOption.standing,
                                              self.select_option)
        self.option_stack_widget = Options(SelectedOption.stack,
                                           self.select_option)
        self.option_move_widget = Options(SelectedOption.move,
                                           self.select_option)
        self.notification_widget = Notifications()

    async def on_mount(self) -> None:
        self.grid.add_column("col", repeat=4)
        self.grid.add_row("row", repeat=5)
        self.grid.add_areas(
            title="col1-start|col4-end,row1",
            picked_up_stack="col3,row2-start|row3-end",
            rules="col4,row2-start|row3-end",
            player="col1-start|col2-end,row2",
            rotate="col1,row3",
            lying="col1,row4",
            standing="col2,row4",
            move="col3,row4",
            stack="col4,row4",
            notification="col1-start|col4-end,row5",
        )

        self.grid.place(title=self.title_widget,
                        picked_up_stack=self.picked_up_stack_widget,
                        rules=self.rules_widget,
                        player=self.player_widget,
                        rotate=self.option_rotate_widget,
                        lying=self.option_lying_widget,
                        standing=self.option_standing_widget,
                        stack=self.option_stack_widget,
                        move=self.option_move_widget,
                        notification=self.notification_widget)

        self.option_lying_widget.set_selected(True)

    def select_option(self, option) -> None:
        # Unselect all buttons
        self.option_lying_widget.set_selected(False)
        self.option_standing_widget.set_selected(False)
        self.option_stack_widget.set_selected(False)
        self.option_move_widget.set_selected(False)
        self.option_rotate_widget.set_selected(False)

        # Set selected to true for the correct option
        if (option == SelectedOption.lying):
            self.option_lying_widget.set_selected(True)
        elif (option == SelectedOption.standing):
            self.option_standing_widget.set_selected(True)
        elif (option == SelectedOption.stack):
            self.option_stack_widget.set_selected(True)
        elif (option == SelectedOption.move):
            self.option_move_widget.set_selected(True)
        elif (option == SelectedOption.rotate):
            self.option_rotate_widget.set_selected(True)
        else:  # sanity check
            print(f"No such option {option}")

    def get_option(self):
        if (self.option_lying_widget.get_selected()):
            return SelectedOption.lying
        elif (self.option_standing_widget.get_selected()):
            return SelectedOption.standing
        elif (self.option_stack_widget.get_selected()):
            return SelectedOption.stack
        elif (self.option_move_widget.get_selected()):
            return SelectedOption.move
        elif (self.option_rotate_widget.get_selected()):
            return SelectedOption.rotate
        else:
            return "None"

    def reset(self) -> None:
        self.player_widget.reset()
        self.notification_widget.reset()
