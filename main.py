from tkinter import Button, Canvas, Label, PhotoImage, Tk
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"

reps = 0
timer = None


def main() -> None:
    window = Tk()
    window.title = "Pomodoro"
    window.config(padx=100, pady=50, background=YELLOW)

    def countdown(count: int) -> None:
        global timer

        minutes = math.floor(count / 60)
        seconds = count % 60
        if seconds < 10:
            seconds = f"0{seconds}"

        canvas.itemconfig(timer_count, text=f"{minutes}:{seconds}")

        if count > 0:
            timer = window.after(1000, countdown, count - 1)
        else:
            start_timer()

            check_marks = ""
            work_sessions = math.floor(reps / 2)
            for _ in range(work_sessions):
                check_marks += CHECK_MARK

            round_label.config(text=f"{check_marks}")

    def start_timer() -> None:
        global reps
        reps += 1

        counter_seconds = 0
        if reps % 8 == 0:
            counter_seconds = LONG_BREAK_MIN * 60
            title.config(text="Break", foreground=RED)
        elif reps % 2 == 0:
            counter_seconds = SHORT_BREAK_MIN * 60
            title.config(text="Break", foreground=PINK)
        else:
            # counter_seconds = WORK_MIN * 60
            counter_seconds = 10
            title.config(text="Work", foreground=GREEN)

        countdown(counter_seconds)

    def reset_timer() -> None:
        global reps
        reps = 0
        window.after_cancel(timer)
        canvas.itemconfig(timer_count, text="00:00")
        title.config(text="Timer", foreground=GREEN)
        round_label.config(text="")

    # UI Title
    title = Label(
        text="Timer",
        foreground=GREEN,
        background=YELLOW,
        font=(FONT_NAME, 40, "normal"),
        padx=0,
        pady=10,
    )
    title.grid(row=0, column=1)

    # UI Timer
    canvas = Canvas(
        width=200,
        height=224,
        background=YELLOW,
        highlightthickness=0,
    )
    background_img = PhotoImage(file="assets/tomato.png")
    canvas.create_image(100, 112, image=background_img)
    timer_count = canvas.create_text(
        100,
        130,
        text="00:00",
        fill="white",
        font=(FONT_NAME, 35, "bold"),
    )
    canvas.grid(row=1, column=1)

    # Buttons
    btn_start = Button()
    btn_start.config(text="Start", highlightbackground=YELLOW, command=start_timer)
    btn_start.grid(row=3, column=0)
    btn_reset = Button()
    btn_reset.config(text="Reset", highlightbackground=YELLOW, command=reset_timer)
    btn_reset.grid(row=3, column=2)

    # Loop Label
    round_label = Label(
        text="",
        foreground=GREEN,
        background=YELLOW,
        font=(FONT_NAME, 24, "normal"),
    )
    round_label.grid(row=4, column=1)

    window.mainloop()


if __name__ == "__main__":
    main()
