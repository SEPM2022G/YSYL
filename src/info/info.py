from textual.views import GridView
from textual.widgets import Placeholder  # TODO: remove when widget for move stack exists
from src.constants import SelectedOption
from src.info.title import Title
from src.info.player import Player
from src.info.options import Options
from src.info.tournament import Tournament
from src.info.notifications import Notifications


class Info(GridView):
    """ This is the right view showing information about the game """

    def __init__(self) -> None:
        """
        Initialize all the widgets on the right side.
        """
        super().__init__()
        self.title_widget = Title()
        self.tournament_widget = Tournament()
        self.player_widget = Player()
        self.picked_up_stack_widget = Placeholder()  # TODO: change to proper widget
        self.option_lying_widget = Options(SelectedOption.lying,
                                           self.select_option)
        self.option_standing_widget = Options(SelectedOption.standing,
                                              self.select_option)
        self.option_stack_widget = Options(SelectedOption.stack,
                                           self.select_option)
        self.notification_widget = Notifications()

    async def on_mount(self) -> None:
        self.grid.add_column("col", repeat=3)
        self.grid.add_row("row", repeat=5)
        self.grid.add_areas(
            title="col1-start|col3-end,row1",
            picked_up_stack="col3,row2-start|row3-end",
            tournament="col1-start|col2-end,row2",
            player="col1-start|col2-end,row3",
            lying="col1,row4",
            standing="col2,row4",
            stack="col3,row4",
            notification="col1-start|col3-end,row5",
        )

        self.grid.place(title=self.title_widget,
                        picked_up_stack=self.picked_up_stack_widget,
                        tournament=self.tournament_widget,
                        player=self.player_widget,
                        lying=self.option_lying_widget,
                        standing=self.option_standing_widget,
                        stack=self.option_stack_widget,
                        notification=self.notification_widget)

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

    def get_option(self):
        if (self.option_lying_widget.get_selected()):
            return SelectedOption.lying
        elif (self.option_standing_widget.get_selected()):
            return SelectedOption.standing
        elif (self.option_stack_widget.get_selected()):
            return SelectedOption.stack
        else:
            return "None"

    def reset(self) -> None:
        self.tournament_widget.reset()
        self.player_widget.reset()
        self.notification_widget.reset()
