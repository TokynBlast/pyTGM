"""
Exposes cls and color, while adding RESET, bold, italic and underline
"""
from .color import color
from .cls import cls

RESET = "\x1b[0m"

bold = '\x1b[1m'
italic = '\x1b[3m'
underline = '\x1b[4m'


__all__ = ["cls", "bold", "italic", "underline", "RESET"]
