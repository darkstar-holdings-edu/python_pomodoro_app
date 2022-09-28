from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from app import App  # noqa: E402 Hide pygame hello message


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
