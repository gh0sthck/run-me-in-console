import os

from zalgo_text import zalgo


def glitch_text(text: str) -> str:
    """Return zalgo text."""
    return zalgo.zalgo().zalgofy(text)


def clear_screen() -> None:
    """Clear console screen based on operating system."""
    os.system("cls") if os.name == "nt" else os.system("clear")