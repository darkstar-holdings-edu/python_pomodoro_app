from tkinter import Button
from typing import Callable, Literal

from .config import YELLOW


class AppButton(Button):
    def __init__(
        self,
        text: str,
        grid_row: int,
        grid_column: int,
        event_handler: Callable[[], None],
        state: Literal["normal", "active", "disabled"] = "normal",
    ) -> None:
        super().__init__()
        self.config(
            text=text,
            highlightbackground=YELLOW,
            command=event_handler,
            state=state,
        )
        self.grid(row=grid_row, column=grid_column)

    def disable(self):
        self.config(state="disabled")

    def enable(self):
        self.config(state="normal")
