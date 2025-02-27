""" Imports all files needed for terminal """

from . import geky
from . import clear
from . import color
from . import pos

__all__ = ['geky',
           'clear', 'color', 'pos',
           'RESET', 'ITALIC', 'BOLD', 'UNDERLINE']

RESET = "\x1b[0m"

BOLD = '\x1b[1m'
ITALIC = '\x1b[3m'
UNDERLINE = '\x1b[4m'
INVIS = '\x1b[8m'
BLINK = '\x1b[5m'