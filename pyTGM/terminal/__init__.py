""" Imports all files needed for terminal """


__all__ = ['geky',
           'clear', 'color', 'pos',
           'RESET', 'ITALIC', 'BOLD', 'UNDERLINE']

RESET = "\x1b[0m"

BOLD = '\x1b[1m'
ITALIC = '\x1b[3m'
UNDERLINE = '\x1b[4m'


import pyTGM.terminal.geky as geky
import pyTGM.terminal.clear as clear
import pyTGM.terminal.color as color
import pyTGM.terminal.pos as pos
