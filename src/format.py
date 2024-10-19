from typing import Literal
from constants import RESET


def format_with_color(s: str, color: Literal["\u001b[32m", "\u001b[36m"]) -> str:
    return f"{color}{s}{RESET}"
