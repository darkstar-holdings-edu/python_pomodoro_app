from tkinter import Label

from .config import FONT_NAME, GREEN, YELLOW


class AppLabel(Label):
    def __init__(
        self,
        text: str,
        text_size: int,
        grid_row: int,
        grid_column: int,
    ) -> None:
        super().__init__(
            text=text,
            foreground=GREEN,
            background=YELLOW,
            font=(FONT_NAME, text_size, "normal"),
            padx=0,
            pady=10,
        )

        self.grid(row=grid_row, column=grid_column)

    def update_text(self, text: str, foreground: str = GREEN) -> None:
        self.config(text=text, foreground=foreground)
