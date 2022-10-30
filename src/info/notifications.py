from textual.widget import Widget
from textual.reactive import Reactive
from rich.panel import Panel
from rich.align import Align
from rich.console import RenderableType
from src.constants import Notification


class Notifications(Widget):
    """ Shows notifications such as ivalid move and win status """
    notification: Reactive[RenderableType] = Reactive(Notification.NORMAL)

    def __init__(self) -> None:
        """
        Set notification to Notification.NORMAL
        """
        super().__init__()
        self.reset()

    def render(self) -> Panel:
        if self.notification == Notification.ERROR:
            notification_style = "red"
        elif self.notification == Notification.INVALID_MOVE:
            notification_style = "red"
        elif self.notification == Notification.VICTORY:
            notification_style = "yellow"
        elif self.notification == Notification.LOSS:
            notification_style = "blue"
        else:
            notification_style = ""

        # If you wish to remove the border change it to Padding
        # you can import it by using from rich.padding import Padding
        return Panel(
            Align.center(self.notification.value, vertical="middle"),
            style=notification_style)

    def set_notification(self, notification: Notification) -> None:
        self.notification = notification

    def reset(self) -> None:
        self.notification = Notification.NORMAL
