""" Imports all files needed for terminal """


__all__ = ['geky',
           'clear', 'color', 'pos',
           'RESET', 'ITALIC', 'BOLD', 'UNDERLINE']

RESET = "\x1b[0m"

BOLD = '\x1b[1m'
ITALIC = '\x1b[3m'
UNDERLINE = '\x1b[4m'


import pytgm.terminal.geky as geky
import pytgm.terminal.clear as clear
import pytgm.terminal.color as color
import pytgm.terminal.pos as pos
