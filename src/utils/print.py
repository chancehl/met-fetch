from typing import Literal


BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"


def color(s: str, c: Literal) -> str:
    """Prints s in the specified color"""
    return f"{c}{s}{RESET}"
