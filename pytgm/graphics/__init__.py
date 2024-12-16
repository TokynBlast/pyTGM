# pytgm/graphics/__init__.py

from .color import color
from .cls import cls
from .Markup import Markup, bold, italic, underline  # Import other symbols as needed

RESET = "\x1b[0m"

__all__ = ["cls", "Markup", "bold", "italic", "underline", "RESET"]


