"""
Exposes everything for the library to import
"""
from .color import color
from .cls import cls
from .pos import pos

RESET = "\x1b[0m"

BOLD = '\x1b[1m'
ITALIC = '\x1b[3m'
UNDERLINE = '\x1b[4m'

__all__ = ["cls", "BOLD", "ITALIC", "UNDERLINE", "RESET", "pos", "color"]
