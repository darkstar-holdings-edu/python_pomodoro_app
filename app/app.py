from tkinter import Tk
import math
import pygame

from .config import APP_NAME, GREEN, PINK, RED, YELLOW, CHECK_MARK
from .timer import AppTimer
from .button import AppButton
from .label import AppLabel

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECS_PER_MIN = 60

pygame.mixer.init()


class App(Tk):
    title_label: AppLabel
    timer_label: AppTimer
    start_button: AppButton
    reset_button: AppButton
    checkmark_label: AppLabel

    timer: str
    repetitions = 0
    timer_running = False

    def __init__(self) -> None:
        super().__init__()
        self.title(APP_NAME)
        self.config(padx=100, pady=50, background=YELLOW)

        self._init_ui()

    def _init_ui(self) -> None:
        self.title_label = AppLabel(
            text="Timer",
            text_size=40,
            grid_row=0,
            grid_column=1,
        )
        self.timer_label = AppTimer(grid_row=1, grid_column=1)
        self.start_button = AppButton(
            text="Start",
            grid_row=2,
            grid_column=0,
            event_handler=self.start_event_handler,
        )
        self.reset_button = AppButton(
            text="Reset",
            grid_row=2,
            grid_column=3,
            event_handler=self.reset_event_handler,
            state="disabled",
        )
        self.checkmark_label = AppLabel(
            text="",
            text_size=24,
            grid_row=3,
            grid_column=1,
        )

    def countdown(self, count: int) -> None:
        minutes = math.floor(count / 60)
        seconds = str(count % 60)
        if int(seconds) < 10:
            seconds = f"0{seconds}"

        self.timer_label.update_text(text=f"{minutes}:{seconds}")

        if count > 0:
            self.timer = self.after(1000, self.countdown, count - 1)
        else:
            self.start_timer()

            check_marks = ""
            work_sessions = math.floor(self.repetitions / 2)
            for _ in range(work_sessions):
                check_marks += CHECK_MARK

            self.checkmark_label.update_text(text=f"{check_marks}")

    def start_timer(self) -> None:
        self.repetitions += 1

        counter_seconds = 0
        if self.repetitions % 8 == 0:
            counter_seconds = LONG_BREAK_MIN * SECS_PER_MIN
            self.title_label.update_text("Break", foreground=RED)
            self.repetitions = 0
            self.play_long_break_sound()

        elif self.repetitions % 2 == 0:
            counter_seconds = SHORT_BREAK_MIN * SECS_PER_MIN
            self.title_label.update_text("Break", foreground=PINK)
            self.play_short_break_sound()

        else:
            counter_seconds = WORK_MIN * SECS_PER_MIN
            self.title_label.update_text("Work", foreground=GREEN)
            self.play_start_work_sound()

        self.timer_running = True
        self.countdown(counter_seconds)

    def start_event_handler(self) -> None:
        self.start_button.disable()
        self.reset_button.enable()
        self.start_timer()

    def reset_event_handler(self) -> None:
        self.repetitions = 0
        self.after_cancel(self.timer)
        self.timer_label.update_text(text="00:00")
        self.title_label.update_text(text="Timer", foreground=GREEN)
        self.checkmark_label.update_text(text="")
        self.start_button.enable()
        self.reset_button.disable()

    def play_sound(self, filename: str) -> None:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

    def play_short_break_sound(self) -> None:
        self.play_sound("assets/mixkit-software-interface-start-2574.wav")

    def play_start_work_sound(self) -> None:
        self.play_sound("assets/mixkit-software-interface-back-2575.wav")

    def play_long_break_sound(self) -> None:
        self.play_sound("assets/mixkit-uplifting-bells-notification-938.wav")
