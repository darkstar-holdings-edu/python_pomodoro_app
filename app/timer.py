from tkinter import Canvas, PhotoImage

from .config import FONT_NAME, YELLOW


class AppTimer:
    canvas: Canvas
    background: PhotoImage
    timer_counter: int

    def __init__(self, grid_row: int, grid_column: int) -> None:
        canvas = Canvas(
            width=200,
            height=224,
            background=YELLOW,
            highlightthickness=0,
        )
        self.background = PhotoImage(file="assets/tomato.png")
        canvas.create_image(100, 112, image=self.background)
        self.timer_counter = canvas.create_text(
            100,
            130,
            text="00:00",
            fill="white",
            font=(FONT_NAME, 35, "bold"),
        )
        canvas.grid(row=grid_row, column=grid_column)

        self.canvas = canvas

    def update_text(self, text: str) -> None:
        self.canvas.itemconfig(self.timer_counter, text=text)
