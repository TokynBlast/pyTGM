"""
Imports all files needed for terd
"""
from .click import click # pylint: disable=import-error
from .geky import geky  # pylint: disable=import-error

from .color import color #pylint:disable=import-error
from .cls import cls #pylint:disable=import-error
from .pos import pos #pylint:disable=import-error

RESET = "\x1b[0m"

BOLD = '\x1b[1m'
ITALIC = '\x1b[3m'
UNDERLINE = '\x1b[4m'

__all__ = ['click', 'geky',
           'cls', 'color', 'pos', 'RESET', 'ITALIC', 'BOLD', 'UNDERLINE']
