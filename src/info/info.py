from textual.views import GridView
from src.constants import SelectedOption
from src.info.title import Title
from src.info.player import Player
from src.info.options import Options
from src.info.tournament import Tournament


class Info(GridView):
    def __init__(self) -> None:
        super().__init__()
        self.title_widget = Title()
        self.tournament_widget = Tournament()
        self.player_widget = Player()
        self.option_lying_widget = Options(SelectedOption.lying,
                                           self.select_option)
        self.option_standing_widget = Options(SelectedOption.standing,
                                              self.select_option)
        self.option_stack_widget = Options(SelectedOption.stack,
                                           self.select_option)

    async def on_mount(self) -> None:
        self.grid.add_column("col", repeat=3)
        self.grid.add_row("row", repeat=4)
        self.grid.add_areas(
            title="col1-start|col3-end,row1",
            tournament="col1-start|col3-end,row2",
            player="col1-start|col3-end,row3",
            lying="col1,row4",
            standing="col2,row4",
            stack="col3,row4",
        )

        self.grid.place(title=self.title_widget,
                        tournament=self.tournament_widget,
                        player=self.player_widget,
                        lying=self.option_lying_widget,
                        standing=self.option_standing_widget,
                        stack=self.option_stack_widget)

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
