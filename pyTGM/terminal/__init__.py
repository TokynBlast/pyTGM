"""Everything that directly affects the terminal visuals"""
import importlib

geky = importlib.import_module('.geky', __name__)
clear = importlib.import_module('.clear', __name__)
color = importlib.import_module('.color', __name__)
pos = importlib.import_module('.pos', __name__)

RESET = "\x1b[0m"
BOLD = "\x1b[1m"
ITALIC = "\x1b[3m"
UNDERLINE = "\x1b[4m"
INVIS = "\x1b[8m"
BLINK = "\x1b[5m"

__all__ = [
    "geky",
    "clear",
    "color",
    "pos",
    "RESET",
    "ITALIC",
    "BOLD",
    "UNDERLINE",
    "INVIS",
    "BLINK",
]
