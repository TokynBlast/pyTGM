"""
Imports all files needed for terd
"""
from .geky import geky  # pylint: disable=import-error

from .color import color #pylint:disable=import-error
from .cls import cls #pylint:disable=import-error
from .pos import pos #pylint:disable=import-error

RESET = "\x1b[0m"

BOLD = '\x1b[1m'
ITALIC = '\x1b[3m'
UNDERLINE = '\x1b[4m'

__all__ = ['geky',
           'cls', 'color', 'pos',
           'RESET', 'ITALIC', 'BOLD', 'UNDERLINE']
